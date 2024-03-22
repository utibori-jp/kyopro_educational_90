import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, comb, lcm
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from bisect import bisect_left
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
    A = i_list()
    A.insert(0, 0)

    B = [0] * (2*N+1)
    for i in range(1, N+1):
        B[i] = B[i-1]+A[i]
    for i in range(1, N+1):
        B[i+N] = B[i+N-1]+A[i]

    if B[N] % 10 != 0:
        print("No")
        return

    for i in range(N+1):
        goal = B[i] + B[N]//10
        pos = bisect_left(B, goal, 0, 2*N+1) # B＜＝Goalを満たす、最大のBのインデックスを返す
        if pos <= 2*N and B[pos] == goal: # B[pos]＝＝Goalか確認する。
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
