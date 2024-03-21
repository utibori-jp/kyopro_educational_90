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
    N, K = i_map()
    A_B = i_row_list(N)
    A_B.sort(key=lambda x:x[1])

    B_score = [row[1] for row in A_B]
    diff_A_B = [row[0] - row[1] for row in A_B]
    add_score = B_score + diff_A_B
    add_score.sort()
    ans = sum(elem for elem in add_score[-K:])
    print(ans)

    # DPせっかく組んだので、TLEしたけど、勿体無いから残しとく
    # dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    # dp[0][0] = 0
    # for i in range(1, N+1):
    #     perfect_score, partial_score = A_B[i-1]
    #     for j in range(1, K+1):
    #         dp[i][j] = dp[i-1][j] # i問目の問題を解かない時

    #         # i問目で部分点を取る場合
    #         dp[i][j] = max(dp[i][j], dp[i-1][j-1]+partial_score)
    #         # i問目で満点を取る場合
    #         if j >= 2:
    #             dp[i][j] = max(dp[i][j], dp[i-1][j-2]+perfect_score)
    # print(dp[N][K])



if __name__ == '__main__':
    main()
