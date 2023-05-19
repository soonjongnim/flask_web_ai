from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

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

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
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

    # 아까 확인했던 property로 클릭할 image element list 획득
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    dir = ".\idols" + "\\" + name

    createDirectory(dir) #폴더 생성
    # 해당 이미지들을 클릭하여 필요한 정보 획득
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath(
                '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute(
                "src")
            # urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
            # print('imgUrl: ' + imgUrl)
            opener = urllib.request.build_opener()
            opener.addheaders = [
                ('User-Agent',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
            ]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, dir + '\\' + name + str(count) + ".jpg")
            count = count + 1
            if count >= 200:
                break
        except Exception as e: 
            # print('e : ', e)
            pass
    driver.close() 

idols = ["워너원 강다니엘", "엑소 백현", "박보검", "송중기", "워너원 황민현", "엑소 시우민", "강동원", "이종석", "이준기", "마동석", "조진웅", "조세호", "안재홍", "윤두준", "이민기", "김우빈", "육성재", "공유", "방탄소년단 정국", "아이콘 바비", "워너원 박지훈", "엑소 수호"]

for idol in idols:
    crawling_img(idol)