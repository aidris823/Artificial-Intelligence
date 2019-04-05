#!/usr/bin/python3
import sys
word_list = open("dictall.txt","r")
all_words = word_list.read().split("\n")
valid = set()
for i in all_words:
    if len(i) == 4:
        valid.add(i)
alphabet = "abcdefghijklmnopqrstuvwxyz"
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

def make_dict(word,dist,start,end):
    ans = dict()
    ans["Word"] = word
    ans["Distance"] = dist
def find_path(start,end):
    pass
