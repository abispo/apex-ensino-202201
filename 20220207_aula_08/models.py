from datetime import datetime

from database import Base

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

posts_tags = Table('tb_posts_tags', Base.metadata,
                   Column('post_id', Integer, ForeignKey('tb_posts.id'), primary_key=True),
                   Column('tag_id', Integer, ForeignKey('tb_tags.id'), primary_key=True)
                )


class Product(Base):

    __tablename__ = 'tb_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    obs = Column(String(200))


class User(Base):

    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    passwd = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    profile = relationship("Profile", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")


class Profile(Base):

    __tablename__ = 'tb_profiles'

    id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", uselist=False, back_populates="profile")


class Post(Base):

    __tablename__ = 'tb_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'))
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", uselist=False, back_populates='posts')
    comments = relationship("Comment", back_populates='post')
    tags = relationship("Tag", secondary=posts_tags, back_populates="posts")


class Comment(Base):
    __tablename__ = 'tb_comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('tb_posts.id'))
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    post = relationship("Post", uselist=False, back_populates='comments')


class Tag(Base):

    __tablename__ = 'tb_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String(200), nullable=False)

    posts = relationship("Post", secondary=posts_tags, back_populates="tags")
