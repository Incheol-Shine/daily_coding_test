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

# def BOJ1351(): # 무한 수열 (https://www.acmicpc.net/problem/1351)
    # n, p, q = map(int, input().split())
    # global dp
    # dp = {0:1}

    # def f(num):
    #     global dp

    #     if num in dp: return dp[num]
    #     else: 
    #         dp[num] = f(num//p) + f(num//q)
    #         return dp[num]
    # print(f(n))
    # return
# BOJ1351()

# def BOJ16493(): # 최대 페이지 수 (https://www.acmicpc.net/problem/16493)
    # import sys
    # n,m = map(int, sys.stdin.readline().split())
    # info = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(m)] # 일, 페이지 1부터 시작

    # dp = [[0]*(n+1) for _ in range(m+1)]  # 행: m 개 챕터,  열: n 일
    # for chapter in range(1,m+1):
    #     for day in range(1,n+1):
    #         if day-info[chapter][0] >= 0:
    #             dp[chapter][day] = max(dp[chapter-1][day], info[chapter][1]+dp[chapter-1][day-info[chapter][0]]) 
    #         else:
    #             dp[chapter][day] = dp[chapter-1][day]
# BOJ16493()

# def BOJ1516(): # 게임개발 (위상정렬?) (https://www.acmicpc.net/problem/1516)
    # import sys
    # from collections import defaultdict

    # dic = defaultdict(list)

    # n = int(input())
    # dp = [-1]*(n+1)
    # times  = [0]            # 건물을 짓는데 걸리는 시간들

    # for i in range(1,n+1):
    #     time, *building = map(int,sys.stdin.readline().split())
    #     times.append(time)
    #     dic[i] = building


    # def find_dp(i):
    #     if dp[i] != -1: return dp[i]
        
    #     maximum = 0
    #     for x in dic[i]:
    #         if x == -1 : break
    #         if dp[x] == -1:
    #             dp[x] = find_dp(x)

    #         maximum = max(maximum, dp[x])

    #     dp[i] = times[i] + maximum
    #     return dp[i]

    # for i in range(1,n+1):
    #     if -1 not in dp[1:]: break
    #     find_dp(i)

    # for i in dp[1:]:
    #     print(i)
# BOJ1516()

# def BOJ12865(): # 평범한 배낭- 완전탐색 (https://www.acmicpc.net/problem/12865)
    # import sys
    # 완전탐색 - 비트연산을 이용해 모든 부분집합을 구해 탐색
    # n,k = map(int, sys.stdin.readline().split())
    # wandv=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # answer = 0
    # for i in range(1<<n):
    #     cnt, value = 0, 0
    #     for j in range(n):
    #         if i & 1<<j:
    #             cnt += wandv[j][0]
    #             value += wandv[j][1]
    #         if cnt > k: break
    #     else:
    #         answer = max(answer,value)
    # print(answer)
# BOJ12865()

# def BOJ9251(): # LCS (https://www.acmicpc.net/problem/9251)
    # import sys

    # word1 = ' '+sys.stdin.readline().strip()
    # word2 = ' '+sys.stdin.readline().strip()

    # # word1 을 열방향, word2 를 행방향
    # dp = [[0]*(len(word1)) for _ in range(len(word2))]
    # for i in range(1, len(word2)):
    #     for j in range(1, len(word1)):
    #         if word2[i] == word1[j]:
    #             dp[i][j] = dp[i-1][j-1] + 1
    #         else:
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # print(dp[-1][-1])
# BOJ9251()