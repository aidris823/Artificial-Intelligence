#!/usr/bin/python3
import sys
word_list = open("dictall.txt","r")
file = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

words = file.read().split("\n")
words.pop()

swag = set()
alphabet = list("abcdefghijklmnopqrstuvwxyz")

all_words = word_list.read().split("\n")

for word in all_words:
    if len(word) == 4:
        swag.add(word)

neighbors = dict()
for i in words:
    ans = list()
    for j in range(len(i)):
        scatter = list(i)
        for k in scatter:
            for l in range(len(alphabet)):
                scatter[j] = l
                x = "".join(scatter)
                if x in swag:
                    ans.append(x)
    neighbors[i] = ans
        
         

word_list.close()
file.close()
output.close()
