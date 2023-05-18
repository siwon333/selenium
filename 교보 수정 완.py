from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import matplotlib.pyplot as plt
from collections import Counter
import csv
import time
import re

def remove_duplicates(lst):
    return list(set(lst))

book_info_list = []
name = []
tags = []
rt = []
years = []
query_txt = "디지털" #input("검색 단어 입력 : ") # 검색창에 검색할 단어 입력

path = r"C:\Users\siwon\Desktop\크롤링\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(r"https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&ra=qntt&len=100") # 드라이버가 제어할 사이트
time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

time.sleep(3) #3초 대기
links = [] #순회할 리스트

while len(book_info_list) < 100:  # 100개의 정보를 수집할 때까지 반복
    link_list = driver.find_elements_by_class_name("prod_info")
    for link_element in link_list:
        href = link_element.get_attribute('href')
        if 'S000' in href:  # 링크에 'S000'이 포함되어 있는지 확인
            links.append(href)

    linkss = remove_duplicates(links)
    n = len(linkss)
    print("링크 수집 완료")

    for link in linkss:
        tags = []
        year = []
        time.sleep(2)
        driver.get(link)

        div_element = driver.find_element_by_css_selector(".prod_info_text.publish_date")
        text = div_element.text
        pattern = r"(\d+년)"
        match = re.search(pattern, text)
        if match:
            year = match.group(1)
        else:
            year = "텍스트를 찾을 수 없음"
            
        if year not in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
            continue

        book_name = driver.find_elements_by_class_name('prod_title')
        name = book_name[0].text if len(book_name) > 0 else "책 제목 없음"

        book_cate = driver.find_elements_by_css_selector('.intro_book ul li a:nth-child(3)')
        categories = [elem.text for elem in book_cate]

        book_tag = driver.find_elements_by_class_name('tab_text')
        for element in book_tag:
            tags.append(element.text)
        rt = tags[13:-8]
        rt = [elem for elem in rt if elem != "교환/반품/품절"]

        book_info = [name, year, categories, rt]

        book_info_list.append(book_info)
        print(len(book_info_list))

        if len(book_info_list) >= 100:
            break

    else : 
        driver.get(r"https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&page=2&ra=qntt&len=100")

print(book_info_list)

driver.quit()

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(book_info_list)
