# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
nums= list(map(int,input().split()))
if len(set(nums))==len(nums):
    print(False)
else:
    print(True)