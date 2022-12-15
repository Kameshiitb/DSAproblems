
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):

    # Write your code here
    arr.sort()

    min_arr = arr[0:4] #taking first four numbers of sorted list
    max_arr = arr[1:5] #taking last four numbers of sorted list
    
    max_sum = sum(max_arr)
    min_sum = sum(min_arr)
    
    print(min_sum, max_sum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)