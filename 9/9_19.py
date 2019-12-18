import csv
with open("./user_info.csv","r",encoding="utf-8")as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
        print(row[0])
        print(row[1])
        print("--------------")
