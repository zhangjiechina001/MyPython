import requests
import os
from bs4 import BeautifulSoup
with open("douban.txt", "w",encoding='utf-8') as f:
    url = 'https://www.douban.com/'
    headers={ "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    data = requests.get(url,headers=headers)
    print(BeautifulSoup(data.text,'html.parser'))
    f.write(data.text)
