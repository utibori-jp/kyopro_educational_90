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

def main():
    sys.stdin = open("input.txt", "r")
    N = i_input()
    C_P = i_row_list(N)
    Q = i_input()
    L_R = i_row_list(Q)

    comulative_sum_1 = [0] * (N+1)
    comulative_sum_2 = [0] * (N+1)
    for i in range(N):
        comulative_sum_1[i+1] = comulative_sum_1[i] + (C_P[i][1] if C_P[i][0] == 1 else 0)
        comulative_sum_2[i+1] = comulative_sum_2[i] + (C_P[i][1] if C_P[i][0] == 2 else 0)

    for l, r in L_R:
        ans_1 = comulative_sum_1[r] - comulative_sum_1[l-1]
        ans_2 = comulative_sum_2[r] - comulative_sum_2[l-1]
        print(ans_1, ans_2)

if __name__ == '__main__':
    main()

