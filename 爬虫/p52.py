import requests

urls=["http://www.baidu.com","http://news.baidu.com","http://datahor.com"]

def get_data(url):
    try:
        data=requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("错误请求，url:",url)
        print("错误详情：",e)
        data=None
    return data

if __name__=='__main__':
    for url in urls:
        data=get_data(url)
        print(data)