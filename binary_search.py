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

###