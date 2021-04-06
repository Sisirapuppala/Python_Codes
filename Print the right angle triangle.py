//Example Input: 3
Example Output:

123
45
6
Example Input: 5
Example Output:

12345
6789
123
45
6
//
def solve(n):
    # write your code here
    c=0
    for i in range(0,n):
        for j in range(n-i,0,-1):
            if c==9:
                c=1
                print(c,end="")
            else:
                c=c+1
                print(c,end="")
        print()
