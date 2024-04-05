from cgitb import text
import re

import nltk
import php
from wordcloud import WordCloud
import imageio
import jieba.posseg as psg
import jieba
import matplotlib.pyplot as plt
from matplotlib.font_manager import *
from imageio import imread
from PIL import Image
import numpy as np

from snownlp import SnowNLP
import codecs
import os
import jieba.posseg as pseg
####试验版，最后请看最终版

path = open("/YUYAN/爬虫\sentiment_comments.txt").read()
stopword_path= "/YUYAN/爬虫\stopwords-master\StopWords.txt"
split_word = open("/YUYAN/爬虫\split_word.txt", 'r', encoding="utf8").read()


#jieba分词
def cut_words(path):
    cut_word = jieba.cut (path,cut_all=True)
    aa = []
    for i in cut_word:
        aa.append(i)
        # print(aa)
    aa.append(i)
    # print(aa)

    return aa

with open('/YUYAN/爬虫\stopwords-master\StopWords.txt', encoding='utf-8') as f: # 可根据需要打开停用词库，然后加上不想显示的词语
    con = f.readlines()
    stop_words = set() # 集合可以去重
    for i in con:
        i = i.replace("\n", "")   # 去掉读取每一行数据的\n
        stop_words.add(i)
# words = pseg.cut(path)
#
# nouns = []
# # verbs = []
# a = []
# for word, flag in words:
#     if flag.startswith('n')and len(word)>1:
#         nouns.append(word)
#     # if flag.startswith('v'):
#     #     verbs.append(word)
# for i in nouns:
#     if i not in stop_words:
#         a.append(i)
#
# print(nouns)
# print(a)
# # # 统计词频
# dic = {}
# word_num = 10
# for word in nouns:
#     dic[word] = dic.get(word, 0) + 1
# freq_word = sorted(dic.items(), key=lambda x: x[1],
#                    reverse=True)[: word_num]
# print(freq_word)
#
# #词云切分文本
# def trans_ch(txt):
#   words = jieba.lcut(txt)
#   newtxt = ''.join(words)
#   return newtxt
#
# #词云可视化：
# f = open('D:\pythonProject\STUDY\YUYAN\爬虫\split_word.txt','r',encoding = 'utf-8')     #文本文件名
# txt = f.read()
# f.close
# #清洗数据
# txt = trans_ch(txt)
# mask = np.array(Image.open("D:\pythonProject\STUDY\YUYAN\爬虫\Alice.png"))               #你的背景图片
# wordcloud = WordCloud(background_color="white",\
#                       width = 800,\
#                       height = 600,\
#                       max_words = 200,\
#                       max_font_size = 80,\
#                       mask = mask,\
#                       contour_width = 4,\
#                       contour_color = 'steelblue',\
#                         font_path =  "D:\pythonProject\STUDY\YUYAN\爬虫\AaLaoJieZhaoPaiTi-2.ttf"
#                       ).generate(txt)
# wordcloud.to_file('Alice_词云图.png')
# plt.show()
#



# #jieba分词
# def cut_words(path):
#     cut_word = jieba.cut (path,cut_all=True)
#     aa = []
#     for i in cut_word:
#         aa.append(i)
#         # print(aa)
#     aa.append(i)
#     # print(aa)
#
#     return aa





