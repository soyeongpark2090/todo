from flask_sqlalchemy import SQLAlchemy
import os
import random
from flask import Flask, render_template, request, redirect, url_for

# Flask 애플리케이션 초기화
app = Flask(__name__)

# DB 기본코드

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


# 테이블 생성
class Rsp_play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_pick = db.Column(db.String(100), nullable=False)    # 사용자 선택
    computer_pick = db.Column(db.String(100), nullable=False)        # 컴퓨터 선택
    result = db.Column(db.String(100), nullable=False)        # 승패 결과

    # def __repr__(self):
    #     return f'{self.username} {self.title} 추천 by {self.username}'


with app.app_context():
    db.create_all()


# 가위바위보 게임
def check_winner():
    
    rsp = ['가위', '바위', '보']
    computer_pick = random.choice(rsp)
    user_pick = request.form.get("user_pick")

    if user_pick not in rsp:
        return ('유효한 입력이 아닙니다')

    if user_pick == computer_pick:
        result = '비겼어요!'
    elif (user_pick == '가위' and computer_pick == '보') or (user_pick == '바위' and computer_pick == '가위') or (user_pick == '보' and computer_pick == '바위'):
        result = '사용자 승리!'
    else:
        result = '컴퓨터 승리!'

    return user_pick, computer_pick, result


@app.route("/submit", methods=['POST'])
def save_to_db():
    user_pick = request.form.get("user_pick")
    a = check_winner()
    user_pick = a[0]
    computer_pick = a[1]
    result = a[2]

    new_play = Rsp_play(user_pick=user_pick, computer_pick=computer_pick,
                        result=result)
    db.session.add(new_play)
    db.session.commit()
    return redirect(url_for('home'))

# @app.route("/record")
# def record():
#     win_cnt = 0
#     draw_cnt = 0
#     lost_cnt = 0
    
#     record_list = Rsp_play.query.all()
#     for record in record_list:
#         if record.result == '사용자 승리!':
#             win_cnt += 1
#         elif record.result == '비겼어요!':
#             draw_cnt += 1
#         else:
#             lost_cnt += 1
#         return render_template('index.html', win_cnt = win_cnt, draw_cnt = draw_cnt, lost_cnt = lost_cnt)
            

# 메인페이지
@app.route("/")
def home():
    pick_list = Rsp_play.query.all()
    
    win_cnt = 0
    draw_cnt = 0
    lost_cnt = 0
    
    record_list = Rsp_play.query.all()
    for record in record_list:
        if record.result == '사용자 승리!':
            win_cnt += 1
        elif record.result == '비겼어요!':
            draw_cnt += 1
        else:
            lost_cnt += 1
    return render_template('index.html', data=pick_list, win_cnt = win_cnt, draw_cnt = draw_cnt, lost_cnt = lost_cnt)


if __name__ == '__main__':
    app.run(debug=True)
