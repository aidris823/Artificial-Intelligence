#!/usr/bin/python3
import math

words = open("dictall.txt","r")
allwords = words.read().split("\n")
valid = set()
for i in allwords:
    if len(i) == 9:
        valid.add(i)
alpha = "abcdefghijklmnopqrstuvwxyz"
word = list("carthorse")
for i in range(26):
    letters.append(0)
for i in word:
    counter = 0
    for j in list(alpha):
        if i == j:
            letters[counter] += 1
        counter += 1
for i in valid:
    broken = list(i)
    for j in broken:
        counter = 0
        candidate = list()
        for k in range(26):
            candidate.append(0)
        for k in list(alpha):
            if i == j:
                candidate[counter] += 1
            counter += 1
        if candidate == letters:
            print i
            
                
def factorial(x):
    ans = 1
    factor = len(x)
    for i in range(len(x)):
        ans *= factor
        factor -= 1
    return ans

        
#Gives permutation of the list x
'''
def perm(x): 
    num = factorial(x)
    foo = x
    ans = list()
    
    for i in range(num):
        ans.append(foo)
        #print ans
        dummy = foo[i]
        foo[i] = foo[i+1]
        foo[i+1] = dummy
        print foo
        #print ans
    return ans
ex = [1,2,3,4]

print perm(ex)
'''
