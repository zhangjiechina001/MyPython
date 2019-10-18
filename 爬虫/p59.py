from fake_useragent import UserAgent
import requests
import re

ua=UserAgent()
head={'User_Agent':ua.random}
html=requests.get('https://www.baidu.com',head)
html.encoding='utf-8'
txt=html.text
# print(txt)
titles=re.findall(r'<a href="(http://.*?.com)" name="tj_tr.*?" class="mnav">(\w{2})</a>',txt)
print(titles)

# <a href='(http://.*?.com)' name='tj_tr.*?' class='mnav'>(\w{2})</a>  <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a>