"""
@Author: Rikesh Chhetri
@Date: 2021-07-31 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-31 10:03:30
@Title : Program Aim perform hadoop mapreduce for word length count.
"""
#!/usr/bin/python

import sys
  
current_length = None
current_count = 0
word_length = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word_length, count = line.split('\t', 1)
    
    count = int(count)
   
    if current_length == word_length:
        current_count += count
    else:
        if current_length:
            # write result to STDOUT
            print ('%s\t%s' % (current_length, current_count))
        current_count = count
        current_length = word_length
# for printing the last word  length
if current_length == word_length:
	print ('%s\t%s' % (current_length, current_count))