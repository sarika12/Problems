def is_palindrome(s):
    return s==s[::-1]




def find_all_palindrome(str1):
    n=len(str1)
    palindrom=[]
    for start in range(n):
        for end in range(start+1,n+1):
            substring=str1[start: end]
            if is_palindrome(substring):
                palindrom.append(substring)
    return palindrom



str1= "abaGADAGdata"
a=find_all_palindrome(str1)
print(a)