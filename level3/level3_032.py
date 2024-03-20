import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, comb
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
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
    A = i_row_list(N)
    M = i_input()
    X_Y = i_row_list(M)

    players = [i for i in range(N)]
    ans_list = []
    invalid_pairs = set()
    for x, y in X_Y:
        invalid_pairs.add((x-1, y-1))
        invalid_pairs.add((y-1, x-1))

    for comb in permutations(players):
        ans_candidate = 0
        flag = True
        for i in range(1, len(comb)):
            if (comb[i-1], comb[i]) in invalid_pairs:
                flag = False
                break
            ans_candidate += A[comb[i]][i]
        if flag:
            ans_candidate += A[comb[0]][0]
            ans_list.append(ans_candidate)

    if len(ans_list) == 0: print(-1)
    else: print(min(ans_list))


if __name__ == '__main__':
    main()
