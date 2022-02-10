from database import session
from models import User, Profile, Post, Comment, Tag

from random import sample, randint

if __name__ == '__main__':

    print("CRIANDO USUÁRIOS")

    users = session.query(User).all()

    if len(users) == 0:
        users_list = [
            {
                'email': 'lorena@email.com',
                'passwd': '123456',
                'profile': {
                    'first_name': 'Lorena',
                    'last_name': 'Silva'
                }
            }, {
                'email': 'maria@email.com',
                'passwd': '123456',
                'profile': {
                    'first_name': 'Maria',
                    'last_name': 'Cardoso'
                }
            }, {
                'email': 'Carla@email.com',
                'passwd': '123456',
                'profile': {
                    'first_name': 'Carla',
                    'last_name': 'Rodrigues'
                }
            }
        ]

        for user_info in users_list:
            user = User(email=user_info.get('email'), passwd=user_info.get('passwd'))
            session.add(user)
            session.commit()

            user_info['profile'].update({'id': user.id})

            user_profile = Profile(**user_info.get('profile'))
            session.add(user_profile)
            session.commit()

    posts = session.query(Post).all()

    if len(posts) == 0:
        posts_list = [
            {
                'user_id': 1,
                'title': 'A linguagem de programação Python',
                'body': 'Python é uma linguagem fácil de ser aprendida'
            },
            {
                'user_id': 1,
                'title': 'A linguagem de programação Javascript',
                'body': 'Javascript é uma linguagem importante de ser aprendida'
            },
            {
                'user_id': 1,
                'title': 'A linguagem de programação C++',
                'body': 'C++ é uma linguagem difícil de ser aprendida'
            },
            {
                'user_id': 2,
                'title': 'A linguagem de programação Golang',
                'body': 'Golang é uma linguagem de alta performance construída pela google'
            }, {
                'user_id': 3,
                'title': 'A linguagem de programação Java',
                'body': 'Java é uma linguagem com muitos usos'
            }
        ]

        for post_info in posts_list:
            post = Post(**post_info)
            # Post(user_id=232, title=2323, body=dfdf)
            # User -> id 10
            # [Post(<id=1>),Post(<id=2>), Post(<id=3>)]
            user.posts.append(Post)
            # post.user = User
            session.add(post)
            session.commit()

    tags = session.query(Tag).all()

    if len(tags) == 0:
        tags_list = [
            "programação", "ti", "2022", "linguagem", "google"
        ]

        for tag_info in tags_list:
            tag = Tag(tag=tag_info)
            session.add(tag)
            session.commit()

    tags = session.query(Tag).all()

    # Associando tags aos posts
    for post in posts:

        if len(post.tags) == 0:
            for i in range(randint(1, 5)):
                post.tags.append(
                    tags[i]
                )
                session.add(post)
            session.commit()

        # tag.posts.append(Post<id=10>)
        # tags.posts = [Post(<id=11>), Post(<id=13>), Post(<id=20>)