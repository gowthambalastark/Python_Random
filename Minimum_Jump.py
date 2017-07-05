def min_jump(l):
    if l[0]==0:
        return -1
    a,b,c,i,f=0,1,l[0],0,0
    while(i<len(l)):
        maxi,k,t=0,0,0
        for j in range(i+1,i+c+1):
            if (i+c)>=len(l)-1:
                return b
            k+=1
            if maxi<=l[j]:
                maxi=l[j]
                t=i+k
        if maxi==0:
            return -1
        c=maxi
        b+=1
        i=t
l=[1, 1,1,0]
print(min_jump(l))
        
