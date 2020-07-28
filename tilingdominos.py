while True:
    n = int(input())
    if n == -1:
        break
    dp = [[0] * 8 for i in range(n + 1)]

    dp[0][7] = 1

    for i in range(n):
        dp[i + 1][0] += dp[i][7]

        dp[i + 1][1] += dp[i][6]

        dp[i + 1][2] += dp[i][5]

        dp[i + 1][3] += dp[i][7]
        dp[i + 1][3] += dp[i][4]

        dp[i + 1][4] += dp[i][3]

        dp[i + 1][5] += dp[i][2]

        dp[i + 1][6] += dp[i][1]
        dp[i + 1][6] += dp[i][7]

        dp[i + 1][7] += dp[i][0]
        dp[i + 1][7] += dp[i][6]
        dp[i + 1][7] += dp[i][3]

    print(dp[n][7])
