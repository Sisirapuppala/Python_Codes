//palindrome program
a=(input())
s=list(a)
w=s[::-1]
g="".join(w)
print(g)
if(a==g):
    print("palindrome")
else:
    print("not")
