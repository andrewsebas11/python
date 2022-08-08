import os.path
import csv
fileexist = os.path.isfile('output1.csv')
print(fileexist)
# with open('output1.csv', 'a') as file:
#     w = csv.writer(file)
#     w.writerow(['ID', 'name', 'age'])
#     w.writerow([1, 'andrew', '26'])


if fileexist == True:
    with open('output1.csv', 'a') as file:
        w = csv.writer(file)
        w.writerow(['1', 'andrew', '26'])
else:
    with open('output1.csv', 'a') as file:
        w = csv.writer(file)
        w.writerow(['ID', 'name', 'age'])
        w.writerow([1, 'andrew', '26'])