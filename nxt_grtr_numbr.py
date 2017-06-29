'''Find next greater number with same set of digits
Given a number n, find the smallest number that has same set of digits as n and is greater than n. If x is the greatest possible number with its set of digits, then print “not possible”.

Examples:
For simplicity of implementation, we have considered input number as a string.

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"
'''

s,g="218765",""
l,r=list(s),[]
if s==s[::-1]:
    print("Nope. NOt Possible")
elif len(s)==2:
    print(s[::-1])
else:
    for i in range(len(s)-1,0,-1):
        t=list(s[i:])
        if t==sorted(t,reverse=True):
            continue
        else:
            g=s[i]
            t=list(s[i+1:])
            r=list(s[:i])
            print(t,r)
            break
    for j in range(len(t)-1,0,-1):
        if t[j]>g:
            v=g
            g=t[j]
            t[j]=v
            t.sort()
            break
    print("".join(r)+g+"".join(t))
            
            
            
    
