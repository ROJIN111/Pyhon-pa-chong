# -*- coding: utf-8 -*-
from snownlp import SnowNLP

from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

source = open("D:\pythonProject\STUDY\YUYAN\实训，爬虫\Part_of_speech_annotation_list.txt", "r", encoding='utf-8')
line = source.readlines()

c = 0
d = 0
e = 0
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

for b in sentimentslist:
    if b > 0.7 :
        c += 1
    if 0.7<b>0.4:
        d += 1
    else:
        e += 1
if c+d<e :
    print("电影综合评价为：差评满满")
else:
    print("电影综合评价为：好评如潮")
plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel(str("满意度"))
plt.ylabel(str("人数"))
plt.title(str("满意度可视图"))
plt.show()
print("好评率：",str(c))
print("中评率：",str(d))
print("差评率：",str(e))