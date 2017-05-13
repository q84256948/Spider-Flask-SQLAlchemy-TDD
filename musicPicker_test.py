# coding=utf-8
__author__ = 'YU'

from MusicORM import Music
from musicPicker import MusicPicker

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
        self.spider= MusicPicker()

    def tearDown(self):  # 单元测试环境清除
        self.spider =None


    def testInit(self):
        self.assertIsNotNone(self.spider)
        self.assertIsNotNone(self.spider.cur_url)
        self.assertEqual(self.spider.cur_url,"https://music.douban.com/chart")
        self.assertEqual(self.spider.datas,[])

    def testGet_page_string(self):
        self.assertIsNotNone(self.spider.Acquire_music_open())

    def testFind_title(self):
        html_string=self.spider.Acquire_music_open()
        titles=self.spider.select_music_Content(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.form_music_Content(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertEqual(titles_length,20)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)


    def testExportData(self):
        html_string=self.spider.Acquire_music_open()
        titles=self.spider.select_music_Content(html_string)
        self.assertIsNotNone(titles)
        titles_length=len(titles)
        model = self.spider.form_music_Content(titles)
        model_length=len(model)
        self.assertGreater(titles_length, 0)
        self.assertEqual(titles_length,20)
        self.assertIsNotNone(model)
        self.assertEqual(model_length, 10)
        for item in model:
            isSuccess=self.spider.exportData(Music(unicode( item), unicode( item)))
            self.assertTrue(isSuccess)



















if __name__ == "__main__":
    unittest.main()







