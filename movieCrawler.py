#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的豆瓣图书前250爬虫
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

from MovieORM import Movie,MovieORMHelper

reload(sys)
sys.setdefaultencoding('utf8')


class MovieCrawler(object):
    """类的简要说明
    本类主要用于抓取豆瓣电影排行的名称
    Attributes:
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的图书名称

    """

    def __init__(self):
        self.cur_url = "https://movie.douban.com/chart"
        self.datas = []
        self.db = MovieORMHelper("flaskr.db")
        self.db.create_db()

        print "豆瓣电影爬虫准备就绪, 准备爬取数据..."

    def open_Film_Page(self):


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

    def select_Film_Content(self, html_string):
        """
        通过返回的整个网页HTML, 正则匹配前250的书籍名称

        Args:
            my_page: 传入页面的HTML文本用于正则匹配
        """

        tree = html.fromstring(html_string)
        content_items = tree.xpath('//span[@style="font-size:12px;"]/text()')
        return content_items

    def form_Film_Content(self, content_items):
        # _top_num: 用于记录当前的top号码
        temp_data = []
        top_num = 1
        for index, item in enumerate(content_items):
            isFive = top_num
            if (item.find("&nbsp") == -1 and isFive):
                temp_data.append("第" + str(top_num) + "名 " + item)
                top_num += 1
        self.datas.extend(temp_data)
        return self.datas

    def start_Film_spider(self):
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        my_page = self.open_Film_Page()
        content_items=self.select_Film_Content(my_page)
        self.form_Film_Content(content_items)

    def exportData(self, movie):
            return self.db.addMovie(movie)





def main():
    print """
        ###############################
            一个简单的豆瓣电影爬虫
            Author: eric.guo email:gyc567@126.com
            Date: 2016-08-27
        ###############################
    """
    my_spider = MovieCrawler()
    my_spider.start_Film_spider()
    for item in my_spider.datas:
        item_unicode=unicode(item)
        my_spider.exportData(Movie(item_unicode , item_unicode ))
        print item



    print "spider is  done..."





if __name__ == '__main__':
    main()
