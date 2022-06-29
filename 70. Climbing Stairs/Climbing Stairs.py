def climbStairs(self, n: int) -> int:
    # dp[] => the memoization array for nth stairs
    # fibonacci series is used in this question
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]