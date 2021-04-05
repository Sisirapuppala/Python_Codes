def solve(n,character):
    # write your code from here
    if(character=="B"):
        other="W"
    else:
        other="B"
    for i in range(0,n):
        for j in range(0,n):
            if((i+j)%2==0):
                print(character,end="")
            else:
                print(other,end="")
        print()
