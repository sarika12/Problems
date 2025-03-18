# The file model2_timings.txt contains a time at the end of each line.
#
# Write a python program to
# (1) find the max time in the file
# (2) find the min time in the file
# (3) find the average time in the file

file_time_add=[]
with open(r"/New_1/model2_timings.txt", '+r') as file:
    file1=file.readlines()
    for file2 in file1:
        file_time=file2.split()[-1]
        file_time_add.append(file_time)
print(max(set(file_time_add)))
print(min(set(file_time_add)))
a=list((file_time_add))
print(a)
# print(sum((set((file_time_add)))))


number_appends=[]
for i in a:
    b=float(i.strip("()s"))
    number_appends.append(b)
print(sum(number_appends))













