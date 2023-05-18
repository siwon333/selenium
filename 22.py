import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from collections import Counter

book_info_list = []
yyyy= []
font_path = 'C:\Windows\Fonts\gulim.ttc'
fontprop = fm.FontProperties(fname=font_path, size=12)

with open('output.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        book_info_list.append(row)

for i in range(100):
    yyyy.append(book_info_list[i][1])

yyyy = tuple(yyyy)
counts = Counter(yyyy)

x_list = list(counts.keys())
X = [item.strip('년') for item in x_list]
y = list(counts.values())

sorted_data = sorted(zip(X, y))
X_sorted, y_sorted = zip(*sorted_data)

plt.plot(X_sorted, y_sorted,'b-', marker='o')
for i, j in zip(X_sorted, y_sorted):
    plt.text(i, j, str(j), ha='center', va='bottom')

plt.xlabel('년도',fontproperties=fontprop)
plt.ylabel('권 수',fontproperties=fontprop)
plt.title('교보문고',fontproperties=fontprop)
plt.grid(True)
plt.show()