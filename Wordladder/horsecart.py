
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
word.sort()
letters = list()
for i in range(26):
    letters.append(0)
for i in word:
    counter = 0
    for j in list(alpha):
        if i == j:
            letters[counter] += 1
        counter += 1
print letters
for i in valid:
    broken = list(i)
    broken.sort()
    if broken == word:
        print i
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
