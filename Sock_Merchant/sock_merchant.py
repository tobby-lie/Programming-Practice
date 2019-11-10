#----------------------------------------------------------------------------
# Sock Merchant problem from hackerrank.com
# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale, given an array of integers representing the color
# of each sock, determine how many pairs of socks with matching colors there
# are.
#----------------------------------------------------------------------------

import math
import os
import random
import re
import sys

#----------------------------------------------------------------------------
# Returns an integer representing the number of matching paris of socks that
# are available
#
#    n: number of socks in the pile
#    ar: colors of each sock, n space-separated integers describing colors ar[i]
#        of socks in the pile
#
#    constraints: 
#        1 >= n <= 100
#        1 <= ar[i] <= 100 where 0 <= i < n
#
#    sample input:
#        9
#        10 20 20 10 10 30 50 10 20
#
#    sample output:
#        3
#----------------------------------------------------------------------------
def sockMerchant(n, ar):

    # list of frequency of each item in ar
    frequencies = []
    # while ar still has elements
    while ar:
        # count frequency of first item in ar
        frequencies.append(ar.count(ar[0]))
        # remove first item in ar
        # use filter to take all elements not equal to ar[0] in ar and 
        # create a list and assign back to ar
        ar = list(filter((ar[0]).__ne__, ar))
    
    # number of pairs 
    pairs = 0
    # for all frequencies recorded
    for frequency in frequencies:
        # pairs incremented by floor of frequencies/2
        pairs += math.floor(frequency/2)

    return pairs

def main():
	# file pointer
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # number of elements in ar
    n = int(input())

    # list of sock colors taken from input that is stripped of trailing spaces and split
    ar = list(map(int, input().rstrip().split()))

    # number of pairs
    result = sockMerchant(n, ar)

    # write results to file
    fptr.write(str(result) + '\n')

    # close file pointer 
    fptr.close()


if __name__ == '__main__':
	main()
