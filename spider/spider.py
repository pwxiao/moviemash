# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 12:03:06 2020

@author: kun
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
ua = UserAgent()

headers = {
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/123.0.0.0',
'Host': 'movie.douban.com'
}


def get_movies():

    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout= 10)
        
        soup = BeautifulSoup(r.text, "lxml")
        # img_list = soup.find_all('div', class_='pic')
        # for each in img_list:
        #     img = each.a.img.get('src').strip()
        div_list = soup.find_all('div', class_='item')
        for each in div_list:
            img = each.find('div', class_='pic').a.img.get('src').strip()
            each = each.find('div', class_='info')
            title = each.find('div', class_='hd').a.span.text.strip()
            info = each.find('div', class_='bd').p.text.strip()
            info = info.replace("\n", " ").replace("\xa0", " ")
            info =  ' '.join(info.split())
            rating = each.find('span', class_='rating_num').text.strip()
            num_rating = each.find('div', class_='star').contents[7].text.strip()
            try:
                quote = each.find('span', class_='inq').text.strip()
            except:
                quote = ""
            
            movie_list.append([img,title, info, rating, num_rating, quote])
        df = pd.DataFrame(movie_list,columns=['海报图片','电影名称', '信息', '评分', '评价人数', '短评'],index=None)
      
        
        
        df.to_csv("spider/douban.csv")
    return movie_list
        
movies = get_movies()
print (movies)