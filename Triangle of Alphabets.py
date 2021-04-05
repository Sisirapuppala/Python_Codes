//
Input:
2
3
5

Output:
A
BB
CCC
A
BB
CCC
DDDD
EEEEE//

testcases=int(input())
for case in range(testcases):
    n=int(input())
    for i in range(n):
        print((chr(65+i))*(i+1))
