from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import matplotlib.pyplot as plt

tags=[]
years=[]
y=[]
query_txt = "디지털" #input("검색 단어 입력 : ") # 검색창에 검색할 단어 입력

path = (r"C:\Users\siwon\OneDrive\바탕 화면\크롤링\chromedriver.exe")
driver = webdriver.Chrome(path)

driver.get("http://www.yes24.com/Product/Search?domain=ALL&query="+query_txt+"&page=1&size=120") # 드라이버가 제어할 사이트
time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

# driver.find_element_by_id("query").click() #검색창 클릭
# element = driver.find_element_by_id("query") #검색창 입력 값을 변수로 설정
# element.send_keys(query_txt) #검색창 입력값에 단어 입력
# element.send_keys(Keys.ENTER) #Enter 누르기

# dropdown=Select(driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/section[2]/div[3]/div/span[2]/span[2]/select'))
# #콤보박스
# dropdown.select_by_value("120")#120개씩 보기
# time.sleep(3) #3초 대기

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
            tags.append(title) #title을 리스트에 저장
        #print(title)

result = list(set(tags)) #반복되는 문자열 삭제
print(result, len(result), "개") #추출 키워드 출력, 키워드 개수 출력

book_time = driver.find_elements_by_xpath('//span[@class="authPub info_date"]')

for i in book_time: #변수안에 값이 다 끝날때 까지
    year = i.text #출간일자를 year에 저장
    y=year.split() #공백을 기준으로 잘라서 y리스트에 저장
    years.append(y[0]) #y리스트에 저장된 연도만 years리스트에 추가

print("2017년 : ",years.count("2017년")) #years리스트 안에 2017인 값의 개수
print("2018년 : ",years.count("2018년")) #years리스트 안에 2018인 값의 개수
print("2019년 : ",years.count("2019년")) #years리스트 안에 2019인 값의 개수
print("2020년 : ",years.count("2020년")) #years리스트 안에 2020인 값의 개수
print("2021년 : ",years.count("2021년")) #years리스트 안에 2021인 값의 개수
print("2022년 : ",years.count("2022년")) #years리스트 안에 2022인 값의 개수

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