# # 加载停用词表过滤后，加载切分文本，返回result_list列表
# def split_words_list(path):
#     # 文本预处理 ：去除一些无用的字符只提取出中文出来
#     stop_words = []
#     a = set()
#     stop_words_test = open("D:\pythonProject\STUDY\YUYAN\爬虫\stopwords-master\StopWords.txt",'r',encoding="utf8").readlines()
#     stop_words_test = str(stop_words_test)
#     cut_word  = jieba.cut(path)
#
#     for i in stop_words_test:
#         i = i.replace("\n", "")  # 去掉读取每一行数据的\n
#         a.add(i)
#     stop_words.append(a)
#     # print(stop_words)
#     cut_word = cut_words(path)
#     result_list=[]
#         # 去除停用词并且去除单字
#     for word in cut_word:
#         if word not in stop_words and len(word)>1 :
#             result_list.append(word)
#
#     # print('处理结果：', '/'.join(result_list))
#     return ''.join(result_list)
#
#
#     # 统计词频
#     dic = {}
#     word_num = 10
#     for word in result_list:
#         dic[word] = dic.get(word, 0) + 1
#     freq_word = sorted(dic.items(), key=lambda x: x[1],
#                        reverse=True)[: word_num]
#     print(freq_word)
#     return result_list
#
#
# def Part_of_speech_annotation(path):
#     list = []
#     dd = open("D:\pythonProject\STUDY\YUYAN\爬虫\Part_of_speech_annotation_list.txt", 'w', encoding='utf8')
#     seg = psg.cut(str(path))
#     for key, value in seg:
#         print('%s %s' % (key, value))
#         dd.write(key + value + "\n")
#     print('+' * 10)
#     ee = open("D:\pythonProject\STUDY\YUYAN\爬虫\Part_of_speech_annotation_list.txt", 'r', encoding='utf8')
#     list.append(ee)
#     # print(ee.read())
#     ff = ee.read()
#     # print(ff)
#
#     return ff
#
#
#
#
#


# dic = {}
# word_num = 10
# for word in result_list:
#     dic[word] = dic.get(word, 0) + 1
# freq_word = sorted(dic.items(), key=lambda x: x[1],
#                    reverse=True)[: word_num]
# print(freq_word)
# return result_list

# jieba分词并过滤停用词和提取前十个名词
# split_words = []
# for lines in open(path, 'r', encoding='utf-8', errors='ignore'):
#     for w, t in pseg.cut(lines.strip()):  # 对每行文本使用jieba的分词功能进行分词处理，并返回分词结果以及词性标注
#         # 加载停用词
#         stop_words = []
#         path = 'merged_stopwords.txt'
#         for line in open(path, encoding='utf8'):
#             stop_words.append(line.strip())
#         if t.startswith('n') is False:  # 通过判断词性是否为名词（'n'开头的词性表示名词）来过滤非名词词语
#             continue
#         if not w in stop_words and len(
#                 w) > 1:  # 判断词语是否不在停用词列表中并且长度大于1，符合条件的名词将被添加到split_words列表中，并且将词语及其词性存储到字典sc_dict中。
#             # print(w, '/', t)
#             sc_dict[w] = t
#             split_words.append(w)
#
#















# #创建词性标注表，并加载词性标注表到list[]列表中，返回list列表的值
# def Part_of_speech_annotation (path):
#     list = []
#     dd = open("D:\pythonProject\STUDY\YUYAN\爬虫\Part_of_speech_annotation_list.txt", 'w', encoding='utf8')
#     seg = psg.cut(str(path))
#     for key, value in seg:
#         print('%s %s' % (key, value))
#         dd.write(key + value+ "\n")
#     print('+' * 10)
#     ee = open("D:\pythonProject\STUDY\YUYAN\爬虫\Part_of_speech_annotation_list.txt", 'r',encoding='utf8')
#     list.append(ee)
#     # print(ee.read())
#     ff = ee.read()
#     # print(ff)
#
#     return ff
#
#
#
# split_words_list(path)
#
# #词云切分文本
# def trans_ch(txt):
#   words = jieba.lcut(txt)
#   newtxt = ''.join(words)
#   return newtxt
#
# #词云可视化：
# f = open('D:\pythonProject\STUDY\YUYAN\爬虫\split_word.txt','r',encoding = 'utf-8')     #将你的文本文件名与此句的'maozedong.txt'替换
# txt = f.read()
# f.close
# txt = trans_ch(txt)
# mask = np.array(Image.open("D:\pythonProject\STUDY\YUYAN\爬虫\Alice.png"))               #将你的背景图片名与此句的"love.png"替换
# wordcloud = WordCloud(background_color="white",\
#                       width = 800,\
#                       height = 600,\
#                       max_words = 200,\
#                       max_font_size = 80,\
#                       mask = mask,\
#                       contour_width = 4,\
#                       contour_color = 'steelblue',\
#                         font_path =  "D:\pythonProject\STUDY\YUYAN\爬虫\AaLaoJieZhaoPaiTi-2.ttf"
#                       ).generate(txt)



