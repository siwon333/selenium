from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import matplotlib.pyplot as plt

tags=[]
years=[]
y=[]
query_txt = "디지털" # 검색창에 검색할 단어 입력

path = (r"C:\Users\siwon\OneDrive\바탕 화면\크롤링\chromedriver.exe")
driver = webdriver.Chrome(path)

driver.get("http://www.yes24.com/Product/Search?domain=ALL&query="+query_txt+"&page=1&size=120") # 드라이버가 제어할 사이트
time.sleep(3) #3초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

book_tag = driver.find_elements_by_css_selector(".tag") #키워드 추출, 변수에 저장
no = len(book_tag) #키워드 개수 세기
if no == 0 : #만약 키워드가 없다면
    print("검색결과가 없습니다.") #출력
else: #키워드가 1개 이상 있다면
    print("키워드 수 : ",no,"개") #키워드 개수 출력
    for i in book_tag: #반복문 / 키워드 수만큼 반복
        title = i.text # 추출한 키워드를 title에 저장
        
        #광고 문구 제거
        if (title=="#북클럽에선무제한")or(title=="#북클러버의선택"):
            title = "" 
        else:
            print(title)
            tags.append(title) #title을 리스트에 저장
        #print(title)

result = list(set(tags)) #반복되는 문자열 삭제
print(result, len(result), "개") #추출 키워드 출력, 키워드 개수 출력

time.sleep(3)
book_time = driver.find_elements_by_xpath('//span[@class="authPub info_date"]')

for i in book_time:
    year = i.text.split()[0]  # Split the text and get the year part
    if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
        years.append(year)

driver.get(r"http://www.yes24.com/Product/Search?domain=ALL&query="+query_txt+"&page=2&size=120")
book_time = driver.find_elements_by_xpath('//span[@class="authPub info_date"]')

for i in book_time:
    year = i.text.split()[0]  # Split the text and get the year part
    if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
        years.append(year)
    if len(years)==100:
        break

print("2017년 : ",years.count("2017년")) #years리스트 안에 2017인 값의 개수
print("2018년 : ",years.count("2018년")) #years리스트 안에 2018인 값의 개수
print("2019년 : ",years.count("2019년")) #years리스트 안에 2019인 값의 개수
print("2020년 : ",years.count("2020년")) #years리스트 안에 2020인 값의 개수
print("2021년 : ",years.count("2021년")) #years리스트 안에 2021인 값의 개수
print("2022년 : ",years.count("2022년")) #years리스트 안에 2022인 값의 개수
print(len(years))

# 그래프로 표현할 두 데이터 리스트 정의
sun = [2017, 2018, 2019, 2020, 2021, 2022]
scores = [years.count("2017년"), years.count("2018년"), 
          years.count("2019년"), years.count("2020년"), years.count("2021년"), years.count("2022년")]

plt.plot(sun, scores) # 사용할 데이터 리스트 선언

# X값과 y값으로 사용할 값 설정
plt.xlabel('Year')
plt.ylabel('Score')

plt.grid(True) # 눈금 표시

plt.show()# 그래프 보여주기