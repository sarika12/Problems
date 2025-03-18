#We need to save username of students, input username and print valid if it contains alphanumeric and invalid if
# it contains any special characters or spaces or duplicate username. WAP in java or python to handle it

list1=[]
enter =set(list(input("enter user name ").split(sep=" ")))

# list1.append(enter)

print(enter)
for ls in enter:
    if ls.isalpha():
        print(f"username is valid {ls}")
    elif ls.isalnum() and ls.isdigit():
        print(f"ussernae is in-valid {ls}")
    else:
        print(f"user name is in-valid becuase of space and spical {ls}")