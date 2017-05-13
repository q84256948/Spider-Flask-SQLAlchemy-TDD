# coding=utf-8

__author__ = 'YU'

from ArticleORM import Article
from newsPicker import NewsPicker

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


class reptileTests(unittest.TestCase):

    def setUp(self):  # 单元测试环境配置
        self.spider= NewsPicker()

    def tearDown(self):  # 单元测试环境清除
        self.spider =None


    def testInit(self):
        self.assertIsNotNone(self.spider)
        self.assertIsNotNone(self.spider.cur_url)
        self.assertEqual(self.spider.cur_url,"http://blog.sina.com.cn/")
        self.assertEqual(self.spider.datas,[])

    def testGet_page_string(self):
        self.assertIsNotNone(self.spider.get_page_string())

    def testFind_title(self):
        html_string=self.spider.get_page_string()
        titles=self.spider.find_title(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.format_data_with_top_5(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertLess(titles_length,100)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)

    def testExportData(self):
        html_string=self.spider.get_page_string()
        titles=self.spider.find_title(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.format_data_with_top_5(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertLess(titles_length,100)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)
        for item in model:
            isSuccess=self.spider.exportData(Article(unicode( item), unicode( item)))
            self.assertTrue(isSuccess)



















if __name__ == "__main__":
    unittest.main()







