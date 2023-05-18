import requests
from bs4 import BeautifulSoup as bs

res = requests.get("http://www.yes24.com/24/Category/BestSeller")
html = res.content
book = bs(html, "html.parser")

books=[]
book_list = book.select('#bestList > ol > li')

for book in book_list:
    title = book.select('p > a')[2].text
    price = book.select('p.price > strong')[0].text
    books.append(title)
    rank = len(books)

    print(rank,"위")
    print("도서명:",title)
    print("가격:",price)


