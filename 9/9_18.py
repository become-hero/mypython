import csv
dates=[["name","age"],["zhangsan",20],["lisi",30]]
'''
with open("./user_info.csv","w")as f:
    writer=csv.writer(f)
    for row in dates:
        writer.writerow(row)
'''
with open("./user_info.csv","w")as f:
    writer=csv.writer(f)
    writer.writerows(dates)
