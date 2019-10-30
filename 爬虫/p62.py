import requests
import chardet
data=requests.get('http://www.baidu.com')
charset=chardet.detect(data.content)
print(charset)
data.encoding='utf-8'
print(data.text)