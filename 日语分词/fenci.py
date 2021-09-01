# 首先安装相关包，使用pip install mecab-python3 
# 安装日文词典 pip install unidic-lite

# encoding=utf-8#
import MeCab
import time
# 手动复制内容，存入txt，下面打开
with open('riwen.txt','r',encoding='utf-8') as f:
    text=f.read()
    
mecab_tagger = MeCab.Tagger("-Owakati") #该模式将分好得词用空格隔开，返回str
mecab_tagger.parse(text)
mecab_tagger.parse(text).split()[:-1] #[:-1]是为了把末尾的\n去掉
# print(mecab_tagger.parse(text))
seg_list=mecab_tagger.parse(text)
# print(seg_list)
seg_list=seg_list.split(' ') #将字符串按照空格隔开，划分为list
# print(seg_list)# type:str
# print(list(seg_list))

#词频统计，将词存入字典
tf={}
for seg in seg_list:
    if seg in tf:
        tf[seg]+=1
    else:
        tf[seg]=1
# print(len(tf))
# print(tf)


ci=list(tf.keys())
# print(ci)
#加载停用词字典：用于下面删除相关词语，可以手动在stopword.txt内加入你想删除的词语
with open(r'stopword.txt','r',encoding='utf-8') as ft:
    stopword=ft.read()
for seg in ci:
    if len(seg)<2 or seg in stopword or '一' in seg: #自己设置删除条件   tf[seg]<10 or len(seg)<2 or 
        tf.pop(seg)
# print(len(tf))
# print(tf)


# 按词频排序，并存入二维数组
data=sorted(tf.items(),key=lambda x:x[1],reverse=True)  # 按字典转化为list，使用sort函数排序，按照每一个元组的第二个元素排列。
# ci=list(tf.keys())
# num=list(tf.values())
# data=[]
# for i in range(len(tf)):
#     data.append((num[i],ci[i]))
# data.sort()
# data.reverse() # 反转，使字典按从高到低排序
# print(data)


# #将词频存入result.txt中
# f=open("result.txt",'w',encoding='utf-8')
# for i in range(len(data)):
#     f.write(data[i][1]+","+str(data[i][0])+"\r\n")
# f.close()


# 生成词云图，安装包使用pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 基础的词云功能 
# text=open('riwen.txt','r',encoding='utf-8').read()
# 设置字体：仿宋
font=r'c:\Windows\Fonts\simfang.ttf'
# wc=WordCloud(font_path=font).generate(text)#generate()功能为生成文本
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# # print(dir(WordCloud))

# 将list转化为字典 
wcdata={}
for d in data:
    wcdata[d[0]]=d[1]
# print(wcdata)
# wc2=WordCloud(font_path=font,background_color='white').generate_from_frequencies(wcdata)
# plt.imshow(wc2)
# plt.axis('off')
# plt.show()
# wc2.to_file('2.png')

import os
# print(os.getcwd())

from PIL import Image
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator

#生成形状词云图，导入相关图片即可,自己选择相关图片
mask=np.array(Image.open('picture\hai2.png'))

image_colors=ImageColorGenerator(mask)
wc1=WordCloud(font_path=font,background_color='white',mask=mask).generate_from_frequencies(wcdata)

# 使用时间戳命名文件
now= str(int(time.time()))
picture_name = 'product/'+now+'.jpg'
#plt.imshow(wc)
plt.imshow(wc1.recolor(color_func=image_colors))
plt.axis('off')
plt.show()
wc1.to_file(picture_name)