#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#


def searchSuggestions(repository, customerQuery):
    # Write your code here
    print(repository, customerQuery)

    if len(customerQuery) < 2:
        return None

    ans = []

    for i in range(1, len(customerQuery)):
        # temp = [ r for r in repository if customerQuery[:i+1].lower() in r.lower() ]
        temp = filter(
            lambda s: customerQuery[:i+1].lower() in s.lower(), repository)

        temp = sorted(temp, key=str.lower)[:3]
        print(len(temp))
        ans.append(temp)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
