#!/usr/bin/python3
import math, sys

file = open(sys.argv[1],'r')
ans = open(sys.argv[2],'w')

texts = file.read().split("\n")
for i in texts:
    line = i.split(",")
   # if len(texts[i]) > 1:
    #    stuff = texts[i][1:]
    ans.write(line[0])
#    print i
    if len(line) > 1:
        stuff = line[1:]
        stuff.sort()
        for i in stuff:
            ans.write(i)
    ans.write("\n")

        

file.close()
ans.close()

