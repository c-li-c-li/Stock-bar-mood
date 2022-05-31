import requests
import pandas as pd
import json
import time
import csv
from bs4 import BeautifulSoup
import os
from urllib import request

header={'Content-Type':'text/html;charset=utf-8','User-Agent':'Mozilla/5.0 (Window NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
url_1="http://guba.eastmoney.com/list,zssh000001,99_"
url_2=".html"

for ii in range (2):
    url=url_1+str(ii+1)+url_2
    html=requests.get(url,headers=header)
    soup=BeautifulSoup(html.content,'lxml')
    
    read_counts=soup.find_all('span',attrs={'class':'l1 a1'})
    
    comment_counts=soup.find_all('span',attrs={'class':'l2 a2'})
    
    title_counts=soup.find_all('span',attrs={'class':'l3 a3'})
    
    author_counts=soup.find_all('span',attrs={'class':'l4 a4'})
    
    time_counts=soup.find_all('span',attrs={'class':'l5 a5'})
    
    for i in range(len(read_counts)-1):#注意源代码中的第一个并非所需数据
        data1=[(read_counts[i+1].string,
                comment_counts[i+1].string,
                title_counts[i+1].find(name='a').get('title'),
                author_counts[i+1].find(name='font').string,
                time_counts[i+1].string)]
        data2=pd.DataFrame(data1)
        data2.to_csv('guba926.csv',header=False,index=False,mode='a+')
    print('page '+str(ii+1)+' has done')
    time.sleep(1)
        
        
        
        
        
        
        
        