#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# list1=[]
# list2=[]
# a=nums1[:m]
# b=nums2[:n]
# print(a)
# print(b)
#
m=3
n=3
# m=1
# n=0
p1=m-1
p2=n-1
p=m+n-1
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2,5,6]
# nums1=[1]
# nums2=[]
while p1>=0  and p2>=0:

    if nums1[p1]>nums2[p2]:
        nums1[p]=nums1[p1]
        p1-=1
    else:
        nums1[p]=nums2[p2]
        p2-=1
    p -= 1
print(nums1)



for i in range(m):
    if m==n:
        nums1[i-3]=nums2[i-m]

    elif m>n:
        print(nums1)
    else:
        print(nums2)

# print(nums1)

nums=[1,1,2]
print(len(nums))
dict1={}
list1=[]
for i in range(len(nums)):
    # print(i)
    if nums[i] in dict1:
        dict1[nums[i]]+=1
    else:
        dict1[nums[i]]=1
for k,v in dict1.items():
    list1.append(k)
print(list1)





