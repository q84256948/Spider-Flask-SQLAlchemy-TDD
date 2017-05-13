# imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# grabs the folder where the script runs
from MusicORM import MusicORMHelper
from MovieORM import MovieORMHelper
from PictureORM import PictureORMHelper
from UserORM import UserORMHelper, Users
from ArticleORM import  ArticleORMHelper,Article
from Picture_ReptileORM import Picture_reptileORMHelper

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# create app
app = Flask(__name__)
app.config.from_object(__name__)
# db = SQLAlchemy(app)
user_orm_helper=UserORMHelper(DATABASE)
user_orm_helper.create_db()
article_orm_helper=ArticleORMHelper(DATABASE)
article_orm_helper.create_db()
music_orm_helper=MusicORMHelper(DATABASE)
music_orm_helper.create_db()
movie_orm_helper=MovieORMHelper(DATABASE)
movie_orm_helper.create_db()
picture_orm_helper=PictureORMHelper(DATABASE)
picture_orm_helper.create_db()
picture_orm=Picture_reptileORMHelper(DATABASE)
picture_orm.create_db()




@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    user_name=request.form['username']
    pass_word=request.form['password']
    user=Users(user_name,pass_word)
    isSuccess=user_orm_helper.addUser(user)
    if isSuccess:
        return render_template('signUpSuccess.html')
    else:
        return render_template('signUpLose.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    user_name=request.form['username']
    pass_word=request.form['password']
    user=Users(user_name,pass_word)
    isSuccess=user_orm_helper.query_all_with_user_name_password(user)
    if len(isSuccess) > 0:
        session['logged_in'] = True
        return render_template('loginSuccess.html')
    else:
        return render_template('loginFail.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
    """Searches the database for entries, then displays them."""
    return render_template('index.html')

@app.route('/login_idx', methods=['GET', 'POST'])
def login_idx():
    """Searches the database for entries, then displays them."""
    return render_template('login_idx.html')

@app.route('/signUp_idx', methods=['GET', 'POST'])
def signUp_idx():
    """Searches the database for entries, then displays them."""
    return render_template('signUp_idx.html')




@app.route('/addArticle', methods=['GET', 'POST'])
def addArticle():
    """User logout/authentication/session management."""

    title=request.form['title']
    text=request.form['text']
    article=Article(title,text)

    isSucess=article_orm_helper.addArticle(article)


    articleList=article_orm_helper.query_all_with_article_name_password(article)
    if (isSucess and len(articleList) > 0):

        return render_template('addArticleSuccess.html',entries=articleList)



@app.route('/allArticle', methods=['GET', 'POST'])
def allArticle():
    """User logout/authentication/session management."""

    articleList=article_orm_helper.query_all_articles()
    print len(articleList)
    if (len(articleList) > 0):

        return render_template('allArticleSuccess.html',entries=articleList)

@app.route('/allMusic', methods=['GET', 'POST'])
def allMusic():
    """User logout/authentication/session management."""

    articleList=music_orm_helper.query_all_musices()
    print len(articleList)
    if (len(articleList) > 0):

        return render_template('allMusicSuccess.html',entries=articleList)

@app.route('/allMovie', methods=['GET', 'POST'])
def allMovie():
    """User logout/authentication/session management."""

    articleList=movie_orm_helper.query_all_movie()
    print len(articleList)
    if (len(articleList) > 0):

        return render_template('allMovieSuccess.html',entries=articleList)



@app.route('/allPicture', methods=['GET', 'POST'])
def allPicture():
    """User logout/authentication/session management."""

    articleList = picture_orm_helper.query_all_Picture()


    print len(articleList)
    if (len(articleList) > 0):
        return render_template('allPictureSuccess.html', entries=articleList)
    else:
        return render_template('allPictureSuccess.html')


@app.route('/Picture', methods=['GET', 'POST'])
def Picture():
    """User logout/authentication/session management."""
    articleList = picture_orm.query__Picture()
    print len(articleList)
    if (len(articleList) > 0):
        return render_template('allPicture.html', entries=articleList)
    else:
        return render_template('allPicture.html')


if __name__ == '__main__':
    app.run()
