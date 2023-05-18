#필요한 라이브러리 호출
from selenium import webdriver #셀레니움:동적 사이트 크롤링 도구
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import matplotlib.pyplot as plt #맷플롯립:시각화 도구
from collections import Counter #카운터: 요소의 개수 세기
import csv #csv 확장자 입출력
import time #시간 
import re

def remove_duplicates(lst): #중복 없애기 함수 정의
    return list(set(lst))

#리스트 정의
book_info_list = [] #책 정보 저장
name = [] #책 제목 저장
tags = [] #책 태그 저장
rt = [] #가공한 태그 저장
years = [] #책 발행년도 저장
query_txt = "디지털" #input("검색 단어 입력 : ") # 검색창에 검색할 단어 입력

path = r"C:\Users\siwon\Desktop\크롤링\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(r"https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&ra=qntt&len=100") # 드라이버가 제어할 사이트
time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

time.sleep(3) #3초 대기
links = [] #순회할 리스트

while len(book_info_list) < 100:  # 100개의 정보를 수집할 때까지 반복
    link_list = driver.find_elements_by_class_name("prod_info") 
    #클래스 이름이 prod_info인 요소를 찾아 변수에 저장
    for link_element in link_list:
        href = link_element.get_attribute('href')#링크를 변수에 저장
        if 'S000' in href:  # 링크에 'S000'이 포함되어 있으면 저장 / S0000가 들어가야 도서
            links.append(href)

    linkss = remove_duplicates(links) #반복되는 링크 저장
    n = len(linkss) #저장된 링크 수
    print("링크 수집 완료")

    for link in linkss: #저장한 링크 순회
        tags = [] #태그 저장 리스트 정의
        year = [] #발행년도 저장 리스트 정의 
        driver.get(link) #드라이버가 제어할 사이트 불러오기
        time.sleep(2) #2초 기다리기 / 로딩이 다 될때까지

        div_element = driver.find_element_by_css_selector(".prod_info_text.publish_date") #발행년도 요소 추출
        text = div_element.text   #텍스트로 저장
        pattern = r"(\d+년)" #정규식
        match = re.search(pattern, text) #이 패턴을 찾아서 변수에 저장
        if match:
            year = match.group(1) #이 패턴이 맞으면 저장
        else:
            year = "텍스트를 찾을 수 없음" #이 패턴이 아니면 텍스트 출력
            
        if year not in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']: #이 년도의 책이 아니면 for문의 처음으로 돌아가기
            continue

        book_name = driver.find_elements_by_class_name('prod_title') #책 제목 요소 추출
        name = book_name[0].text if len(book_name) > 0 else "책 제목 없음" #값이 있으면 텍스트로 저장, 없으면 텍스트 출력

        book_cate = driver.find_elements_by_css_selector('.intro_book ul li a:nth-child(3)') #책의 카테고리 요소 추출
        categories = [elem.text for elem in book_cate]  #저장

        book_tag = driver.find_elements_by_class_name('tab_text') #책의 태그 요소 추출
        for element in book_tag: 
            tags.append(element.text) #추출한 요소 추출
        rt = tags[13:-8] #요소 데이터 전처리
        rt = [elem for elem in rt if elem != "교환/반품/품절"]

        book_info = [name, year, categories, rt] 
        #책 정보(책 제목, 발행년도, 카페고리, 태그) 저장

        book_info_list.append(book_info) #책 정보를 리스트에 저장
        print(len(book_info_list)) #리스트의 요소 개수 출력

        if len(book_info_list) >= 100: #개수가 100개 되면 for문을 나가기
            break

    else : #100개가 안되면 다음 페이지로
        driver.get(r"https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&page=2&ra=qntt&len=100")

print(book_info_list) #100개의 책 정보 리스트 출력

driver.quit() #드라이버 종료

with open('output.csv', 'w', newline='') as csvfile: #100개의 책 정보를 csv파일로 저장
    writer = csv.writer(csvfile)
    writer.writerows(book_info_list)
