#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的新浪网新闻头条爬虫
Author: eric.guo email:gyc567@126.com
Date: 2016-08-27
Language: Python2.7.10

"""
import string
import re
import urllib2
import sys
import os

from bs4 import BeautifulSoup
from lxml import html

from ArticleORM import ArticleORMHelper, Article

reload(sys)
sys.setdefaultencoding('utf8')


class NewsPicker(object):
    """类的简要说明
    本类主要用于抓取新浪网新闻头条的标题

    Attributes:
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的图书名称
    """

    def __init__(self):           #初始化配置
        self.cur_url = "http://blog.sina.com.cn/"
        self.datas = []
        self.db=ArticleORMHelper("flaskr.db")
        self.db.create_db()

        print "新浪新闻爬虫准备就绪, 准备爬取数据..."




    def get_page_string(self):
        """
        Returns:
            返回抓取到整个页面的HTML(unicode编码)
        Raises:
            URLError:url引发的异常
        """
        try:
            html_string = urllib2.urlopen(self.cur_url).read().decode("utf-8")
            # print "page content-->" + html_string
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return html_string




    def find_title(self, html_string):
        """
        通过返回的整个网页HTML, 正则匹配新闻标题名称

        Args:
            html_string: 传入页面的HTML文本用于正则匹配
        """
        tree = html.fromstring(html_string)
        content_items = tree.xpath('//div[@class="p01_l05_items"]/h3/a/text()')
        return content_items




    def format_data_with_top_5(self, content_items):
        # _top_num: 用于记录当前的top号码
        temp_data = []
        top_num = 1
        for index, item in enumerate(content_items):

            if (item.find("&nbsp") == -1 and top_num<=10):
                temp_data.append("第" + str(top_num) + "名 " + item)
                top_num += 1
        self.datas.extend(temp_data)
        return self.datas




    def start_spider(self):
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        my_page = self.get_page_string()
        content_items=self.find_title(my_page)
        self.format_data_with_top_5(content_items)

    def exportData(self,article):
      return self.db.addArticle(article)

def main():
    print """
        ###############################
            一个简单的新浪新闻爬虫
            Author: eric.guo email:gyc567@126.com
            Date: 2016-08-27
        ###############################
    """
    my_spider = NewsPicker()
    my_spider.start_spider()
    for item in my_spider.datas:      #迭代结果

        my_spider.exportData(Article(item,item))
        print item
        print my_spider




    print "spider is  done..."






if __name__ == '__main__':
    main()
