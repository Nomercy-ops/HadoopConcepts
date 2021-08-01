"""
@Author: Rikesh Chhetri
@Date: 2021-07-31 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-31 10:03:30
@Title : Program Aim perform hadoop mapreduce for matrix multiplication.
"""
#!/usr/bin/env python 
"""mapper.py"""
import sys

for line in sys.stdin:
    line = line.strip() #used for removing white space
    entry = line.split(',') # splitting values by comma and storing it to entry
    key = entry[0]
    value = line[1:] 
    if key == "A":
        print('{0}\t{1}'.format(key,value))
    elif key == 'B':
         print('{0}\t{1}'.format(key,value))
