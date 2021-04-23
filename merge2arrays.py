class Solution:
    def mergeTwoArrays(self, A, B, C):
        # write your method here
        n1=len(A)
        n2=len(B)
       
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2: 
            if A[i] < B[j]: 
                C[k] = A[i] 
                k = k + 1
                i = i + 1
            else: 
                C[k] = B[j] 
                k = k + 1
                j = j + 1
        while i < n1: 
            C[k] = A[i]
            k = k + 1
            i = i + 1

        while j < n2: 
            C[k] = B[j]; 
            k = k + 1
            j = j + 1
        return C
      
     # Write a program to merge two sorted Arrays into single sorted Array.The time complexity must be in O(N).
#Example:
#1 2 3 3
#2 4 5 6
#Ouput:
#1 2 2 3 3 4 5 6
