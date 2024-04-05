#-"-coding:utf-8-"-
import xlwt
import requests
from bs4 import BeautifulSoup
from lxml import etree
# 爬取网页内容
import requests
import re
import os
from tqdm import tqdm


#通常只针对文字，而符号、数字等是没有意义的，如果一项项的分开去除，那样就会浪费时间，所以想只留下汉子时，
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':  # 判断一个uchar是否是汉字
        return True
    else:
        return False

def allcontents(contents):
    content = ''
    for i in contents:
        if is_chinese(i):
            content = content + i
    print('\n' + content)
    return content




# 输入网页url
for p in range(0,400,20):
    url = 'https://movie.douban.com/subject/35875180/reviews?start=' + str(p)
    # .设置headers目的
    # 在请求网页爬取的时候输出的text信息中会出现抱歉，无法访问等字眼，这就是网页设置了禁止爬取。
    # headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept - Encoding': "gzip, deflate",
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    # 输入要爬取的网站
    resource = requests.get(url, headers=headers)
    resource.encoding = "utf-8"
    r = resource
    text = resource.content.decode("utf-8", "ignore")
    text = r.text
    tree = etree.HTML(text)
    items = tree.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]')
    # aa = []
    # w = 0
    comments_count = 0
    for item in items:
        for i in range(1, 20, 1):
            if i <= 21:
                # name = item.xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div[" + str(i) + "]/div/header/a[2]/text()")[0]
                # clear_character(name)

                # Raca = item.xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div[" + str(i) + "]/div/header/span[1]")

                comments = item.xpath(
                    "/html/body/div[3]/div[1]/div/div[1]/div[1]/div[" + str(i) + "]/div/div/div[1]/div/text()")
                comments = str(comments)

                b=allcontents(comments)

                # f = open("sentiment_comments.txt", "r")
                # lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
                # for line in lines:
                #     print (line)
                # # -*-coding:utf8-*-# encoding:utf-8
                # name_list = b
                # for i in tqdm(name_list):
                #     f = open('D:/project/tm_caption/file_names.txt', 'a')
                #     f.write(str(i) + '\n')
                #     f.close()
                # sp = open("D:\pythonProject\STUDY\YUYAN\爬虫\sentiment_comments.txt", "a", encoding='utf8')
                # sp.writelines(b)
                with open('/YUYAN/爬虫\sentiment_comments.txt', 'a') as f:
                    f.write(b+'\n')





            if i > 21:
                print('出错')

print("输出页数{}".format(i))
print('完成')

            # aa.append(name)
            # aa.append(clear_character(comments))
            # Name = item.xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div["+str(i)+"]/div/header/span[1]")
            # ent_text = etree.tostring(Name[0], method='text', encoding='utf-8')
            # print(ent_text.decode())

            # soup = BeautifulSoup('https://movie.douban.com/subject/35875180/reviews?start=', 'html.parser')
            # s1 = soup.find('span', attrs={"class": "red"})  # 查找span class为red的字符串
            # s2 = soup.find_all("span")  # 查找所有的span
            # result = [span.get_text() for span in s2]
            # print(result)  # ['item1', 'item2']
            # Note = open('影评.txt', mode='w')
            # Note.writelines(n)  # \n 换行符




# def clear_character(r):
#     pattern = re.compile("['[\[\]\s+\.\!\/_,$%^*(+\"\'?:&@#;<>=-]+|[+\
#           ——！？~@#￥%……&*（）」「’]+|[《》 ，。；﹔、：\- ★ 【 】 － 😂 “ ” 🙃 😅 •]+|[a-zA-Z]+|[0-9]+', '']")  # 只保留中英文、数字和符号，去掉其他东西
#     # 若只保留中英文和数字，则替换为[^\u4e00-\u9fa5^a-z^A-Z^0-9]
#     line = re.sub(pattern, '',r )  # 把文本中匹配到的字符替换成空字符
#     new_sentence = ''.join(line.split())  # 去除空白
#     print('',new_sentence)
#     return pattern ,line,new_sentence



#
#
# #匹配数字
# def find_chinese(text):
#     pattern=re.compile(r'[\u4e00-\u9fa5]')
#     chinese_txt=re.sub(pattern,'',text)
#     return chinese_txt








# def delelem(data):
#     """
#     删除多余的标点符号   出现的无用空格   不出现中文字符的数据行
#     :param data: list
#     :return: list
#     """
#     res_del = []
#
#     for i in data:
#         # 使用空字符替换掉间隔符
#         a = re.sub(r'\s', '', i)
#
#         # 使用精准匹配，匹配连续出现的符号;并用空字符替换他
#         b = re.sub(r'\W{2,}', '', a)
#
#         # 使用空字符替换空格
#         c = re.sub(r' ', '', b)
#
#         # 删除没有中文的数据行
#         if len(re.findall(r"[\u4e00-\u9fa5]", c)) >= 10:
#             res_del.append(c)
#
#     return res_del
