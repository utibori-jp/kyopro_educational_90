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
    # sys.stdin = open("input.txt", "r")
    N = i_input()
    A = i_list()
    Q = i_input()
    B = i_row(Q)
    A.sort()

    # b < Aを満たす最小のAを探す.
    # right: b <= Aを満たす最小のAのインデックス
    # left: b > Aを満たす最大のAのインデックス
    for b in B:
        right = N+1
        left = 0
        if b < A[0]: # Aの最小値より、ｂが小さい時
            print(A[0]-b)
        elif b > A[N-1]: # Aの最大値より、ｂが大きい時
            print(b-A[N-1])
        else: # ｂがAの要素の最大から最小の範囲に収まっているとき
            while right-left > 1:
                mid = (right + left) // 2
                if b > A[mid]: left = mid
                else: right = mid
            A_left = b-A[left]
            A_right = A[right]-b
            print(min(A_left, A_right))
    # b > Aを満たす最大のAを探す.

if __name__ == '__main__':
    main()

