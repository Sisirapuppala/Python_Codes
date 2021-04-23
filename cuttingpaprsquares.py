#Mary has an n x m piece of paper that she wants to cut into 1 x 1 pieces according to the following rules:

#She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
#Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways 
#to cut a  3 x 2 piece of paper:
#Constraints
#1<=n, m<=109
#Output Format
#Print a long integer denoting the minimum number of cuts needed to cut the entire paper into  1 x 1 squares.
#Sample Input
#3 1
#Sample Output
#2
n,m = [int(i) for i in input().strip().split(" ")]
print(n*m - 1)
