def solve(n):
    while n%2==0:
        print(2,end=" ")
        n=n//2
    for i in range(3,int((n)**0.5)+1,2):
        while n%i==0:
            print(i,end=" ")
            n=n//i
    if n>2:
        print(n)
//
Complete the given method solve that takes as parameter a positive integer n and prints all the prime factors of the number n.

2 has only 1 prime factor: 2. However, for 63 there are 3 3 7

Note : Number will always greater than 1

Example Input: 6
Output: 2 3
Example Input: 27
Output: 3 3 3
Example Input: 321
Output: 3 107
//
