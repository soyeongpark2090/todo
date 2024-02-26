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


users = []
for i in range(3):
    name = input(f'회원 이름{i+1}을 입력하세요 : ')
    username = input(f'회원 아이디{i+1}를 입력하세요: ')
    password = input(f'회원 {i+1}의 비밀번호를 입력하세요: ')
    users.append(Member(name, username, password))

for user in users:
    print(user.name)


posts = []
for i in range(9):
    title = input(f'게시물{i+1}의 제목을 입력하세요: ')
    content = input(f'게시물{i+1}의 내용을 입력하세요: ')
    author = input(f'게시물{i+1}의 작성자를 입력하세요: ')
    posts.append(Post(title, content, author))

# p1 = Post('title_1', '민지는 10살입니다', m1.username)
# p2 = Post('title_2', '영수는 25살입니다', m2.username)
# p3 = Post('title_3', '민지는 여자입니다', m3.username)
# p4 = Post('title_4', '철수는 16살입니다', m1.username)
# p5 = Post('title_5', '민호는 40살입니다', m2.username)
# p6 = Post('title_6', '지연은 32살입니다', m3.username)
# p7 = Post('title_7', '민지는 동생이 있습니다', m1.username)
# p8 = Post('title_8', '준영은 23살입니다', m2.username)
# p9 = Post('title_9', '민지의 아빠는 45살입니다', m3.username)

for user in users:
    m_posts = list(filter(lambda post: post.author == user.username, posts))
    for post in m_posts:
        print(f'회원 아이디 {user.username}님은 {post.title}를 작성하셨습니다')

m_filter = list(filter(lambda post: '민지' in post.content, posts))
for post in m_filter:
    print(post.title)
