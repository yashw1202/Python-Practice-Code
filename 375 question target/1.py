#Maximum and minimum of an array using minimum number of comparisons

#Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.
import sys
def setmini(N):
    mini= sys.maxsize 
    for num in N:
        mini=min(num,mini)
    return mini
def setmaxi(N):
    maxi= -sys.maxsize-1 
    for num in N:
        maxi=max(num,maxi)
    return maxi
N = list(map(int,input().split()))
print(f"Smallest is {setmini(N) }")
print(f"Largest is {setmaxi(N) }")