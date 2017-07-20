'''
Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
 
Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows. 
The first line of each test case contains a single integer N denoting the size of array. 
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
 
Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.
 
Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
-100 ≤ A[i] <= 100
 
Example:
Input
2
3
1 2 3
4
-1 -2 -3 -4
Output
6
-1

'''
for a in range(int(input())):
    m=int(input())
    l=list(map(int,input().split()))
    m,mi=l[0],l[0]
    for i in range(1, len(l)):
        m=max(l[i],m+l[i])
        mi=max(mi,m)
    print(mi)