import csv

def reading():
    with open("user.csv",mode="r") as file :
        reader=csv.reader(file)
        header=next(reader)
        for row in reader:
            # print(row)
            print(f"user {row[0]}")





a=reading()
# print(a)