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

# def BOJ12865_2(): # 평범한 배낭 - DP

    # 표를 그리게 되는 경우가 많다.
    # 주의할 건, 표를 그리고 유추를 하는데 정확한 - 논리적이고 합리적인 관계식을 찾아야 한다.
    # 그냥 추측으로 때려 맞추면 안된다.

    # import sys

    # n, k= map(int, input().split())
    # dp = [[0]*(k+1) for _ in range(n+1)]

    # w,v = [0], [0]
    # for i in range(1,n+1):
    #     a,b = map(int, sys.stdin.readline().split())
    #     w.append(a)
    #     v.append(b)
    #     for j in range(1, k+1):
    #         if j >= w[i]:
    #             dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # print(dp[-1][-1])
# BOJ12865_2()

# def BOJ12865_3(): # 평범한 배낭 - 더 단순한 DP
    # import sys
    # input = sys.stdin.readline

    # n,k = map(int, input().split())
    # ary = [list(map(int, input().split())) for _ in range(n)]

    # dp = [0]*(k+1)
    # ary.sort()
    # for weight, val in ary:
    #     for j in range(k, weight-1,-1):
    #         dp[j] = max(dp[j], dp[j-weight] + val)

    # print(dp[k])
# BOJ12865_3()

# def BOJ9252(): # LCS 2 (https://www.acmicpc.net/problem/9252)
    # a = input()
    # b = input()
    # dp = [[0 for col in range(len(b)+1)]for row in range(len(a)+1)]

    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if a[i] == b[j]:
    #             dp[i+1][j+1] = dp[i][j] + 1
    #         else:
    #             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])   ## 점화식으로 dp 채우기

    # answer_1 = dp[-1][-1]

    # answer_2 = '' # 공통문자를 역순으로 저장하는 문자열
    # r,c = len(a), len(b) # 공통문자를 탐색하기위한 좌표 r : 행,  c : 열 
    # while dp[r][c] != 0:
    #     if dp[r-1][c] == dp[r][c]:
    #         r -= 1
    #     elif dp[r][c-1] == dp[r][c]:
    #         c -= 1
    #     else:
    #         answer_2 += a[r-1]  # 또는 b[c-1] 
    #         r,c = r-1, c-1

    # print(answer_1)
    # print(answer_2[::-1])
# BOJ9252

# def BOJ10942(): # 펠린드롬? (https://www.acmicpc.net/problem/10942)
    # import sys

    # n = int(input())
    # nums = list(map(int, sys.stdin.readline().split()))

    # dp = [[False]*n for _ in range(n)]

    # # fill dp
    # for i in range(n):
    #         dp[i][i] = True     # 길이가 1인 경우 palindrome 이 맞다(True)

    # for i in range(2, n+1): # 길이가 2 ~ n 인 경우에 대해 (n+1 포함 x)
    #     for j in range(n-i+1):
    #         if nums[j] == nums[j+i-1]:
    #             if i == 2:      # 길이가 2인경우, 두 숫자가 같으면 palindrome
    #                 dp[j][j+i-1] = True
    #             elif dp[j+1][j+i-2] == True:  # 그 중간이 palindrome 인지 확인
    #                 dp[j][j+i-1] = True

    # m = int(input())
    # for _ in range(m):
    #     s, e = map(int, sys.stdin.readline().split())
    #     s, e = s-1, e-1
    #     print(int(dp[s][e]))
# BOJ10942()

# def BOJ11057(): # 오르막 수 (https://www.acmicpc.net/problem/11057)
    # n = int(input())
    # dp = [[1]*10]
    # for i in range(1,n):
    #     dp.append([0]*10)
    #     for j in range(10):
    #         dp[i][j] = dp[i][j-1] + dp[i-1][j]

    # print(sum(dp[n-1])%10007)
# BOJ11057()

# def BOJ5557(): # 1학년 (https://www.acmicpc.net/problem/5557)
    # import sys

    # n = int(input())
    # nums = list(map(int,sys.stdin.readline().split()))

    # start = nums[0]
    # target = nums[-1]

    # dp=[[0]*21 for _ in range(n)]

    # dp[0][start] = 1    # dp 원소의 의미 : 수식의 답(열)이 해당 행과 같은 경우의 수. 즉 마지막 행, 열이 입력의 마지막 수(등식의 우변) 인 원소를 반환하면 된다. 
    # for i in range(1,n-1):
    #     for j in range(21):         # 20 포함
    #         if dp[i-1][j]:
    #             if j + nums[i] <= 20 : dp[i][j + nums[i]] += dp[i-1][j]
    #             if j - nums[i] >= 0 : dp[i][j - nums[i]] += dp[i-1][j]

    # print(dp[n-2][target])
    # return
# BOJ5557()

#### 재귀함수 문제
# def BOJ17478(): # 재귀함수가 뭔가요? (https://www.acmicpc.net/problem/17478)
    # n = int(input())
    # output = ['어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.',
    #             '"재귀함수가 뭔가요?"',
    #             '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    #             '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
    #             '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',
    #             '"재귀함수는 자기 자신을 호출하는 함수라네"',
    #             '라고 답변하였지.']
    # def f(depth):
    #     if depth == 0:
    #         print('____'*(n-depth)+output[1])
    #         print('____'*(n-depth)+output[5])
    #         print('____'*(n-depth)+output[-1])
    #         return
    #     else:
    #         for i in output[1:-2]:
    #             print('____'*(n-depth)+i)
    #         f(depth-1)
    #     print('____'*(n-depth)+output[-1])
    
    # print(output[0])
    # f(n)
# BOJ17478()

# def BOJ14501():	# 퇴사 (https://www.acmicpc.net/problem/14501)
# 	import sys

# 	input = sys.stdin.readline
# 	n = int(input().strip())
# 	t, p = zip([0, 0], *[list(map(int, input().split())) for _ in range(n)])
# 	# print(t)
# 	# print(p)
# 	dp = [[0] * (n + 1) for _ in range(n + 1)]
# 	for i in range(1, n + 1):
# 		for j in range(1, n + 1):
# 			if (j == t[i] + i - 1): 
# 				if (i - 1 + t[i] <= i): dp[i][j] = dp[i - 1][j] + p[i]
# 				else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# 			else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# 	for i in dp:
# 		for j in i:
# 			print(j, end = " ")
# 		print()
# 	print(dp[-1][-1])
# BOJ14501()