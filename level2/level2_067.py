import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_list_by_one_string(): return [int(x) for x in input()]
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def convert_8_9(N: int) -> int:
    N_10 = int(str(N), 8)
    N_9 = ""
    while N_10 > 0:
        N_9 = str(N_10%9) + N_9
        N_10 = N_10//9
    return int(N_9)

def convert_9_8(N: int) -> int:
    N_10 = int(str(N), 9)
    N_8 = ""
    while N_10 > 0:
        N_8 = str(N_10%8) + N_8
        N_10 = N_10//8
    return int(N_8)

def replace_8(N_9: int) -> int:
    N_9_replaced = str(N_9).replace('8', '5')
    return int(N_9_replaced)

def main():
    # sys.stdin = open("input.txt", "r")
    N, K = i_map()

    if N == 0:
        print(0)
    else:
        for i in range(K):
            N_9 = convert_8_9(N)
            N = replace_8(N_9)
        print(N)



if __name__ == '__main__':
    main()

