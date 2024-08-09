# Repeat and Missing Number Array

# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.

def repeatedNumber(A):
        lst=[0,0]
        for i in range(1,len(A)+1):
            if A.count(i)==2:
                lst[0]=i
            elif A.count(i)==0:
                lst[1]=i
            else:
                continue
        return lst
A= list(map(int,input().split()))
print(repeatedNumber(A))