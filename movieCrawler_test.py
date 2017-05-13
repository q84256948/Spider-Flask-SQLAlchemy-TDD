# coding=utf-8
__author__ = 'YU'

from MovieORM import Movie
from movieCrawler import MovieCrawler

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


class filmReptileTests(unittest.TestCase):

    def setUp(self):  # 单元测试环境配置
        self.spider= MovieCrawler()

    def tearDown(self):  # 单元测试环境清除
        self.spider =None


    def testInit(self):
        self.assertIsNotNone(self.spider)
        self.assertIsNotNone(self.spider.cur_url)
        self.assertEqual(self.spider.cur_url,"https://movie.douban.com/chart")
        self.assertEqual(self.spider.datas,[])

    def testGet_page_string(self):
        self.assertIsNotNone(self.spider.open_Film_Page())

    def testFind_title(self):
        html_string=self.spider.open_Film_Page()
        titles=self.spider.select_Film_Content(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.form_Film_Content(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertEqual(titles_length,10)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)


    def testExportData(self):
        html_string=self.spider.open_Film_Page()
        titles=self.spider.select_Film_Content(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.form_Film_Content(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertEqual(titles_length,10)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)
        for item in model:
            isSuccess=self.spider.exportData(Movie(unicode( item), unicode( item)))
            self.assertTrue(isSuccess)

















if __name__ == "__main__":
    unittest.main()







