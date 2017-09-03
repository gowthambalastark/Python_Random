'''
printing odd star pattern:

n=3:

          *           
        * * *         
      * * * * *       
    * * * * * * *     
  * * * * * * * * *
  
'''
#n=int(input())
n=5
for i in range(n):
    for j in range(n*2+1):
        t=i*2+1
        t1=((n*2+1)-t)//2
        if j>(t1-1) and j<(n*2+1)-t1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
        
