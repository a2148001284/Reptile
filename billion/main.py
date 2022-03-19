from selenium import webdriver
import time
import requests
from lxml import etree

#billion网站爬虫 可以用于爬取关键词对应的搜索结果名称以及url链接和其相应的点赞数量
#用户可以自行修改爬取的页数

def ahead_web():
    options=webdriver.ChromeOptions()
    location=r"./chrome-win/chrome.exe"
    options.binary_location=location
    options.add_argument("headless")
    driver = webdriver.Chrome("./chromedriver.exe", options=options)
    return driver

def next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)
    likes = html.xpath("//div[@class='ops']/span[@class='like']/@title")
    return likes

def main():
    driver=ahead_web()
    keyword=str(input("please input the keywords you want to search!!"))
    for i in range(1,20):
        url = "https://search.bilibili.com/all?keyword={}".format(keyword)
        url = url + "&page={}"
        url=url.format(i)
        print("******this url is:  "+url+"*************")
        driver.get(url)
        xpath_title = "//ul[@class='video-list clearfix']//li[@class='video-item matrix']/a"
        title_pre = driver.find_elements_by_xpath(xpath_title)
        xpath_next_url="//li[@class='video-item matrix']/a"
        next_url_pre=driver.find_elements_by_xpath(xpath_next_url)
        for j in range(len(title_pre)):
            title = title_pre[j].get_attribute("title")
            url_next=next_url_pre[j].get_attribute("href")
            likes=next_page(url_next)
            print("title is: "+title+" likes is:"+str(likes)+"  video_url is:  "+url_next)

    time.sleep(10)
    driver.quit()




if __name__ == '__main__':
    main()