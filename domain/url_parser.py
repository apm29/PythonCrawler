# coding=utf-8
import re

from bs4 import BeautifulSoup

"""
<a href="http://www.imooc.com/video/10689" class="continue" title="调度程序
7-2调度程序">继续</a>
"""


class UrlParser(object):
    def parse_content(self, html_content,page_url):
        bs = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        href = bs.find_all(name='a', href=re.compile(r"/video/\d+"))
        title = bs.find(name='em')
        # print href.__len__()
        url_list = set()
        for tag in href:
            url_list.add("http://www.imooc.com/" + tag['href'])
            pass
        return url_list, title.text+"\t"+page_url
