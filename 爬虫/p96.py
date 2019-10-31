import re
import requests
import pandas as pd
from fake_useragent import UserAgent

url='https://www.hao123.com/'
ua=UserAgent()
headers={'User-Agent':ua.random}

resp=requests.get(url,headers)
data=resp.text
# href="https://pan.baidu.com/">
#<a class="hao123logourl" href="http://www.hao123.com/redian/sheshouyef.htm" title="上网从hao123开始" hidefocus="true" style="width:120px;height:33px;"><img src="https://gss0.bdstatic.com/5bVWsj_p_tVS5dKfpU_Y_D3/res/r/image/2017-09-27/297f5edb1e984613083a2d3cc0c5bb36.png" width="120" height="33"></a>
urls=re.findall(r'href="(http.*?)"',data)
print(urls)
df=pd.DataFrame()
df['url']=urls[:1000]
df.to_csv('hao123Urls.csv',index=None)