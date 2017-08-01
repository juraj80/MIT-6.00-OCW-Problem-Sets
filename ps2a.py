# -*- coding: utf-8 -*-
'''Problem 1.
Diophantine Equation
Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, by finding
solutions to the Diophantine equation. You can solve this in your head, using paper and pencil,
or writing a program. However you chose to solve this problem, list the combinations of 6, 9
and 20 packs of McNuggets you need to buy in order to get each of the exact amounts.
Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by combinations of 6,
9 and 20 packs, show that it is possible to buy 56, 57,…, 65 McNuggets. In other words, show
how, given solutions for 50-55, one can derive solutions for 56-65. '''


n=50

#6a+9b+20c=n

result=[]
bestsoFar = 0

while n<200:
    for c in range (0,n/20+1):
        for b in range (0,n/9+1):
            for a in range (0,n/6+1):
                if 6*a+9*b+20*c==n:
                     bestSoFar=n   
                     if n not in result:   
#                         result = result + [n]   
                         result=result+[n,(a,b,c)]
                elif 6*a+9*b+20*c>n:
                    break
    n=n+1              
print result
print bestSoFar    
