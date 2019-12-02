import os
import requests
import pandas as pd

def savepucs(img_urls,titles):
    for i in range(len(img_urls)):
        imgUrl=img_urls[i]
        title=titles[i]
        img_data=requests.get(url=imgUrl).content
        with open(str(title)+'.jpg','wb') as f:
            f.write(img_data)

if __name__=='__main':
    if 'xlsxdata' not in os.listdir():
        os.mkdir('xlsxdata')
    os.chdir('xlsxdata')

    book_data=pd.read_csv('result.csv')
    img_urls=book_data['img_urls']
    titles=book_data['titles']
    savepucs(img_urls,titles)