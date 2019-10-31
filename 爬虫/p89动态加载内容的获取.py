import re
import json
import requests
from fake_useragent import UserAgent
def printjson(data):
    json_str=json.dump(data,indent=4,ensure_ascii=False)
    print(json_str)

#获取网页数据
def get_data(json_url):
    ua=UserAgent()
    header={'User-Agent':ua.random}
    data=requests.get(json_url,headers=header)

    re_data=re.findall('pcMiaoShaAreaList\(({.*})\)',data.text)[0]
    json_data=json.loads(re_data)

    miaoshaList=json_data['miaoShaList']
    print(miaoshaList)

if __name__=='__main__':
    jsurl='https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList&_=1572487431120'
    get_data(jsurl)