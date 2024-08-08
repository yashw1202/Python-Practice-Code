#Array Reverse

#Reversing an array means changing the position of each number in the array to its corresponding position from the end. 
#For example, if a number is at position 1,its new position will be at Array.
#length, and similarly, if a number is at position 2, its new position will be at Array.length – 1, and so on.

N = list(map(int,input().split()))
rev = N[::-1]
print(rev)

