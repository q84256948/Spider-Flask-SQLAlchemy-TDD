#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的豆瓣音乐前250爬虫
Author: eric.guo email:gyc567@126.com
Date: 2016-08-27
Language: Python2.7.10

"""
import string
import re
import urllib2
import sys

from bs4 import BeautifulSoup
from lxml import html
from MusicORM import Music,MusicORMHelper

reload(sys)
sys.setdefaultencoding('utf8')


class MusicPicker(object):
    """类的简要说明
    本类主要用于抓取豆瓣图书Top前250的书籍的名称

    Attributes:
        page: 用于表示当前所处的抓取页面
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的图书名称
        _top_num: 用于记录当前的top号码
    """

    def __init__(self):
        self.cur_url = "https://music.douban.com/chart"
        self.datas = []
        self.db=MusicORMHelper("flaskr.db")
        self.db.create_db()

        print "豆瓣音乐爬虫准备就绪, 准备爬取数据..."




    def Acquire_music_open(self):
        """
        Returns:
            返回抓取到整个页面的HTML(unicode编码)
        Raises:
            URLError:url引发的异常
        """
        try:
            html_string = urllib2.urlopen(self.cur_url).read().decode("utf-8")

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return html_string


    def select_music_Content(self, html_string):
        """
        通过返回的整个网页HTML, 正则匹配前250的书籍名称
        Args:
            my_page: 传入页面的HTML文本用于正则匹配
        """
        tree = html.fromstring(html_string)
        content_items = tree.xpath('//a[@href="javascript:;"]/text()')
        return content_items


    def form_music_Content(self, content_items):
        top_num = 1
        temp_data = []
        for index, item in enumerate(content_items):
            if (item.find("&nbsp") == -1 and top_num<=10):
                temp_data.append("第" + str(top_num) + "名 " + item)
                top_num += 1
        self.datas.extend(temp_data)
        return  self.datas



    def start_music_spider(self):
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        my_page = self.Acquire_music_open()
        content_items = self.select_music_Content(my_page)
        self.form_music_Content(content_items)

    def exportData(self, music):
            return self.db.addmusic(music)



def main():
    print """
        ###############################
            一个简单的豆瓣音乐前250爬虫
            Author: eric.guo email:gyc567@126.com
            Date: 2016-08-27
        ###############################
    """
    my_spider = MusicPicker()
    my_spider.start_music_spider()

    for item in my_spider.datas:
        item_unicode = unicode(item)
        my_spider.exportData(Music(item_unicode,item_unicode))

        print item



    print "spider is  done..."





if __name__ == '__main__':
    main()
