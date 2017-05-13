# coding=utf-8
__author__ = 'YU'
import os
import unittest
from UserORM import Users,UserORMHelper




TEST_DB = 'test.db'

class UserORMHelperTestCase(unittest.TestCase):



    def setUp(self):
        """Set up a blank temp database before each test"""
        self.helper=UserORMHelper("user.db")
        self.helper.drop_db()
        self.helper.create_db()


    def tearDown(self):
        """Destroy blank temp database after each test"""
        self.helper.drop_db()

    def test_add(self):
        # 插入测试
        isSuccess=self.helper.addUser(Users("tome", "tom jobn"))
        self.assertTrue(isSuccess)
        isSuccess=self.helper.addUser(Users("tome", "tom jobn"))
        self.assertFalse(isSuccess)


    def test_delete(self):
        # 删除测试
        isSuccess = self.helper.addUser(Users("tome", "tom jobn"))
        self.assertTrue(isSuccess)
        isSucess=self.helper.delete(Users("tome", "tom jobn"))
        self.assertTrue(isSucess)

    def test_query_all(self):
        # 查询所有相同name数据测试
         isSuccess=self.helper.addUser(Users("tome", "tom jobn"))
         self.assertTrue(isSuccess)
         isSuccess=self.helper.addUser(Users("tome", "tom jobn2"))
         self.assertTrue(isSuccess)
         isSuccess=self.helper.addUser(Users("tome", "tom jobn3"))
         self.assertTrue(isSuccess)
         userList=self.helper.query_all_with_user_name(Users("tome", "tom jobn"))
         # print userList
         self.assertEqual(len(userList),3)


    def test_query_none(self):
        # 查询相同name数据，取第一个  测试
         userList=self.helper.query_first_with_user_name(Users("tom", "tom job"))
         self.assertEqual(userList,None)

    def test_query_one(self):
        # 查询相同name数据，取一个   测试
        isSuccess = self.helper.addUser(Users("tome", "tom jobn"))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.addUser(Users("tome", "tom jobn2"))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.addUser(Users("tome", "tom jobn3"))
        self.assertTrue(isSuccess)
        userList = self.helper.query_one(Users("tome", "tom jobn4"))
        self.assertEqual(len(userList), 1)


    def test_revise_extra(self):
        isSuccess = self.helper.addUser(Users("tome", "tom jobn"))
        self.assertTrue(isSuccess)

        isSuccess=self.helper.update_user_extra_by_user_name(Users("tome", "tomUpdate"))

        self.assertTrue(isSuccess)
        userList = self.helper.query_all_with_user_name(Users("tome", "tom job"))
        self.assertEqual(len(userList), 1)


    def test_recise_name(self):
        isSuccess = self.helper.addUser(Users("tome", "tom jobn"))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.update_user_name_by_user_extra(Users("tomeUpdate", "tom jobn"))
        self.assertTrue(isSuccess)
        userList = self.helper.query_all_with_user_name(Users("tomeUpdate", "tom job"))
        self.assertEqual(len(userList),1)















if __name__ == '__main__':
    unittest.main()


