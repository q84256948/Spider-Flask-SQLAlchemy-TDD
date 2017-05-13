# coding=utf-8
__author__ = 'YU'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flaskr.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()


# 创建单表
class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    text = Column(String(1000))

    def __init__(self, title, text):
        self.title = title
        self.text = text

    __table_args__ = (
        UniqueConstraint('id', 'title', name='uix_id_title'),
        Index('idx_title_text', 'title', 'text'),
    )


class MovieORMHelper(object):
    def __init__(self, database_name):
        DATABASE_PATH = os.path.join(basedir, database_name)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)

    def create_db(self):

        Base.metadata.create_all(self.engine)  # 创建表
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def drop_db(self):
        Base.metadata.drop_all(self.engine)   #删除表

    def addMovie(self, music):

        # 插入数据
        isSucess = False
        self.session.add(music)
        self.session.commit()
        isSucess = True
        return isSucess

    def query_all_with_movie_name_password(self, users):
        # 查询所有相同于name，password数据
        userList=self.session.query(Movie).filter_by(title=users.title, text=users.text).all()
        return userList

    def query_all_movie(self):
        userList = self.session.query(Movie).all()
        print len(userList)
        return userList


