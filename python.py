#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

msg = ""
def test_case(n):
    global msg 
    fizz        = n % 3
    buzz        = n % 5
    if (fizz == 0):
        msg = "Fizz"
    if(buzz == 0):
        msg = "Buzz"
    if (fizz == 0 and buzz == 0):
        msg = "FizzBuzz"
    if (fizz == 0):
        return True
    elif(buzz ==0):
        return True
    else:
        return False
    
def fizzBuzz(n):
    n = n+1
    for i in range(n):
        if i == 0:
            pass
        else:
            test = test_case(i)
            if test:
                print(msg)
            else:
                print(i)
            

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
