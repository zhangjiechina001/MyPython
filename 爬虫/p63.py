import re
import requests
from fake_useragent import UserAgent

ua=UserAgent()
heads={'User-Agent':ua.random}

html=requests.get('https://www.baidu.com/',headers=heads)
html.encoding='utf-8'
txt=html.text
# print(txt)
titles=re.findall(r'(<a href="http://.*?.com" name="tj_tr.*?" class="mnav">)(\w{2})</a>',txt)
print(titles)