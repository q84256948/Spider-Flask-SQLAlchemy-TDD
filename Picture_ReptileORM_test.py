# coding=utf-8
from struct import pack

__author__ = 'YU'
import os
import unittest
from Picture_ReptileORM import Picture_reptile,Picture_reptileORMHelper

TEST_DB = 'test.db'


class PictureORMHelperTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a blank temp database before each test"""

        self.helper = Picture_reptileORMHelper("Picture_reptile.db")
        self.helper.drop_db()
        self.helper.create_db()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        self.helper.drop_db()

    def test_add(self):
        # 插入测试
        isSuccess = self.helper.addPicture(Picture_reptile("tome", pack('H', 365),None))
        isSuccess = self.helper.addPicture(Picture_reptile("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.addPicture(Picture_reptile("tome", pack('H', 365),None))
        self.assertTrue(isSuccess)




    def test_query_all(self):
        # 查询所有相同name数据测试
        isSuccess = self.helper.addPicture(Picture_reptile("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        userList = self.helper.query_all_with_Picture_name_password(Picture_reptile("tome" ,pack('H', 365),None))
        # print userList
        self.assertGreater(len(userList),0)

    def test_query(self):
        isSuccess = self.helper.addPicture(Picture_reptile("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        userList = self.helper.query__Picture()
        self.assertGreater(len(userList), 0)


if __name__ == '__main__':
    unittest.main()
