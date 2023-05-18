from selenium import webdriver
import time

path = (r"C:\Users\siwon\OneDrive\바탕 화면\크롤링\chromedriver.exe")
driver = webdriver.Chrome(path)

# Navigate to the search result page


years = []
while len(years) < 100:
    driver.get('https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&ra=qntt&len=100')
    # Find all the elements that match the given XPath expression
    book_time = driver.find_elements_by_xpath('//span[@class="authPub info_date"]')

    for i in book_time:
        year = i.text.split()[0]  # Split the text and get the year part
        if year in ['2017년', '2018년', '2019년', '2020년', '2021년', '2022년']:
            years.append(year)
            print(years)

            if len(years) == 100:
                break

    if len(years) == 81:
        time.sleep(2)
        next_url = 'https://search.kyobobook.co.kr/search?keyword=%EB%94%94%EC%A7%80%ED%84%B8&target=total&gbCode=TOT&page=2&ra=qntt&len=100'
        driver.get(next_url)

# Print the list of years
print(years)
