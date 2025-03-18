def count_substring(string, sub_string):
    flag = False
    pos = -1
    n = len(string)
    count = []
    while True:
        pos = string.find(sub_string, pos + 1, n)

        if pos == -1:
            break
        count.append(pos)
        flag = True
    if flag == False:
        return 0
    return len(count)




if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)