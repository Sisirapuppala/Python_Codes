n = int(input(""))

for i in range (n):
    inp =int(input())
    for y in range(1, inp + 1):
        
        x=""
        for j in range(3):
            x+=str(y)+ " "
        x=x.strip()
        print(x)
    
