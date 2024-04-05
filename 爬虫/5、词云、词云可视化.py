from PIL import Image
import numpy as np
import jieba
from wordcloud import WordCloud



#词云切分文本
def trans_ch(txt):
  words = jieba.lcut(txt)
  newtxt = ''.join(words)
  return newtxt

#词云可视化：
f = open('D:\pythonProject\STUDY\YUYAN\实训，爬虫\split_word.txt','r',encoding = 'utf-8')     #文本文件名
txt = f.read()
f.close
#清洗数据
txt = trans_ch(txt)
mask = np.array(Image.open("D:\pythonProject\STUDY\YUYAN\实训，爬虫\Alice.png"))               #你的背景图片
wordcloud = WordCloud(background_color="white",\
                      width = 800,\
                      height = 600,\
                      max_words = 200,\
                      max_font_size = 80,\
                      mask = mask,\
                      contour_width = 4,\
                      contour_color = 'steelblue',\
                        font_path =  "D:\pythonProject\STUDY\YUYAN\实训，爬虫\AaLaoJieZhaoPaiTi-2.ttf"
                      ).generate(txt)
wordcloud.to_file('Alice_词云图.png')

