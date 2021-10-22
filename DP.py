# DP 문제들 목록

# def BOJ2193(): # 이친수 (https://www.acmicpc.net/problem/2193)
    # # 1. 1로 시작해야 한다.
    # # 2. 1이 연속으로 나타나지 않는다.
    # # 첫 두자리는 아마도 10 으로 고정될 듯?
    # n = int(input())

    # dp = [[0]*2 for _ in range(n+1)]
    # dp[1][0] = 0
    # dp[1][1] = 1
    # for i in range(2,n+1):
    #     dp[i][0] = dp[i-1][1] + dp[i-1][0]
    #     dp[i][1] = dp[i-1][0]
    # answer = dp[n][0] + dp[n][1]

    # print(answer)

    # return
# BOJ2193()