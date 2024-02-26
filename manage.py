class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print('회원 이름: ', self.name)
        print('회원 아이디: ', self.username)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


m1 = Member('김네모', 'square', 12345)
m2 = Member('박세모', 'triangle', 20901)
m3 = Member('최동글', 'donggle', 84636)

members = []
members.append(m1)
members.append(m2)
members.append(m3)

# # print(members) // 이렇게는 확인 불가.
for member in members:
    print(member.name)
# username_value = [member.username for member in members]

posts = []
p1 = Post('title_1', '민지는 10살입니다', m1.username)
p2 = Post('title_2', '영수는 25살입니다', m2.username)
p3 = Post('title_3', '민지는 여자입니다', m3.username)
p4 = Post('title_4', '철수는 16살입니다', m1.username)
p5 = Post('title_5', '민호는 40살입니다', m2.username)
p6 = Post('title_6', '지연은 32살입니다', m3.username)
p7 = Post('title_7', '민지는 동생이 있습니다', m1.username)
p8 = Post('title_8', '준영은 23살입니다', m2.username)
p9 = Post('title_9', '민지의 아빠는 45살입니다', m3.username)

adds = p1, p2, p3, p4, p5, p6, p7, p8, p9

for add in adds:
    posts.append(add)

# posts.extend(adds)도 가능
# post = [p1~p9]

m1_posts = list(filter(lambda post: post.author == m1.username, posts))
m2_posts = list(filter(lambda post: post.author == m2.username, posts))
m3_posts = list(filter(lambda post: post.author == m3.username, posts))
for post in m1_posts:
    print(f'회원 아이디 {m1.username}님은 {post.title}를 작성하셨습니다')
for post in m2_posts:
    print(f'회원 아이디 {m2.username}님은 {post.title}를 작성하셨습니다')
for post in m3_posts:
    print(f'회원 아이디 {m3.username}님은 {post.title}를 작성하셨습니다')

m_filter = list(filter(lambda post: '민지' in post.content, posts))
for post in m_filter:
    print(post.title)
