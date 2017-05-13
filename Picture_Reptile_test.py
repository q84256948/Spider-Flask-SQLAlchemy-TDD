# coding=utf-8
__author__ = 'YU'
from Picture_Reptile import Picture_Reptile

import os
import unittest  # 包含单元测试模块
import string
import re
import urllib2
import sys


from bs4 import BeautifulSoup
from lxml import html

reload(sys)
sys.setdefaultencoding('utf8')


class rictureReptileTests(unittest.TestCase):

    def setUp(self):  # 单元测试环境配置
        self.spider= Picture_Reptile("test.db","http://www.meizitu.com/a/5366.html")

    def tearDown(self):  # 单元测试环境清除
        self.spider =None


    def testInit(self):
        self.assertIsNotNone(self.spider)
        self.assertIsNotNone(self.spider.cur_url)
        self.assertEqual(self.spider.cur_url,"http://www.meizitu.com/a/5366.html")



    def testGet_page_string(self):
        self.cur_url="http://www.meizitu.com/a/5366.html"
        self.assertIsNotNone(self.spider.get_page(self.cur_url))
        imgList = self.spider.getImgListFromURL()
        self.assertIsNotNone(imgList)
        titles_imgList = len(imgList)
        self.assertGreater(titles_imgList, 0)
        img = self.spider.findImgSrcAndSaveImg(imgList)
        self.assertEqual(img, True)
        model=self.spider.saveImgContent()
        self.assertEqual(model, True)

















if __name__ == "__main__":
    unittest.main()







