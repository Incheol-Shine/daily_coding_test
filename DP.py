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

# def BOJ11660(): # 구간 합 구하기 5 (https://www.acmicpc.net/problem/11660)
    # import sys

    # n, m = map(int, input().split())
    # table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # # (0,0) 기준 구간합 구하기
    # for i in range(n):
    #     for j in range(1,n):
    #         table[i][j] += table[i][j-1]
    
    # for i in range(1,n):
    #     for j in range(n):
    #         table[i][j] += table[i-1][j]

    # def section_sum(*coordination):
    #     x1,y1,x2,y2 = coordination
    #     x0 = table[x1-1][y2] if x1>=1 else 0
    #     y0 = table[x2][y1-1] if y1>=1 else 0
    #     xy0 = table[x1-1][y1-1] if x1>=1 and y1>=1 else 0
    #     answer = table[x2][y2] - y0 - x0 + xy0
    #     print(answer)
    #     return

    # for _ in range(m):
    #     x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    #     section_sum(x1-1,y1-1,x2-1,y2-1) # index 로 맞춰주기 위해 1을 뺌
    
    # return
# BOJ11660()