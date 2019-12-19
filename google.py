from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# imprt bs4
# soup = bs4. BeautifulSoup()
# 앞에 프롬 임포트를 쓰면 위와 아래의 식이 같아짐 bs4생략가능?
# from bs4 improt BeaytifulSoup
# soup = BeautifulSoup()

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://www.google.com/')
search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('hello world')
search_input.send_keys(Keys.RETURN)