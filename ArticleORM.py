# coding=utf-8
__author__ = 'YU'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
basedir = os.path.abspath(os.path.dirname(__file__))



Base = declarative_base()


# 创建单表
class Article(Base):
    __tablename__ = 'article'
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


class ArticleORMHelper(object):

    def __init__(self, database_name):
        DATABASE_PATH = os.path.join(basedir, database_name)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
        self.db_engine = create_engine(SQLALCHEMY_DATABASE_URI)


    def create_db(self):

        Base.metadata.create_all(self.db_engine)  # 创建表
        Session = sessionmaker(bind=self.db_engine)
        self.session = Session()

    def drop_db(self):
        Base.metadata.drop_all(self.db_engine)   #删除表

    def addArticle(self, article):

        # 插入数据
        isSucess = False
        self.session.add(article)
        self.session.commit()
        isSucess = True
        return isSucess

    def query_all_with_article_name_password(self, users):
        # 查询所有相同于name，password数据
        userList=self.session.query(Article).filter_by(title=users.title,text=users.text).all()
        return userList


    def query_all_articles(self):
        # 查询所有相同于name，password数据
        userList=self.session.query(Article).all()
        print len(userList)
        return userList









