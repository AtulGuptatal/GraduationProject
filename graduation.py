def ceremony_probability():
    N = int(input())
    dp = [[0] * N for _ in range(4)]
    dp[0][0], dp[1][0], dp[2][0], dp[3][0] = 1, 1, 1, 1

    for i in range(1, N):
        dp[3][i] = dp[1][i - 1] + dp[0][i - 1]
        dp[2][i] = dp[2][i - 1] + dp[1][i - 1]
        dp[1][i] = dp[3][i - 1] + dp[2][i - 1]
        dp[0][i] = dp[3][i - 1]

    present, absent = dp[2][-1], dp[1][-1]
    total = present + absent

    print(total)
    print('{}/{}'.format(absent, total))
