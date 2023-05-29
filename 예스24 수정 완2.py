#필요한 라이브러리 호출
import csv 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from collections import Counter

book_info_list = []
yyyy= []
font_path = 'C:\Windows\Fonts\gulim.ttc'
fontprop = fm.FontProperties(fname=font_path, size=12)

with open('outputY.csv', 'r', newline='') as csvfile: #앞에서 저장한 csv파일 가져오기
    reader = csv.reader(csvfile)
    for row in reader:
        book_info_list.append(row)
#csv파일에서 발행년도 데이터 가져오기        
for i in range(100):
    yyyy.append(book_info_list[i][1])

yyyy = tuple(yyyy) #발행년도 데이터를 튜플로 저장
counts = Counter(yyyy) #발행년도 개수 세기

x_list = list(counts.keys()) #튜플의 키값을 리스트로 저장
X = [item.strip('년') for item in x_list] #년 이라는 문자열 삭제
y = list(counts.values()) #튜플의 밸류값을 리스트로 저장

sorted_data = sorted(zip(X, y)) 
#두 리스트를 연결하고 정렬 / 두 리스트를 연결하지 않고 정렬하면 각 값이 달라짐
X_sorted, y_sorted = zip(*sorted_data)#연결해 정렬한 데이터를 각각 새로운 리스트로 저장

plt.plot(X_sorted, y_sorted,'b-', marker='o') #선그래프 그리기
for i, j in zip(X_sorted, y_sorted):
    plt.text(i, j, str(j), ha='center', va='bottom')

plt.xlabel('년도',fontproperties=fontprop) #x축에 년도 리스트 지정
plt.ylabel('권 수',fontproperties=fontprop) #y축에 권수 리스트 지정
plt.title('Yes24',fontproperties=fontprop)
plt.grid(True)
plt.show()