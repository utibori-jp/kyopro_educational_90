import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, atan2, degrees, radians, sin, cos
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

def angle(X, Y, x, y, z):
    leng_X = X-x
    leng_Y = Y-y
    XY = (leng_X**2+leng_Y**2)**(1/2)
    radian = atan2(z, XY)
    return degrees(radian)

def main():
    sys.stdin = open("input.txt", "r")
    T = i_input()
    L, X, Y = i_map()
    Q = i_input()
    E = i_row(Q)
    print(T, L, X, Y, Q, E)

    for e in E:
        degree = 360*e/T
        theta = radians(degree)
        y, z = -L/2*sin(theta), L/2-L/2*cos(theta)
        print(angle(X, Y, 0, y, z))



if __name__ == '__main__':
    main()

