import os
import jieba


#创建停用词表

# 输入你要读取的目录
path = '.\stopwords-master'
files = os.listdir(path)
print(files)
stopwords = []
for file in files:
    if file[-3:] == 'txt':  # 也可以是md,xsl等
        # 逐行读取，然后再数组拼接；这里不能用append，append会将数组当成一个对象接在stopwords之后：[1,2,3,[1,2,3]]
        stopwords += ([line.strip() for line in open(path + '\\' + file, encoding='UTF-8').readlines()])
# 去重
stopwords = list(set(stopwords))
print(len(stopwords))
# 保存在Stopwords.txt
with open(path + '\\' + 'StopWords.txt', 'w', encoding='utf-8') as f:
    for stopword in stopwords:
        f.write(stopword + "\n")





