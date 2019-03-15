#!/usr/bin/python3
import sys
word_list = open("dictall.txt","r")
fred = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

words = fred.read().split("\n")
words.pop()

valid = set()
alphabet = list("abcdefghijklmnopqrstuvwxyz")

all_words = word_list.read().split("\n")

for word in all_words:
    if len(word) == 4:
        valid.add(word)

neighbors = dict()

def find_neighbors(word):
    ans = list()
    sec = list(word)
    ls = sec[:]
    for i in range(4):
        ls = sec[:]
        for j in alphabet:
            ls[i] = j
            q = "".join(ls)
            if q != word and q in valid :
                ans.append(q)
    return ans
#print find_neighbors("head")
for i in valid:
    neighbors[i] = find_neighbors(i)

for i in words:
    fred_rogers = find_neighbors(i)
    length = len(fred_rogers)
    output.write(i + "," + str(length) + "\n")

    
    

'''
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
   '''     
         

word_list.close()
fred.close()
output.close()
