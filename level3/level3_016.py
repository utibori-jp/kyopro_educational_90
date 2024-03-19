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
    A, B, C = sorted(i_list()) # A < B < C
    ans_candidate = []
    for i in reversed(range(N//C+1)):
        res = N-C*i
        ans_C = i
        flag = True
        if res == 0: # Cのコインのみでちょうど払える->絶対これ最小だからループをやめていい。
            ans_candidate.append(ans_C)
            flag = False
            break
        elif res >= B: # Cのコインのみでちょうどは払えない。かつ、Bのコインで払う余地がある。
            for j in reversed(range(res//B+1)):
                res_B = res - B*j
                ans_B = ans_C + j
                # Bのみ、またはBとCでちょうど払える組み合わせが出るまで探す。出るか全ての組み合わせを確認したらループは終了
                if res_B == 0: # BとCのコインでちょうどならここで終了
                    ans_candidate.append(ans_B)
                    break
                elif res_B % A == 0: # AとBとCのコインでちょうどならここで終了。それ以外ならループを最初からやり直す。
                    ans_candidate.append(ans_B + res_B//A)
                    break
        elif res >= A and res % A ==0: # CとAのみでちょうど払える
            ans_candidate.append(ans_C + res//A)

    if N%A == 0:
        ans_candidate.append(N//A)
    print(min(ans_candidate))



if __name__ == '__main__':
    main()

