import jieba
import jieba.posseg as psg
#创建词性标注表，并加载词性标注表到list[]列表中，返回list列表的值

def Part_of_speech_annotation (path):
    list = []
    dd = open("D:\pythonProject\STUDY\YUYAN\实训，爬虫\Part_of_speech_annotation_list.txt", 'w', encoding='utf8')
    seg = psg.cut(str(path))
    for key, value in seg:
        print('%s %s' % (key, value))
        dd.write(key + value+ "\n")
    print('+' * 10)
    ee = open("D:\pythonProject\STUDY\YUYAN\实训，爬虫\Part_of_speech_annotation_list.txt", 'r',encoding='utf8')
    list.append(ee)
    # print(ee.read())
    ff = ee.read()
    # print(ff)

    return ff


#统计名词
jieba.del_word(stopword_path)
words = psg.cut(path)
stopword = open("D:\pythonProject\STUDY\YUYAN\实训，爬虫\stopwords-master\StopWords.txt",'r',encoding='utf8').read()
stopword = str(stopword)
nouns = []
# verbs = []

for word, flag in words:
    if flag.startswith('n')and len(word)>1:
        nouns.append(word)
    # if flag.startswith('v'):
    #     verbs.append(word)
print(nouns)

# # 统计词频
dic = {}
word_num = 10
for word in nouns:
    dic[word] = dic.get(word, 0) + 1
freq_word = sorted(dic.items(), key=lambda x: x[1],
                   reverse=True)[: word_num]
print(freq_word)
