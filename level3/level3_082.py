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

# 模範解答用の関数。自分の回答では使ってない
def count_number(number: int) -> int:
    digit, cnt = 1, 0
    while True:
        under = 10**(digit-1)-1
        top = min(under, 10**digit-1)
        cnt += ((top*(top+1)-under*(under+1))//2) * digit

        if number <= 10 ** digit-1:
            return cnt
        digit += 1

def main():
    # sys.stdin = open("input.txt", "r")
    L, R = i_map()
    L_keta = len(str(L))
    R_keta = len(str(R))
    if L_keta == R_keta:
        sum = (L+R) * (R-L+1)//2%MOD*L_keta%MOD
        print(sum)
    else:
        ans = 0
        L_max = 10**(L_keta)-1
        ans += (L + L_max) * (L_max-L+1)//2%MOD*L_keta%MOD
        R_min = 10**(R_keta-1)
        ans += (R_min + R) * (R-R_min+1)//2%MOD*R_keta%MOD

        keta_diff = R_keta - L_keta
        # 桁数の差が1の時はこれで終わり
        if keta_diff == 1:
            print(ans%MOD)
        else:
            for i in range(1, keta_diff):
                mid_min = 10**(L_keta+i-1)
                mid_max = 10**(L_keta+i)-1
                ans += (mid_max+mid_min) * (mid_max-mid_min+1)//2%MOD*(L_keta+i)%MOD
            print(ans%MOD)

    # 模範回答。参考として。
    # print((count_number(R) - count_number(L-1))%MOD)



if __name__ == '__main__':
    main()
