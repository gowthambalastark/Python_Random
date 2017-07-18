'''
There is a class of N students and you have to find the top K marks scorers.You need to print the index of the toppers of the class which will be same as the index of the student in the input array(use 0-based indexing).First print the index of the students having highest marks then the students with second highest and so on.If there are more than one students having same marks then print their indices in ascending order.Suppose k = 2 and the students having highest marks have indices 0 and 5 and students having second highest marks have indices 6 and 7 then output will be 0 5 6 7

Input:
The first line of input consists of an integer T denoting the number of test cases .Each test case consists of three lines first line consists of an integer N denoting the number of students of class second line consists N spaced integers denoting the marks of students and third line consists of an integer K which denotes the number of top scores you have to find.

Output:
Single line output, denoting the indices of top k cores with space between them.

Constraints:
1<=T<=100
1<=N<=1000
1<=marks of students<=10^6

It is given that k will be such that its value will always be less than or equal to type of marks of students
Example:
Input
1
5
2 2 1 3 1
2
Output
3 0 1
'''

for a in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m,d,c,i=int(input()),0,0,0
    l1=list(set([i for i in l]))
    l1.sort(reverse=True)
    for i in range(m):
        k=l.count(l1[i])
        print(l.index(l1[i]),end=' ')
        if k>1:
            for j in range(1,k):
                print((l.index(l1[i]))+j,end=' ')     
    print()
