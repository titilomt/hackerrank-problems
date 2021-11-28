#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#

def foo(codeList, shoppingCart):
    # Write your code here
    subShoppingCart = shoppingCart

    def verifyCode(slist, code):
        for i, v in enumerate(slist):
            if code[i] == 'anything':
                continue
            if v != code[i]:
                return False
        return True

    for code in codeList:
        temp = code.split(' ')

        firstidx = [x for x in range(len(subShoppingCart))
                    if verifyCode(subShoppingCart[x: x + len(temp)], temp)][:1]

        if firstidx:
            idx = firstidx.pop(0)
            idx = idx + len(temp)
            if idx > len(subShoppingCart):
                return 0
            else:
                subShoppingCart = subShoppingCart[idx:]

        else:
            return 0

    return 1


if __name__ == '__main__':

    codeList_count = 4

    codeList = [
        'orange',
        'apple apple',
        'banana orange apple',
        'banana'
    ]

    # for _ in range(codeList_count):
    #     codeList_item = input()
    #     codeList.append(codeList_item)

    # shoppingCart_count = int(input().strip())

    shoppingCart = ['orange',
                    'apple',
                    'apple',
                    'banana',
                    'orange',
                    'apple',
                    'banana'
                    ]

    # for _ in range(shoppingCart_count):
    #     shoppingCart_item = input()
    #     shoppingCart.append(shoppingCart_item)

    result = foo(codeList, shoppingCart)

    print(str(result) + '\n')
