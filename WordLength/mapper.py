"""
@Author: Rikesh Chhetri
@Date: 2021-07-31 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-31 10:03:30
@Title : Program Aim perform hadoop mapreduce for word length count.
"""
#!/usr/bin/env python
"""mapper.py"""

# input comes from STDIN (standard input)
import sys
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (len(word), 1))
