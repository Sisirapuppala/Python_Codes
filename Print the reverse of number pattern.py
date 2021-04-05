//5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
//
n = int(input())  
for i in range(0, n):  
    # inner loop for decrement in i values  
    for j in range(i+1):  
        print(n-j, end=' ')  
    print()  


