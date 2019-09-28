import requests
from bs4 import BeautifulSoup

url="https://book.douban.com/latest"
heads={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
data=requests.get(url,headers=heads)
# print(data.text)
soup=BeautifulSoup(data.text,'lxml')
book_left=soup.find('ul',{'class':"cover-col-4 clearfix"})
book_left=book_left.findAll('li')
books=list(book_left)
print(books)