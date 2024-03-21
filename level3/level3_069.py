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

def mod_pow(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x %mod
        x = x*x%mod
        n //= 2
    return result

def main():
    # sys.stdin = open("input.txt", "r")
    N, K = i_map()
    mod = 10**9+7
    k = K%mod
    if N == 1:
        print(k)
    elif N == 2:
        if K == 1: print(0)
        else:
            ans = (k*(k-1))%mod
            print(ans)
    elif K <= 2: print(0)
    else:
        ans = (k * (k-1)) % mod
        ans = ans * mod_pow(k-2, N-2, mod)%mod
        print(ans)

    # 以下模範解答　条件分岐はn==1のみでよかった。条件分岐を手当たり次第に書くのではなく、重複は整理する習慣をつける
    # n, k = map(int,input().split())
    # mod = 10 ** 9 + 7
    # if n == 1:
    #     print(k)
    # else:
    #     ans = k * (k - 1) * pow(k - 2, n - 2, mod)
    #     print(ans % mod)



if __name__ == '__main__':
    main()
