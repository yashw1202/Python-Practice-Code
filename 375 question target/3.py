# Maximum Sub-array

# Given an integer array nums, find the 
# subarray
# with the largest sum, and return its sum.
import sys
nums=list(map(int,input().split()))
maxi = -sys.maxsize-1
n = len(nums)
sum=0
for num in range(n):
    sum+=nums[num]
    if sum>maxi:
        maxi=sum
    if sum<0:
        sum=0
print(maxi)
