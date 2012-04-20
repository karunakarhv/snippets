#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import datetime
import re
import sys
from pyquery import PyQuery as pq

def date_range(begin_date, end_date):
    for n in range((end_date - begin_date).days):
        yield begin_date + datetime.timedelta(n)


class Post(object):
    
    def __init__(self, url, beg_time, end_time):
        self.url = url
        self.beg_time = beg_time
        self.end_time = end_time
        self.posts = {}

    def get_posts(self):
        for single_date in date_range(self.beg_time, self.end_time):
            try:
                print single_date
                page = urllib2.urlopen(self.url + single_date.strftime("/%Y/%m/%d/"), None, 1)
                content = page.read()
                page.close()
                d = pq(content)
                href = d(".postTitle").find('h4').find('a').attr('href')
                title = d(".postTitle").find('h4').find('a').attr('title')
                if href and title:
                    self.posts[title] = href 
                    print title, href
            except IOError:
                pass

    def prt_posts(self):
        for k, v in self.posts:
            print k, v

def main(argv=None):
    p = Post("http://blog.youxu.info/",
             datetime.date(2008, 1, 1), 
             datetime.date(2012, 4, 20)) 
    p.get_posts()
    p.prt_posts()
    return 0

if __name__ == "__main__":
    sys.exit(main())