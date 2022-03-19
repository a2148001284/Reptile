import sys
sys.path.append("./package/")
from selenium import webdriver

def web_driver():
    options=webdriver.ChromeOptions()
    location=r"./chrome-win/chrome.exe"
    options.binary_location=location
    options.add_argument("headless")   #quiet execute
    driver=webdriver.Chrome("./chromedriver.exe",options=options)
    return driver

def page_search(keywords,pages):
    for j in range(1,pages+1):
        driver = web_driver()
        driver.get("https://github.com/search?p=%s&q=%s" % (j,keywords))
        title = driver.find_elements_by_xpath("//a[@class='v-align-middle']")
        explains = driver.find_elements_by_xpath("//p[@class='mb-1']")
        stars = driver.find_elements_by_xpath("//a[@class='Link--muted']")
        for i in range(len(title)):
            try:
                if(len(title)==len(explains)==len(stars)):
                    keys = title[i].get_attribute("text")  # a标签下xpath获取内容的方式
                    explain = explains[i].get_attribute('innerText')  # p标签获取内容的方式
                    star = stars[i].get_attribute("innerText")  # innerText标签有时候比text好用很多
                    url = title[i].get_attribute("href")  # a标签下获取href内容也是如此
                    # star.strip()  #字符串开头和结尾去空
                    # star.replace(" ","")   #完全去空
                    print("keys:", keys, " explain:", explain, " stars:", star, "  url:", url)
                else:
                    print("Some explains are None,So we miss the explains this page")
                    keys = title[i].get_attribute("text")
                    star = stars[i].get_attribute("innerText")
                    url = title[i].get_attribute("href")
                    print("keys:", keys, " explain:","None", " stars:", star, "  url:", url)
            except IndexError as f:
                print("IndexError: list index out of range")
        print("pages %s finished!"%j)
        driver.quit()

def main():
    keywords=input("please input the keywords you want to search:")
    pages=int(input("please input the pages all you want to get:"))
    page_search(keywords,pages)


if __name__ == '__main__':
    main()