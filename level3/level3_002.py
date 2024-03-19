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

def hantei(candidate):
    if candidate.count("(") == candidate.count(")"):
        count = 0
        for s in candidate:
            if s == "(": count += 1
            else: count -= 1
            if count < 0: return False

        return True

def main():
    # sys.stdin = open("input.txt", "r")
    N = i_input()

    for i in range(2**N):
        candidate = ""
        for j in range(N):
            if (i&(1<<j)) == 0: candidate += "("
            else: candidate += ")"
        if hantei(candidate): print(candidate)
if __name__ == '__main__':
    main()

