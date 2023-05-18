from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import matplotlib.pyplot as plt

name = []
names = []
tags=[]
years=[]
y=[]
query_txt = "디지털" #input("검색 단어 입력 : ") # 검색창에 검색할 단어 입력

path = (r".\chromedriver.exe")
driver = webdriver.Chrome(path)

driver.get(r"https://search.kyobobook.co.kr/search?keyword="+query_txt+"&target=total&gbCode=TOT&ra=qntt&len=100") # 드라이버가 제어할 사이트
time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

time.sleep(3) #3초 대기
links=[] #순회할 리스트
link_list = driver.find_elements_by_class_name("prod_info")
for i in  link_list:
    href = i.get_attribute('href')
    links.append(href)
nn=(len(links))
print(links)

# 중복 제거를 위한 set 생성
unique_links = set()

# 중복 제거 및 리스트 갱신
for link in links:
    if link not in unique_links:
        unique_links.add(link)
    else:
        links.remove(link)

print(links)

years = []  # 빈 리스트 생성
category = []
for link in links:
    for i in range(len(links)):
        print(i,link)
    

#     time.sleep(1)
#     book_name = driver.find_elements_by_css_selector("div.prod_title_box > div.auto_overflow_contents > div > h1 > span")                     
#     book_time = driver.find_elements_by_xpath('//span[@class="date"]')
#     book_cate = driver.find_elements_by_css_selector('.intro_book ul li a:nth-child(3)')
#     book_tag = driver.find_elements_by_css_selector(".tag") #키워드 추출, 변수에 저장

    

#     if len(years) == nn:
#         break

# print("책 제목:",names)  
# print("발행연도:",years)
# print("카테고리:",category)


driver.quit()