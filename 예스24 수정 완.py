#필요한 라이브러리 호출
from selenium import webdriver #셀레니움:동적 사이트 크롤링 도구
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import matplotlib.pyplot as plt #맷플롯립:시각화 도구
from collections import Counter #카운터: 요소의 개수 세기
import csv #csv 확장자 입출력
import time #시간 
import re
from selenium.common.exceptions import NoSuchElementException

def remove_duplicates(lst): #중복 없애기 함수 정의
    return list(set(lst))

#리스트 정의
data = []
links = []
book_info_list = [] #책 정보 저장
name = [] #책 제목 저장
tags = [] #책 태그 저장
rt = [] #가공한 태그 저장
years = [] #책 발행년도 저장
query_txt = "디지털" #input("검색 단어 입력 : ") # 검색창에 검색할 단어 입력

path = r"C:\Users\siwon\Desktop\크롤링\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(r"http://www.yes24.com/Product/Search?query=%EB%94%94%EC%A7%80%ED%84%B8&domain=BOOK&page=1&size=120") # 드라이버가 제어할 사이트
time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

time.sleep(3) #3초 대기
links = [] #순회할 리스트

while len(book_info_list) < 100:  # 100개의 정보를 수집할 때까지 반복
    link_list = driver.find_elements_by_class_name("gd_name") 
    #클래스 이름이 prod_info인 요소를 찾아 변수에 저장
    for link_element in link_list:
        href = link_element.get_attribute('href')#링크를 변수에 저장
        if 'Goods' in href:  # 링크에 'S000'이 포함되어 있으면 저장 / S0000가 들어가야 도서
            links.append(href)

    linkss = remove_duplicates(links) #중복 링크 삭제
    n = len(linkss) #저장된 링크 수
    print("링크 수집 완료")

    for link in linkss: #저장한 링크 순회
        tags = [] #태그 저장 리스트 정의
        year = [] #발행년도 저장 리스트 정의 
        driver.get(link) #드라이버가 제어할 사이트 불러오기
        time.sleep(2) #2초 기다리기 / 로딩이 다 될때까지

        div_element = driver.find_element_by_class_name("gd_date") #발행년도 요소 추출
        text = div_element.text   #텍스트로 저장
        data = text.split()
        year = data[0]
            
        if year not in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']: #이 년도의 책이 아니면 for문의 처음으로 돌아가기
            continue

        book_name = driver.find_elements_by_class_name('gd_name') #책 제목 요소 추출
        name = book_name[0].text 

        book_cate = driver.find_elements_by_css_selector('#infoset_goodsCate > div.infoSetCont_wrap > dl > dd > ul > li:nth-child(1) > a:nth-child(4)') #책의 카테고리 요소 추출
        categories = book_cate[0].text  #저장

        try:
            book_tag = driver.find_element_by_id("tagArea")
            tags = book_tag.find_elements_by_tag_name("a")
            exclude_phrases = ["#크레마클럽에있어요", "#분철","#책읽아웃","#2023을예측하다","#인문위클리레터에소개된책"]
            rt = [a.text for a in tags if all(phrase not in a.text for phrase in exclude_phrases)]

        except NoSuchElementException:
            rt = []

        book_info = [name, year, categories, rt] 
        #책 정보(책 제목, 발행년도, 카페고리, 태그) 저장

        book_info_list.append(book_info) #책 정보를 리스트에 저장
        print(len(book_info_list)) #리스트의 요소 개수 출력

        if len(book_info_list) >= 100: #개수가 100개 되면 for문을 나가기
            break

    else : #100개가 안되면 다음 페이지로
        driver.get(r"http://www.yes24.com/Product/Search?query=%EB%94%94%EC%A7%80%ED%84%B8&domain=BOOK&page=2&size=120")

print(book_info_list) #100개의 책 정보 리스트 출력

driver.quit() #드라이버 종료

with open('outputY.csv', 'w', newline='') as csvfile: #100개의 책 정보를 csv파일로 저장
    writer = csv.writer(csvfile)
    writer.writerows(book_info_list)
