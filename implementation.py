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

def BOJ12731(): # 열차 시간표(small) (https://www.acmicpc.net/problem/12731)
    import sys

    def hToM(hhmm):
        hh, mm = list(map(int,hhmm.split(':')))
        return hh*60 + mm

    # 정렬 알고리즘. 
    # 숫자가 작을수록 뒤에 (내림차순)
    # 숫자가 같으면 알파벳 순으로 (flag = True 이면 내림차순 (b,a) , False 이면 오름차순 (a,b))
    def quick_sort(arr,flag): # arr = [[val, alpha]]
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2][0]
        lesser_arr, equal_arr, greater_arr = [], [], []
        for num in arr:
            if num[0] < pivot:
                lesser_arr.append(num)
            elif num[0] > pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
        return quick_sort(greater_arr,flag) + sorted(equal_arr, key=lambda x: x[1], reverse=flag) + quick_sort(lesser_arr,flag)

    n = int(input())
    for i in range(n):
        t = int(sys.stdin.readline().strip())
        na, nb = map(int, sys.stdin.readline().split())
        
        a_station = [] # b 에서 온 열차 도착시간 + t, a 에서 출발하는 열차 출발시간
        b_station = [] # a 에서 온 열차 도착시간 + t, b 에서 출발하는 열차 출발시간
        for _ in range(na):
            start, end = map(hToM, sys.stdin.readline().split())
            a_station.append([start, 'a'])
            b_station.append([end+t, 'a'])

        # 두가지 방법으로 정렬하려고 하는데 어떤 자료구조를 사용해야 할까?
        for _ in range(nb):
            start, end = map(hToM, sys.stdin.readline().split())
            a_station.append([end+t, 'b'])
            b_station.append([start, 'b'])

        a_station = quick_sort(a_station,False)
        b_station = quick_sort(b_station,True)

        old, new = 0,0
        answer_na, answer_nb = na, nb
        # print(a_station,b_station)

        for _ in range(len(a_station)):
            new = a_station.pop()[1]
            if old == 'b' and new == 'a': answer_na -= 1 # a 역에서는 b에서 출발한 열차가 도착후, a 역에서 출발하는 열차가 있는경우, 열차개수 1개 차감.
            old = new
        for _ in range(len(b_station)):
            new = b_station.pop()[1]
            if old == 'a' and new == 'b': answer_nb -= 1 # b 역에서는 a에서 출발한 열차가 도착후, b 역에서 출발하는 열차가 있는 경우, 열차개수 1개 차감.
            old = new

        print(f'Case #{i+1}:',answer_na,answer_nb)
        
    return
BOJ12731()

# def BOJ20920():
    # import sys
    # from collections import defaultdict

    # global words
    # n,m = map(int,input().split())
    # words = defaultdict(int)
    # for _ in range(n):
    #     word = sys.stdin.readline().strip()
    #     # 조건 : 
    #     # 0. m 보다 긴 단어
    #     # 1. 자주나오는 단어
    #     # 2. 긴단어
    #     # 3. 알파벳 순서
    #     if len(word) >=m:
    #         words[word] += 1
    # arr = list(words.keys())

    # def quick_sort(arr):
    #     global words
    #     if len(arr) <= 1:
    #         return arr
    #     pivot = arr[len(arr) // 2]
    #     lesser_arr, equal_arr, greater_arr = [], [], []
    #     for word in arr:
    #         # 1. 자주나오는 단어
    #         if words[word] > words[pivot]:
    #             lesser_arr.append(word)
    #         elif words[word] < words[pivot]:
    #             greater_arr.append(word)
    #         else:
    #             # 2. 긴단어
    #             if len(word) > len(pivot):
    #                 lesser_arr.append(word)
    #             elif len(word) < len(pivot):
    #                 greater_arr.append(word)
    #             else:
    #                 # 3. 알파벳 순서
    #                 if word < pivot:
    #                     lesser_arr.append(word)
    #                 elif word > pivot:
    #                     greater_arr.append(word)
    #                 else:
    #                     equal_arr.append(word)
    #     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

    # answer = quick_sort(arr)
    # for i in answer:
    #     print(i)
# BOJ20920()