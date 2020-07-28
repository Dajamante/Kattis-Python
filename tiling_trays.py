n = int(input())

dp = [[0] * 8 for i in range(n + 1)]

dp[0][7] = 1

for i in range(n):
    dp[i + 1][0] += dp[i][7]

    dp[i + 1][1] += dp[i][7]  # either full column in i (small tray) or binary 6 (long tray)
    dp[i + 1][1] += dp[i][6]

    dp[i + 1][2] += dp[i][5]
    dp[i + 1][2] += dp[i][7]

    dp[i + 1][3] += dp[i][4]
    dp[i + 1][3] += dp[i][5]
    dp[i + 1][3] += dp[i][6]
    dp[i + 1][3] += dp[i][7] * 2  # one long or two small to create state 3 from state 7 in i

    dp[i + 1][4] += dp[i][3]
    dp[i + 1][4] += dp[i][7]

    dp[i + 1][5] += dp[i][2]
    dp[i + 1][5] += dp[i][6]
    dp[i + 1][5] += dp[i][3]
    dp[i + 1][5] += dp[i][7]

    dp[i + 1][6] += dp[i][7] * 2
    dp[i + 1][6] += dp[i][1]
    dp[i + 1][6] += dp[i][2]
    dp[i + 1][6] += dp[i][3]
    dp[i + 1][6] += dp[i][4]
    dp[i + 1][6] += dp[i][5]

    dp[i + 1][7] += dp[i][0]
    dp[i + 1][7] += dp[i][7] * 3
    dp[i + 1][7] += dp[i][3] * 2
    dp[i + 1][7] += dp[i][6] * 2
    dp[i + 1][7] += dp[i][5]

    # i was empty, or was not, and then we can have 3 small, one small one long, one long one small

    print(dp[n][7])
