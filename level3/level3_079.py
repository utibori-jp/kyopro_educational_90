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

def check_last_mass(matrix):
    H = len(matrix)
    W = len(matrix[0])
    flag =  matrix[H-1][W-1] == matrix[H-2][W-1] and matrix[H-1][W-1] == matrix[H-1][W-2] and matrix[H-1][W-1] == matrix[H-2][W-2]
    return flag

def main():
    # sys.stdin = open("input.txt", "r")
    H, W = i_map()
    A_matrix = i_row_list(H)
    B_matrix = i_row_list(H)

    A_sum = 0
    B_sum = 0
    for i in range(H):
        for j in range(W):
            B_matrix[i][j] -= A_matrix[i][j]

    cnt = 0
    for i in range(H-1):
        for j in range(W-1):
            diff = B_matrix[i][j]
            if j == W-2 and i == H-2: # 一番下のますに来たら4マス全て確認
                if check_last_mass(B_matrix):
                    print("Yes")
                    print(cnt+abs(diff))
                    return
                else:
                    print("No")
                    return
            if i == H-2 and B_matrix[i][j] != B_matrix[i+1][j]: # 一番端のマスに来たら上のマスどちらも確認
                print("No")
                return
            if j == W-2 and B_matrix[i][j] != B_matrix[i][j+1]: # 一番下のマスに来たら、下のマスどちらも確認
                print("No")
                return

            B_matrix[i][j] -= diff
            B_matrix[i+1][j] -= diff
            B_matrix[i][j+1] -= diff
            B_matrix[i+1][j+1] -= diff
            cnt += abs(diff)

if __name__ == '__main__':
    main()
