import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, comb, lcm
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

def main():
    # sys.stdin = open("input.txt", "r")
    N = i_input()
    A = i_list()
    B = i_list()
    C = i_list()

    A_dict = {key:0 for key in range(46)}
    B_dict = {key:0 for key in range(46)}
    C_dict = {key:0 for key in range(46)}
    for a in A:
        A_dict[a%46] += 1
    for b in B:
        B_dict[b%46] += 1
    for c in C:
        C_dict[c%46] += 1

    ans = 0
    for a_key, a_value in A_dict.items():
        for b_key, b_value in B_dict.items():
            for c_key, c_value in C_dict.items():
                if (a_key+b_key+c_key) % 46 == 0:
                    ans += a_value * b_value * c_value
    print(ans)

if __name__ == '__main__':
    main()
