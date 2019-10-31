import time
from selenium import webdriver

def getdata(html):
    pass

def run():
    json_url='https://miaosha.jd.com/'
    # options=webdriver.ChromeOptions()
    # options.binary_location=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    # drive_binary=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    drive=webdriver.Chrome()
    drive.get(json_url)
    time.sleep(5)

    html=drive.page_source
    drive.quit()
    print(html)
def demo():
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()  # 创建实例
    driver.get("http://www.baidu.com")  # 请求百度首页
    time.sleep(6)  # 睡眠六秒
    driver.quit()  # 退出浏览器


if __name__=='__main__':
    run()