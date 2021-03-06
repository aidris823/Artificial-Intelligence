#!/usr/bin/python3
import sys, math

#[A2,B2,C2,D3,E3,F3,G4,H4,I4,J5,K5,L5,M6,N6,O6,P7,Q7,R7,S7,T8,U8,V8,W9,X9,Y9,Z9]

alpha = 'abcdefghijklmnopqrstuvwxyz'
numbers = [None,None,['a','b','c'],['d','e','f'],['g','h','i'],
               ['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

a_w = open('dictall.txt','r')
all_words = a_w.read().split("\n")


valid = set()
for i in all_words:
    if len(i) == 5:
        valid.add(i)
def generate_words(numbers):
    ans = list()
    valid = set()
    
    for i in all_words:
        if len(i) == len(numbers):
            valid.add(i)
    for i in valid:
        candidate = generate_numbers(i)
        if candidate == numbers:
            ans.append(i)
    return ans
    
def generate_numbers(word):
    ans = list()
    split = list(word)
    for i in split:
        for j in range(2,len(numbers)):
            if i in numbers[j]:
                ans.append(j)
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    _ans = list()
    for i in range(len(ans)):
        _ans.append(str(ans[i]))
    return ''.join(_ans)


print generate_numbers("buttonwood")
print generate_numbers("fearme")
print generate_words("2888669663")
