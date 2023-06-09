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

years = []  # 빈 리스트 생성
category = []
for link in links:
    time.sleep(1)
    book_name = driver.find_elements_by_css_selector("div.prod_title_box > div.auto_overflow_contents > div > h1 > span")
    for i in book_name:
        name = i.text  
        names.append(name)
        if len(names) == nn:
            break                       
    book_time = driver.find_elements_by_xpath('//span[@class="date"]')
    for i in book_time:
        year = i.text.split()[0]  
        years.append(year)
        if len(years) == nn:
            break
    book_cate = driver.find_elements_by_css_selector('.intro_book ul li a:nth-child(3)')
    for i in book_cate:
        cate = i.text
        category.append(cate)
        if len(category) == nn:
            break

    book_tag = driver.find_elements_by_css_selector(".tag") #키워드 추출, 변수에 저장
    for i in book_tag: #반복문 / 키워드 수만큼 반복
        title = i.text # 추출한 키워드를 title에 저장
        tags.append(title) #title을 리스트에 저장
        result = list(set(tags)) #반복되는 문자열 삭제
        print("키워드:",result,i,"==") #추출 키워드 출력, 키워드 개수 출력
    

    if len(years) == nn:
        break

print("책 제목:",names)  
print("발행연도:",years)
print("카테고리:",category)


driver.quit()
# for link in links:
#     book_name = driver.find_element_by_class_name('prod_title')
#     print(book_name.text)
        

# book_time = driver.find_elements_by_xpath('//span[@class="date"]') #출간일자를 수집할 변수

# for i in book_time:
#     year = i.text.split()[0]  # Split the text and get the year part
#     if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
#         years.append(year)



# book_time = driver.find_elements_by_xpath('//span[@class="date"]') #출간일자를 수집할 변수

# for i in book_time:
#     year = i.text.split()[0]  # Split the text and get the year part
#     if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
#         years.append(year)

# driver.get(r"https://search.kyobobook.co.kr/search?keyword="+query_txt+"&target=total&gbCode=TOT&page=2&ra=qntt&len=100")
# book_time = driver.find_elements_by_xpath('//span[@class="date"]')

# for i in book_time:
#     year = i.text.split()[0]  # Split the text and get the year part
#     if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
#         years.append(year)
#     if len(years)==100:
#         break

# print("2017년 : ",years.count("2017년")) #years리스트 안에 2017인 값의 개수
# print("2018년 : ",years.count("2018년")) #years리스트 안에 2018인 값의 개수
# print("2019년 : ",years.count("2019년")) #years리스트 안에 2019인 값의 개수
# print("2020년 : ",years.count("2020년")) #years리스트 안에 2020인 값의 개수
# print("2021년 : ",years.count("2021년")) #years리스트 안에 2021인 값의 개수
# print("2022년 : ",years.count("2022년")) #years리스트 안에 2022인 값의 개수
# print(len(years))

# # 그래프로 표현할 두 데이터 리스트 정의
# sun = [2017, 2018, 2019, 2020, 2021, 2022]
# scores = [years.count("2017년"), years.count("2018년"), 
#           years.count("2019년"), years.count("2020년"), years.count("2021년"), years.count("2022년")]

# plt.plot(sun, scores) # 사용할 데이터 리스트 선언

# # X값과 y값으로 사용할 값 설정
# plt.xlabel('Year')
# plt.ylabel('Score')

# plt.grid(True) # 눈금 표시

# plt.show()# 그래프 보여주기