import time
import requests
import concurrent
from concurrent import futures
import pandas as pd
import threading
from multiprocessing import Pool
#装饰器，打印函数的执行时间
def gettime(func):
    def warapper(*args,**kwargs):
        print('='*50)
        print(func.__name__,'Start...')
        starttime=time.time()
        func(*args)
        endtime=time.time()
        spendtime=endtime-starttime
        print(func.__name__,'End...')
        print('spend',spendtime,'s totally')
        print('='*50)
    return warapper

def get_urls_from_file(n):
    df=pd.read_csv('hao123Urls.csv')
    urls=list(df['url'][:n])
    return urls

def getdata(url,retries=3):
    headers={}
    try:
        html=requests.get(url,headers)
    except requests.exceptions.ConnectionError as e:
        html=None

    if(html!=None and html.status_code>=500 and html.status_code<600 and retries):
        retries-=1
        getdata(url,retries)
        data=html.text
    else:
        data=None
    return data

@gettime
def normal():
    for url in urls:
        getdata(url)

@gettime
def processPool(num=10):
    pool=Pool(num)
    result=pool.map(getdata,urls)
    pool.close()
    pool.join()
    return result

@gettime
def multithread(max_threads=10):
    def urls_process():
        while True:
            try:
                url=urls.pop()
            except IndexError:
                break
            data=getdata(url,retries=3)

    threads=[]

    while int(len(threads)<max_threads) and len(urls):
        thread=threading.Thread(target=urls_process)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

@gettime
def threadPool(num_of_max_works=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_max_works) as executor:
        executor.map(getdata,urls)


if __name__=='__main__':
    urls=get_urls_from_file(10)
    threadPool()
    normal()
    processPool()
    multithread()


