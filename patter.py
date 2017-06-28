'''
Generate the following pattern when x is given upto Nth terms
For ex:

Input: x=2 ,N=5

OUTPUT:

2

12

1112

3112

132112

'''

s,c,t="2",0,""
j=0
for i in range(5):
    while j<len(s):
        c=0
        for k in range(j,len(s)):
            if s[j]==s[k]:
                c+=1
        t+=s[j]+str(c)
        j+=c
    j=0
    s=t
    t=""
    print(s[::-1])
        
                
