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
    N, L = i_map()

    mod = 10**9+7
    # 模範回答：DPを使って、答えをだす。
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(1, N+1):
        if i < L: dp[i] = dp[i-1]
        else: dp[i] = (dp[i-1]+dp[i-L]) % mod
    print(dp[N])

    # 自分の回答:場合分けして、各場合の組み合わせの数を計算していく
    # fact = [1]*(N+1)
    # for i in range(1, N+1):
    #     fact[i] = fact[i-1]*i% mod

    # ans = 0
    # for i in range(N//L+1): # Lが0回からL_max回までの全ての場合を確認する
    #     rest = N - L*i

    #     ans += fact[rest + i] * pow(fact[rest], mod-2, mod) * pow(fact[i], mod-2, mod)
    #     ans %= mod
    # print(ans)





if __name__ == '__main__':
    main()
