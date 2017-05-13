# coding=utf-8
__author__ = 'YU'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index, BLOB
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
class Picture_reptile(Base):
    __tablename__ = 'picture_reptile'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    image = Column(BLOB)
    image_base64= Column(String(100000))

    def __init__(self, title, image,image_base64):
        self.title = title
        self.image = image
        self.image_base64=image_base64

    __table_args__ = (
        UniqueConstraint('id', 'title', name='uix_id_title'),
        Index('idx_image_base64 ', 'image_base64' ),
    )


class Picture_reptileORMHelper(object):
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

    def addPicture(self, music):

        # 插入数据
        isSucess = False
        self.session.add(music)
        self.session.commit()
        isSucess = True
        return isSucess

    def query_all_with_Picture_name_password(self, users):
        # 查询所有相同于name，password数据
        userList=self.session.query(Picture_reptile).filter_by(title=users.title ).all()
        return userList

    def query__Picture(self):
        userList = self.session.query(Picture_reptile).all()
        print len(userList)
        return userList

