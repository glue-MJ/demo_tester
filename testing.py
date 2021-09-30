from typing import Union
import math
from numba import jit

def factorial(i: int):
    summation = 1
    for num in range(1, i+1):
        summation *= num
    return summation

def main():
    print(factorial(10))

if __name__ == '__main__':
    main()