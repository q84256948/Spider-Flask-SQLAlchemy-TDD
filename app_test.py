# coding=utf-8
__author__ = 'YU'
import os
import unittest

from app import app,user_orm_helper

from UserORM import Users





class BasicTestCase(unittest.TestCase):


    def test_database(self):
        """inital test. ensure that the database exists"""
        tester = os.path.exists("flaskr.db")
        self.assertTrue(tester)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        print "the basedir ---->",basedir
        app.config['TESTING'] = True
        # db_path='sqlite:///' + \
        # os.path.join(basedir, TEST_DB)
        # app.config['SQLALCHEMY_DATABASE_URI'] =db_path
        # print 'db_path--->',db_path
        self.app = app.test_client()




    def tearDown(self):
        """Destroy blank temp database after each test"""
        self.app=None


    def signUp(self, username, password):
        """Login helper function"""
        return self.app.post('/signUp', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)


    def Login(self, username, password):
        """Login helper function"""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def addArticle(self, title, text):
        """Login helper function"""
        return self.app.post('/addArticle', data=dict(
            title=title,
            text=text
        ), follow_redirects=True)

    def index(self, title, text):
        """Login helper function"""
        return self.app.post('/index', data=dict(
            title=title,
            text=text
        ), follow_redirects=True)

    def logout(self):
        """Logout helper function"""
        return self.app.get('/logout', follow_redirects=True)

    def allArticle(self):
        """Logout helper function"""
        return self.app.get('/allArticle', follow_redirects=True)

    def allMovie(self):
        """Logout helper function"""
        return self.app.get('/allMovie', follow_redirects=True)

    def allMusic(self):
        """Logout helper function"""
        return self.app.get('/allMusic', follow_redirects=True)

    def allPicture(self):
        """Logout helper function"""
        return self.app.get('/allPicture', follow_redirects=True)

    def Picture(self):
        """Logout helper function"""
        return self.app.get('/Picture', follow_redirects=True)


    def testSignUpUser(self):

        rv = self.signUp("tom2333", "tom12333")
        print type(rv)
        print rv.data
        user_orm_helper.delete(Users("tom2333", "tom12333"))

        self.assertIn("Sign Up Success!",rv.data)


    def testSignUpUserLose(self):
        rv = self.signUp("tom", "tom123")
        rv = self.signUp("tom", "tom123")
        self.assertIn("Sign Up Lose!",rv.data)


    def testLoginSuccess(self):
        rv = self.signUp("tom", "tom123")
        rv=self.Login("tom","tom123")
        self.assertIn("Login Success", rv.data)

    def testLoginFail(self):
        rv=self.Login("tom242424dggghjh","tom12344423234")
        self.assertIn("Login Failed", rv.data)


    def test_userLogout(self):
        rv = self.Login("tom", "tom123")
        self.assertIn("Login Success", rv.data)
        rv = self.logout()
        self.assertIn(b'You were logged out', rv.data)


    def test_add_ArrtcleORMSuccess(self):
        rv = self.addArticle("fish","fish is good!")
        self.assertIn("Music published successfully", rv.data)

    def test_allArticle(self):
        rv = self.allArticle()
        self.assertNotIn("No entries yet. Add some!", rv.data)

    def test_allMusic(self):
        rv = self.allMusic()
        self.assertNotIn("No entries yet. Add some!", rv.data)

    def test_allMovie(self):
        rv = self.allMovie()
        self.assertNotIn("No entries yet. Add some!", rv.data)


    def test_Picture(self):
        rv = self.Picture()
        self.assertNotIn("No entries yet!", rv.data)

    def test_allPicture(self):
        rv = self.allPicture()
        self.assertNotIn("No entries yet. Add some!", rv.data)

























if __name__ == '__main__':
    unittest.main()



