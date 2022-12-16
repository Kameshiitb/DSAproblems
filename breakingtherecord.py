import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    
    min_count = 0
    max_count = 0

    for score in scores:
        if score<min:
            min = score
            min_count+=1
        elif score>max:
            max = score
            max_count+=1
        else:
            pass        
    return  max_count, min_count

    

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print("She broke her max record ", result[0], "times.")
    print("She broke her max record ", result[1], "times.")
