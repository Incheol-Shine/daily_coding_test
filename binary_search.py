# 이분 탐색 문제들 목록

### 투 포인터

# def BOJ3649(): # 로봇 프로젝트(https://www.acmicpc.net/problem/3649)
    # import sys

    # while True:
    #     line = sys.stdin.readline().strip()
    #     if line == '': break
        
    #     width = int(line) * 10000000
    #     n = int(sys.stdin.readline().strip())
    #     L = [int(sys.stdin.readline().strip()) for _ in range(n)]
    #     L_sort = sorted(L)

    #     left = 0
    #     right = len(L_sort)-1

    #     while left < right:
    #         if L_sort[left] + L_sort[right] < width:
    #             left += 1
    #         elif L_sort[left] + L_sort[right] > width:
    #             right -= 1
    #         else :
    #             print('yes',L_sort[left], L_sort[right])
    #             break
    #     else:
    #         print('danger')
# BOJ3649()

# def BOJ17609(): # 회문(https://www.acmicpc.net/problem/17609)
    # import sys

    # def f(i,j,flag):
        
    #     while i<=j:
    #         if word[i] == word[j]:
    #             i += 1
    #             j -= 1
    #         elif word[i] != word[j] and flag == False:
    #             a = f(i+1,j,True)
    #             b = f(i,j-1,True)

    #             if a!=2 or b!=2:
    #                 return 1
    #             else:
    #                 return 2

    #         else: return 2
        
    #     if flag == False: return 0
    #     else: return 1

    # t = int(input())

    # for _ in range(t):
    #     word = sys.stdin.readline().strip()

    #     i = 0
    #     j = len(word)-1
    #     flag = False # 한 문자 삭제 여부
    #     print(f(i,j,flag))
# BOJ17609()

###