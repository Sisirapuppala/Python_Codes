//Write a program to sort the given array by using merge sort.Your solution must be in
//O(N logN).
//Example Input:
//1 3 2 1 4 5
//Output:
//1 1 2 3 4 5
class Solution {
  public static int [] divide(int arr[])
  {
    if(arr.length==0||arr.length==1)
    return arr;
    int len=arr.length;
    int left[]=new int[len/2];
    int right[];
    if(len%2==1)
    right=new int[len/2+1];
    else
    right=new int[len/2];
    for(int i=0;i<len/2;i++)
    left[i]=arr[i];
    for(int i=len/2;i<len;i++)
    {
      right[i-len/2]=arr[i];
    }
    left=divide(left);
    right=divide(right);
    int sol[]=new int[left.length+right.length];
    sol=merge(left,right);
    return sol;
  }
  public static int[] merge(int a[],int b[])
  {
    if(a.length==0)
    return b;
    if(b.length==0)
    return a;
    int len=a.length+b.length;
    int ans[]=new  int[len];
    int k=0,l=0;
    for(int i=0;i<len;i++)
    {
         if(k<a.length&&l<b.length)
         {
           if(a[k]<b[l])
           {
             ans[i]=a[k];
             k++;
           }
           else{
             ans[i]=b[l];
             l++;
           }
         }
         else if(k==a.length)
         {
           ans[i]=b[l];
           l++;
         }
         else if(l== b.length)
         {
           ans[i]=a[k];
           k++;
         }
         
    }
    return ans;
  }
  public static int [] mergesort(int [] Arr) {
      /* write your solution here */
      Arr=divide(Arr);
      return Arr;
  }
}
