from selenium import webdriver
import time

def web_driver():
    options=webdriver.ChromeOptions()
    location=r"./chrome-win/chrome.exe"
    options.binary_location=location
    options.add_argument("headless")
    driver=webdriver.Chrome("./chromedriver.exe",options=options)
    return driver

def main():
    driver=web_driver()
    driver.get("http://www.zsxg.cn/market")
    title=driver.find_elements_by_xpath("//div[@class='antd-pro-components-market-stock-list-styles-indexListRight']/div/div")
    name=driver.find_elements_by_xpath("//div[@class='antd-pro-components-market-stock-list-styles-itemName']")
    for i in range(len(name)):
        names=name[i].get_attribute("innerText")
        list=[]
        for j in range(i*11,i*11+11):
            titles=title[j].get_attribute("innerText")
            list.append(titles)
        print("股票:",names," 最新收盘价:",list[0]," PE:",list[1]," PE分位:",list[2]," PB:",list[3]," PB分位:",list[4]," ROE:",list[5]," 股息率:",list[6]," 近1月:",list[7]," 近3月:",list[8]," 近6月:",list[9]," 近1年:",list[10])

    time.sleep(5)
    driver.quit()




if __name__ == '__main__':
    main()