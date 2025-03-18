# Write a python program to extract the 3rd substring from each line in the input file
# Request-ID-list.txt (attached) and write the output to a separate file.
#
# For example, the substring 'op2xyzgarden' needs to be extracted from the string
# 'abc_xyzGarden-op2rajourixyzgarden-2023-04-11-02h-55m-36s-42D_17L_2M_eyBKN
# MCcYzM2W6Qt8WHCGY'

with open(r"D:\New_folder\New_1\Request-ID-list.txt", '+r') as file:
    file1=file.readlines()
    for file2 in file1:
        print(file2.split("-")[1])