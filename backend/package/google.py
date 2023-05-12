from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(name):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    xpath = images.get_attribute("xpath")
    print('xpath: ' + str(xpath))
    dir = ".\idols" + "\\" + name

    createDirectory(dir) #폴더 생성
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            # 요소의 full xpath 가져오기
            # xpath = image.get_attribute("xpath")
            # print('xpath: ' + str(xpath))
            imgUrl = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute("src")
            # //*[@id="islrg"]/div[1]/div[56]/div[51]/a[1]/div[1]/img
            # //*[@id="islrg"]/div[1]/div[57]/div[31]/a[1]/div[1]/img
            # //*[@id="islrg"]/div[1]/div[14]/a[1]/div[1]/img
            # /html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[56]/div[50]/a[1]/div[1]/img
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            path = ".\\idols\\" + name + "\\"
            urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
            count = count + 1
            if count >= 260:
                break
        except:
            pass

    driver.close()


idols = ["아이유"]

for idol in idols:
    crawling_img(idol)