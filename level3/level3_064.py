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

def process_left(E, L, V, E_sum):
    if E[L-2] >= 0: # E[L-2]が正->A[i]>A[i-1]
        E[L-2] += V
        E_sum += V
    else: # E[L-2]が負->A[i]<A[i-1]
        E_sum -= abs(E[L-2])
        E[L-2] += V
        E_sum += abs(E[L-2])
    return E_sum, E

def process_right(E, R, V, E_sum):
    if E[R-1] > 0:
        E_sum -= abs(E[R-1])
        E[R-1] -= V
        E_sum += abs(E[R-1])
    else:
        E[R-1] -= V
        E_sum += V
    return E_sum, E

def main():
    # sys.stdin = open("input.txt", "r")
    N, Q = i_map()
    A = i_list()

    # 複雑に考えすぎて、論理のところをややこしくしてしまい、自力では解けなかったため、回答を写した
    E = []
    ans = 0
    for i in range(N-1):
        E.append(A[i+1]-A[i])
        ans += abs(E[i])

    for i in range(Q):
        L, R, V = i_map()
        if L > 1:
            L -= 2
            ans -= abs(E[L])
            E[L] += V
            ans += abs(E[L])
        if R < N:
            R -= 1
            ans -= abs(E[R])
            E[R] -= V
            ans += abs(E[R])
        print(ans)

if __name__ == '__main__':
    main()
