#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------#
#     »Search Google«               #    
#     programmer : Mohammad Lakzaee #
#     Version    : 0.2              #
#-----------------------------------#
from bs4 import BeautifulSoup
import requests

search = "اموزش پایتون".replace(" ", "+") #چیزی که میخواد جستجو کنید   
limit_search = 10 # مقدار دریافت خروجی
usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}
lang = "en" # set Language [fa, en, ...]

req = requests.get(url=f"https://www.google.com/search?q={search}&num={limit_search+1}&hl={lang}", headers=usr_agent, proxies=None)
html = BeautifulSoup(req.text, 'html.parser')
items = html.find_all('div', attrs={'class': 'g'})
links = []
titles = []
for item in items:
    # print(item)
    if item.find('span').text is not None:
        title = item.find('span').text
    if item.find('a', href=True)['href'] is not None: 
        link = item.find('a', href=True)['href']
    links.append(link)
    titles.append(title)
    

for i in range(0, len(links)):
    print(f"Url : {links[i]}\nTitle : {titles[i]}\n-----------------------------\n")





