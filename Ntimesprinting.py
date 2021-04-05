n = int(input(""))
k = int(input(""))
for i in range (1,n+1):
    x=""
    for j in range(k):
        x+=str(i)+ " "
    x=x.strip()
    print(x)
    
