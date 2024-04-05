# 请求库
# 导入requests库
from cgitb import html
from html.parser import HTMLParser

from lxml.html import fromstring, tostring
import xlwt
import requests
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re
import os
import lxml
for i in range(0,100,20):
    url = 'https://movie.douban.com/subject/35875180/reviews?start={}' + str(i)

    # .设置headers目的
    # 在请求网页爬取的时候输出的text信息中会出现抱歉，无法访问等字眼，这就是网页设置了禁止爬取。
    # headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据
    # 输入网页url
    h2={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    # 输入要爬取的网站

    reso = requests.get(url, headers=h2)
    # r = resource.text
    tree = etree.HTML(reso.text)
    # 转为string
    tree1 = html.tostring(tree[0])
    # 编码'utf-8'
    tree2 = HTMLParser().unescape(tree1.decode('utf-8'))
    print(tree2)





# for u in range(1, 20, 1):
#     if u <= 20:
#         text = html.xpath(f"/html/body/div[3]/div[1]/div/div[1]/div[1]/div[{u}]/div/header/a[2]/text()")[0]
#         print(text)








# i=0
# a='https://movie.douban.com/'
# b='subject/35875180/reviews?start='
# for i in range (50):
#     i=0
#     if i<20:
#         #输入网页url
#         url = 'https://movie.douban.com/subject/35875180/reviews?start=0'
#         # .设置headers目的
#        # 在请求网页爬取的时候输出的text信息中会出现抱歉，无法访问等字眼，这就是网页设置了禁止爬取。
#         #headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据
#         headers = {
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#            'Accept - Encoding': 'gzip, deflate, br',
#            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#            'Connection': 'keep-alive',
#            'Host': 'movie.douban.com',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
#         # 输入要爬取的网站
#         r = requests.get('https://movie.douban.com/subject/35875180/', url, headers=headers, )
#         # with open('./day06{}北面.html'.format(page_name), 'w', encoding='utf-8') as fp:
#         # fp.write(respone.text)
#
#         # 查看响应对象的类型
#         print(type(r))
#         # 查看响应状态码
#         print(r.status_code)
#         # 查看响应内容的类型
#         print(type(r.text))
#         # 查看响应的内容
#         print(r.text)
#         # 查看cookies
#         print(r.cookies)
#         i+20;
#     if i>20:
#         continue
