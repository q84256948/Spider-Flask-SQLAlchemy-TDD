#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的图片爬虫
Author: eric.guo email:gyc567@126.com
Date: 2016-08-27
Language: Python2.7.10

"""
import base64

import string
import re
import urllib2
import sys
import urllib2
from bs4 import BeautifulSoup
from PictureORM import Picture,PictureORMHelper
import socket

reload(sys)
sys.setdefaultencoding('utf8')


class ImgScrapy(object):
    """类的简要说明
    本类主要用于抓取豆瓣图书Top前250的书籍的名称

    Attributes:
        page: 用于表示当前所处的抓取页面
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的图书名称
        _top_num: 用于记录当前的top号码
    """

    def __init__(self,db_name,url):

        self.cur_url=url
        self.db = PictureORMHelper(db_name)
        self.db.drop_db()
        self.db.create_db()

        print "图片爬虫准备就绪, 准备爬取数据..."

    def get_page(self,url ):
        req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        #定义请求豹纹头。伪造成火狐浏览器
        req_timeout = 20
        #请求等等时间
        try:
           req = urllib2.Request( url,None,req_header)
           page = urllib2.urlopen(req,None,req_timeout)

        except urllib2.URLError as e:
             print e.message
        except socket.timeout as e:
             self.get_page( url)
        return page

    def page_loop(self):

        # print url
        imgList = self.getImgListFromURL()

        self.findImgSrcAndSaveImg(imgList)

    def getImgListFromURL(self):
        page = self.get_page(self.cur_url)
        soup = BeautifulSoup(page)

        img = soup.find_all(['img'])
        return img



    def findImgSrcAndSaveImg(self,  imgList):
        isSuccess=False
        for myimg in imgList:
            self.link = myimg.get('src')
            self.name = myimg.get('alt')
            # print self.link
            #  content2 = urllib2.urlopen(link).read()
            # 可以添加筛选Link的代码


            self.saveImgContent()
            isSuccess=True
        return isSuccess

    def saveImgContent(self):
        isSuccess = False
        name=str(self.name).decode('utf-8')
        imgContent = self.get_page(self.link).read()
        picName = 'static/pictures/' + name + '.jpg'
        fp = open(picName, 'wb')
        fp.write(imgContent)
        fp.close()
        img_head=u"<img src="
        img_tail=u"/>"
        img_url=str(img_head+picName+img_tail).decode('utf-8')
        pic=Picture(name, imgContent,img_url)
        isSuccess = self.db.addPicture(pic)

        return isSuccess


    def start_spider(self):
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        self.page_loop()


def main():
    print """
        ###############################
            一个简单的图片爬虫
            Author: eric.guo email:gyc567@126.com
            Date: 2016-08-27
        ###############################
    """
    my_spider = ImgScrapy("flaskr.db","http://www.meizitu.com/a/5516.html")
    my_spider.start_spider()
    print "spider is  done..."


if __name__ == '__main__':
    main()
