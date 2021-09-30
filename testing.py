from typing import Union
import math
from numba import jit

def factorial(i: int):
    summation = 1
    for num in range(1, i+1):
        summation *= num
    return summation

@jit(nopython=True)
def createarray(i: int):
    lst = []
    for _ in range(i):
        # lst += [0]
        # lst = lst[:-1]
        lst.append(0)
        lst.pop()
    print(lst)

def main():
    import time

    start = time.time()

    createarray(15_000_000)

    end = time.time()

    print(end - start)

if __name__ == '__main__':
    main()