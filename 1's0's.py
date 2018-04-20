'''
Given a string consisting of zeros and ones, you are allowed to flip at most 1 bit from 0 to 1.
   Print the size of the subarray which consists of maximum no. of consecutive 1s (after changing a bit).
   For Eg.
    Input : 1 0 1 1 1 0 1 1 1 0
    Output : 7  
'''

l=[1,0,1,1,1,0,1,1,1,0]
last,c,maxi=-1,0,0
for i in range(len(l)):
    if l[i]==0:
        if last!=-1:
            if maxi<c:
                maxi=c
                c=i-last
                last=i
        else:
            last=i
            c+=1
    else:
        c+=1
print(maxi if c<maxi else c)
        
