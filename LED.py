'''
1. Count the number of changes in LED Light when display one digit after another of a given number. (Initially all LED is off)
Example:

Given number – 082
Answer: 9
Explanation: Initially 0 has 6 LED On, then for 8 we will turn on 1 more LED, then for 2 we turn off two LEDs so 6+1+2 = 9.
'''
s="082"
d={'0':{1,2,3,4,5,6},'1':{3,4},'2':{2,3,7,6,5},'3':{2,3,7,4,5},'4':{1,7,3,4},'5':{2,1,7,4,5},'6':{1,4,5,6,7},'7':{2,3,4},'8':{1,2,3,4,5,6,7},'9':{1,2,3,4,7}}
a,l=0,set()
for i in s:
    l^=d[i]
    a+=len(l)
    l=set(d[i])
print(a)
