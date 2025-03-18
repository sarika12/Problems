numberList = [55, 126, 85, 35, 89, 1000, 125]

for i in range(len(numberList)):
    for j in range(1, i + 1 - 1):
        if numberList[j] > numberList[j + 1]:
            numberList[j + 1] = numberList[j]
print(numberList[j + 1])


