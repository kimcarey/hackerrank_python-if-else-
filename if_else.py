import math
import os
import random
import re
import sys

n = random.randint(1, 101)

def weird_or_not(n):
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and (2 <= n <= 5):
        print("Not Weird")
    elif n % 2 == 0 and (6 <= n <= 20):
        print("Weird")
    elif n % 2 == 0 and (n > 20):
        print("Not Weird")


if __name__ == '__main__':
    weird_or_not(n = int(input().strip()))