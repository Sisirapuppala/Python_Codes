class Solution:
    def partition(self,A,pivot):
        i=-1
        high=A[pivot]

        for j in range(0,len(A)-1):
            if A[j] <= high:
                i+=1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        i+=1    
        temp=A[i]
        A[i]=A[pivot]
        A[pivot]=temp
//
Write a program to partition a given array around an element (called the pivot). Given the array and the index of pivot element (passed as parameters to the function), rearrange the numbers in the array so that all elements lesser than the pivot come to the left of it, while all numbers greater than the pivot come to the right of it in the newly rearranged array.

Example Input:

9 -6 6 10 1 -3 -8 -3 -8 -2
9
Output:

-6 -3 -8 -3 -8 -2 6 10 1 9//
