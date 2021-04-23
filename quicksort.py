class Solution:
    def quicksort1(self,Arr,low,high):
        if(len(Arr)==1):
            return Arr
        if(low<high):
            pivot_position =self.partition(Arr,low,high)
            self.quicksort1(Arr,low,pivot_position-1)
            self.quicksort1(Arr,pivot_position+1,high)
    def quicksort(self, Arr):
# write your method here
            self.quicksort1(Arr,0,len(Arr)-1)
            return(Arr)

    def partition(self, A, low , pivot):
        i=low-1
        j=low
        while(j<=pivot):
            if(A[j]>A[pivot]):
                j=j+1
            else:
                i=i+1
                t=A[i]
                A[i]=A[j]
                A[j]=t
                j=j+1
        return i
//
Write a program to sort the given array by using quick sort.Your solution must be in
O(N logN).

Example Input:
1 3 2 6 4 5

Output:
1 2 3 4 5 6
//
