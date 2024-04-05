from wordcloud import WordCloud
import jieba
from PIL import Image
import jieba.posseg as pseg
from snownlp import SnowNLP
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用于读取图片

path = open("D:\pythonProject\STUDY\YUYAN\爬虫\sentiment_comments.txt").read()
stopword_path= "D:\pythonProject\STUDY\YUYAN\爬虫\stopwords-master\StopWords.txt"
split_word = open("D:\pythonProject\STUDY\YUYAN\爬虫\split_word.txt",'r',encoding="utf8").read()

#jieba库加载停用词切分文本，分析文本词性，统计10个最多的名词
def cut_stopword_pseg_tongji(path):
    with open('D:\pythonProject\STUDY\YUYAN\爬虫\stopwords-master\StopWords.txt',
              encoding='utf-8') as f:  # 可根据需要打开停用词库，然后加上不想显示的词语
        con = f.readlines()
        stop_words = set()  # 集合可以去重
        for i in con:
            i = i.replace("\n", "")  # 去掉读取每一行数据的\n
            stop_words.add(i)
    words = pseg.cut(path)       #pesg:jieba.posseg:即为jieba库的接口，输出的数据为列表（list）类型，且同时输出词性
    g = open("D:\pythonProject\STUDY\YUYAN\爬虫\Parts_of_speech_annotation_list.txt",'w',encoding='utf8')
    g.write(str(words))

    nouns = []
    # verbs = []
    a = []
    for word, flag in words:
        if flag.startswith('n') and len(word) > 1:  # 谱匹配名词，且为长度不小于1的名词
            nouns.append(word)
        # if flag.startswith('v'):
        #     verbs.append(word)
    for i in nouns:
        if i not in stop_words:  # 加载停用词
            a.append(i)

    print("pseg.cut词性分析切分且过滤完名词后处理后：   "+str(nouns))
    print("停用词处理后：    "+str(a))
    # # 统计词频
    dic = {}
    word_num = 10
    for word in a:
        dic[word] = dic.get(word, 0) + 1
    freq_word = sorted(dic.items(), key=lambda x: x[1],
                       reverse=True)[: word_num]

    print("dic字典内容为：  "+str(dic))
    print("词频最大的10个名词：  "+str(freq_word))

    a = str(freq_word)

    def clean(i):
        pattern = re.compile(u'[^\u4e00-\u9fa5]'+'')  # 中文的范围为\u4e00-\u9fa5
        i = re.sub(r'\d+', '', i)# 将其中所有非中文字符替换
        c = re.sub(r'[^\w\s]','',i)
        return c
    f = clean(a)
    b = open("D:\pythonProject\STUDY\YUYAN\爬虫\split_word.txt",'w',encoding='utf8')
    for i in f :
        b.write(i)

    print(f)

    # return ''.join(f)


# 词云可视化
def ciyun():
    # 词云切分文本
    def trans_ch(txt: object) -> object:
        words = jieba.lcut(txt)
        newtxt = ''.join(words)
        return newtxt

    # 词云可视化：
    f = open('D:\pythonProject\STUDY\YUYAN\爬虫\split_word.txt', 'r', encoding='utf-8')  # 文本文件名
    txt = f.read()
    f.close
    # 清洗数据
    txt = trans_ch(txt)
    mask = np.array(Image.open("D:\pythonProject\STUDY\YUYAN\爬虫\Alice.png"))  # 你的背景图片
    wordcloud = WordCloud(background_color="white",
                          width=800,
                          height=600,
                          max_words=200,
                          max_font_size=80,
                          mask=mask,
                          contour_width=4,
                          contour_color='steelblue',
                          font_path="D:\pythonProject\STUDY\YUYAN\爬虫\AaLaoJieZhaoPaiTi-2.ttf"
                          ).generate(txt)
    wordcloud.to_file('Alice_词云图.png')
    # img1 = mpimg.imread('Alice_词云图.png')
    # plt.imshow(img1)


# 情感分析可视化
def commen_feel():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    #请用创建词性标注表代码生成文件再使用
    source = open("D:\pythonProject\STUDY\YUYAN\爬虫\Part_of_speech_annotation_list.txt", "r", encoding='utf-8')
    line = source.readlines()
    z = 0
    c = 0
    e = 0
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)#使用snownlp库来对切分切经过词性标注的评论进行情感分析
        # print(s.sentiments)#sentimes为情感分析模块
        sentimentslist.append(s.sentiments)

    for b in sentimentslist:#统计好评数，>0.7:好评，<0.4:差评，其他：中评
        if b > 0.5:
            c += 1
            e += 1

        else:
            z +=1
            e += 1
    q=c/e

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel(str("满意度"))
    plt.ylabel(str("人数"))
    plt.title(str("满意度可视图"))
    plt.show()

    print("好评条：", str(c))
    print("差评条：", str(z))
    print("评论数：", str(e))
    print("好评率：", str(q))
    if q<0.5:
        print("电影综合评价为：差评满满")
    else:
        print("电影综合评价为：好评如潮")


cut_stopword_pseg_tongji(path)

ciyun()
commen_feel()
