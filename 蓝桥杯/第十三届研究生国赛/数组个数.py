import os
import sys
from collections import Counter

def count_valid_arrays(n, B):
    MOD = 1_000_000_007

    # 初始化 dp 表，用于动态规划
    # dp[i][j] 表示第 i 个位置为 j 时的合法数组数量
    dp = [[0] * 101 for _ in range(2)]

    # 初始化第一个位置的 dp
    for a0 in range(101):
        if max(a0, 0, 0) == B[0]:
            dp[0][a0] = 1

    # 动态规划计算每个位置
    for i in range(1, n):
        for ai in range(101):
            dp[i % 2][ai] = 0  # 清空当前行的 dp

            for ai_minus_1 in range(101):
                if i == n - 1:  # 最后一个元素
                    if max(ai_minus_1, ai, 0) == B[i]:
                        dp[i % 2][ai] += dp[(i - 1) % 2][ai_minus_1]
                        dp[i % 2][ai] %= MOD
                else:  # 中间的元素
                    if max(ai_minus_1, ai, ai + 1) == B[i]:
                        dp[i % 2][ai] += dp[(i - 1) % 2][ai_minus_1]
                        dp[i % 2][ai] %= MOD

    # 累加最后一行的结果
    return sum(dp[(n - 1) % 2]) % MOD


def main():

    n = int(input())
    B = list(map(int, input().split()))
    # 输出结果
    print(count_valid_arrays(n, B))


if __name__ == "__main__":
    main()



