'''
Problem 1
Write a program that computes and prints the 1000th prime number.
'''
from math import *

x=2
n=1000
count=1
sumlog=0

while count<=n:
    prime=True
    for i in range (2,x): # loop from 2 to x-1, in first iteration x==2 for loop is not executed
        if x%i==0:
            prime=False # if x is divisible by i, set prime to False and break from loop
            break
    if prime==True:
        sumlog+=log(x)
        if count==n:
            print x
        count=count+1
    x=x+1

print sumlog, n, sumlog/n
    

'''
x=2
n=20

while x<=n:
    prime = True
    for i in range(2,x):
        if x%i==0:
            prime = False
            break
    if prime == True:
        print x
    x=x+1
'''
