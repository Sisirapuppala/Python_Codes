//
*.........*
**.......**
***.....***
****...****
*****.*****
***********
*****.*****
****...****
***.....***
**.......**
*.........*
//
def solve(n):
    rows = n
    for i in range(1,rows+1):
	    for j in range(1,i+1):
		    print("*",end='')
	    for k in range(i*2, rows*2+1):
		    print(".",end='')
	    for l in range(1,i+1):
		    print("*",end='')
	    print()
    for i in range(0,rows*2+1):
	    print("*",end='')
    print()
    for i in range(1,rows+1):
        for j in range(i,rows+1):
            print("*",end='')
        for k in range(1,i*2):
            print(".",end='')
        for l in range(i,rows+1):
            print("*",end='')
        print()
