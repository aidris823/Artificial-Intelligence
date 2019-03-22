#!/usr/bin/python3
import sys

mercury = open("dictall.txt","r")

alpha = "abcdefghijklmnopqrstuvwxyz"
word = "horsecart"
broken = list(word)
print broken

letters = list()
for i in range(26):
    letters.append(0)
print letters
print len(letters)

for i in broken:
    counter = 0
    for j in list(alpha):
        if i == j:
            letters[counter] += 1
        counter += 1
for i in range(362880):
    

            

