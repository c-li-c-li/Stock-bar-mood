
from wordcloud import WordCloud
import jieba
import numpy as np
import PIL.Image as Image
import pandas as pd

def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist

df=pd.read_csv('ddx927预警筛选.csv',encoding='gbk')
title_list=df['所属行业'].values.tolist()
# recommend_list=df['recommend'].values.tolist()
text=""
for jj in range (len(title_list)):
    # if recommend_list[jj]==1:
    text=text+chinese_jieba(title_list[jj])
# print(text)
mask_pic=np.array(Image.open("VCG211169937397.jpg"))
wordcloud=WordCloud(font_path="simsun.ttc",
                               mask=mask_pic,
                               background_color="white",
                               max_font_size=150,
                               max_words=200,
                               # stopwords={'的','我','大盘','吗','股票','需要',
                               #            '对','看','了','今天','是','大家','就',
                               #            '人','在','不','没有','也','你','说',
                               #            '明天','会','都有','有','要','市场',
                               #            '点','都','月','就是','后','这','对',
                               #            '我们','一个','股市','A股','日','炒股',
                               #            '什么','因为','这个','与','股'}
                               ).generate(text)
image=wordcloud.to_image()
wordcloud.to_file('ddx927预警筛选.png')
image.show()