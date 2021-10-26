# 구현 문제들 목록

# def BOJ3085(): # 사탕게임 (https://www.acmicpc.net/problem/3085)
    # import sys
    # from copy import deepcopy
    # n = int(input())
    # board = [list(sys.stdin.readline().strip()) for _ in range(n)]

    # # 1. 가장 긴 행 or 열 길이 구하기
    # def max_candy(matrix):
    #     answer = 0
    #     for i in matrix:
    #         length = 0
    #         initial = i[0]
    #         for j in i:
    #             if j == initial:
    #                 length += 1
    #             else:
    #                 initial = j
    #                 length = 1
    #             answer = max(answer, length)
    #     return answer
    
    # def find_max_candy(matrix):
    #     return max(max_candy(matrix), max_candy(list(zip(*matrix))))
        
    # answer = 0

    # for i in range(len(board)):
    #     for j in range(len(board)-1):
    #         if board[i][j] != board[i][j+1]:
    #             new_board = deepcopy(board)
    #             new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    #             answer = max(answer, find_max_candy(new_board))
    
    # for j in range(len(board)):
    #     for i in range(len(board)-1):
    #         if board[i][j] != board[i+1][j]:
    #             new_board = deepcopy(board)
    #             new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
    #             answer = max(answer, find_max_candy(new_board))

    # print(answer)

    # return
# BOJ3085()

# def BOJ22114(): # 창영이와 점프 (https://www.acmicpc.net/problem/22114)
    # ### Solution 1
    # import sys

    # n, k = map(int, input().split())
    # width = list(map(int, sys.stdin.readline().split()))  # 문제에서 주어진 돌 사이 간격

    # # bound : k 보다 큰 간격들의 index 를 저장한다. 맨 처음, 맨 마지막 index 를 포함한다. ex) if width == 2 3 1 5 3 5 : bound = [-1, 3, 5, 6]
    # bound = [-1]
    # bound.extend([i for i in range(len(width)) if width[i] > k])
    # bound.append(len(width))
    
    # # bound 사이 간격을 저장한다. ex) if bound == [-1, 3, 5, 6] : blocks = [4,2,1]
    
    # blocks = []
    # for i in range(1, len(bound)):
    #     blocks.append(bound[i]-bound[i-1])
    # answer = 0
    # if len(blocks) == 1: answer = blocks[0]
    # else:
    #     # blocks 의 인접한 두 숫자의 합 중 최댓값을 정답으로 출력한다.
    #     for i in range(len(blocks)-1):
    #         answer = max(answer, blocks[i]+blocks[i+1])

    # print(answer)
    
    # return
# BOJ22114()

# def BOJ13335(): # 트럭 (https://www.acmicpc.net/problem/13335)

    # import sys
    # from collections import deque

    # n,w,L = map(int, sys.stdin.readline().split())
    # trucks = deque(map(int, sys.stdin.readline().split()))

    # u = 0
    # total_weight = 0
    # bridge = deque([[False,0]]*w)
    # # print(bridge)
    # while True:
    #     is_last, weight = bridge.popleft()
    #     total_weight -= weight

    #     if len(trucks) != 0 and total_weight + trucks[0] <= L:
    #         truck = trucks.popleft()
    #         flag = False if len(trucks) != 0 else True
    #         bridge.append([flag, truck])
    #         total_weight += truck
    #     else:
    #         bridge.append([False,0])

    #     u += 1
    #     # print(u,bridge,trucks)
    #     if is_last == True: break
    # print(u)
# BOJ13335()