import csv
import matplotlib.pyplot as plt
from collections import Counter

book_info_list = []
yyyy= []

with open('output.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        book_info_list.append(row)

for i in range(100):
    yyyy.append(book_info_list[i][1])

yyyy = tuple(yyyy)
counts = Counter(yyyy)
print(counts)

x_list = list(counts.keys())
y_list = list(counts.values())

plt.bar(x_list, y_list)
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Year')
plt.show()