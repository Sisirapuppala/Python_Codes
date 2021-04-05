//
The first prime number is 2. The next prime number: 3. The 7th prime number is 17
Example Input: 1
Output: 2
Example Input: 3
Output: 5
Example Input: 7
Output: 17
//
def solve(n):
    # write your code here
    prime_numbers = [2,3]
    i=3

    if(0<n<3):
        print(n,prime_numbers[n-1])
    elif(n>2):
        while (True):
            i+=1
            status = True
            for j in range(2,int(i/2)+1):
                if(i%j==0):
                    status = False
                    break
            if(status==True):
                prime_numbers.append(i)
            if(len(prime_numbers)==n):
                break
        print( prime_numbers[n-1])
    else:
        print(' ')
