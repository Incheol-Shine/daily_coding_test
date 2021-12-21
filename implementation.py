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

# def BOJ12731(): # 열차 시간표(small) (https://www.acmicpc.net/problem/12731)
    # import sys

    # def hToM(hhmm):
    #     hh, mm = list(map(int,hhmm.split(':')))
    #     return hh*60 + mm

    # # 정렬 알고리즘. 
    # # 숫자가 작을수록 뒤에 (내림차순)
    # # 숫자가 같으면 알파벳 순으로 (flag = True 이면 내림차순 (b,a) , False 이면 오름차순 (a,b))
    # def quick_sort(arr,flag): # arr = [[val, alpha]]
    #     if len(arr) <= 1:
    #         return arr
    #     pivot = arr[len(arr) // 2][0]
    #     lesser_arr, equal_arr, greater_arr = [], [], []
    #     for num in arr:
    #         if num[0] < pivot:
    #             lesser_arr.append(num)
    #         elif num[0] > pivot:
    #             greater_arr.append(num)
    #         else:
    #             equal_arr.append(num)
    #     return quick_sort(greater_arr,flag) + sorted(equal_arr, key=lambda x: x[1], reverse=flag) + quick_sort(lesser_arr,flag)

    # n = int(input())
    # for i in range(n):
    #     t = int(sys.stdin.readline().strip())
    #     na, nb = map(int, sys.stdin.readline().split())
        
    #     a_station = [] # b 에서 온 열차 도착시간 + t, a 에서 출발하는 열차 출발시간
    #     b_station = [] # a 에서 온 열차 도착시간 + t, b 에서 출발하는 열차 출발시간
    #     for _ in range(na):
    #         start, end = map(hToM, sys.stdin.readline().split())
    #         a_station.append([start, 'a'])
    #         b_station.append([end+t, 'a'])

    #     # 두가지 방법으로 정렬하려고 하는데 어떤 자료구조를 사용해야 할까?
    #     for _ in range(nb):
    #         start, end = map(hToM, sys.stdin.readline().split())
    #         a_station.append([end+t, 'b'])
    #         b_station.append([start, 'b'])

    #     a_station = quick_sort(a_station,False)
    #     b_station = quick_sort(b_station,True)

    #     old, new = 0,0
    #     answer_na, answer_nb = na, nb
    #     # print(a_station,b_station)

    #     for _ in range(len(a_station)):
    #         new = a_station.pop()[1]
    #         if old == 'b' and new == 'a': answer_na -= 1 # a 역에서는 b에서 출발한 열차가 도착후, a 역에서 출발하는 열차가 있는경우, 열차개수 1개 차감.
    #         old = new
    #     for _ in range(len(b_station)):
    #         new = b_station.pop()[1]
    #         if old == 'a' and new == 'b': answer_nb -= 1 # b 역에서는 a에서 출발한 열차가 도착후, b 역에서 출발하는 열차가 있는 경우, 열차개수 1개 차감.
    #         old = new

    #     print(f'Case #{i+1}:',answer_na,answer_nb)
        
    # return
# BOJ12731()

# def BOJ20920(): # 영단어 암기는 괴로워 (https://www.acmicpc.net/problem/status/20920)
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

# def BOJ20920_2(): # 영단어 암기는 괴로워 2번째 해답
    # import sys
    # from collections import Counter # 1번째 해답코드의 words 에 해당하는 dic 을 바로 만들어 준다.

    # n,m = map(int, sys.stdin.readline().split())
    # words = Counter(sys.stdin.readline().strip() for _ in range(n))
    # words = sorted(words, key = lambda x: (-words[x], -len(x), x)) # sort 에서 여러 조건으로 나누는 경우
    # print(*words, sep = "\n")
# BOJ20920_2()

# def BOJ2174(): # 로봇 시뮬레이션 (https://www.acmicpc.net/problem/2174)
    # import sys

    # global robots
    # global world

    # a,b = map(int, input().split())
    # n,m = map(int, input().split())


    # world = [[-1]*b for _ in range(a)]
    # dir_word = {'N':0, 'E':1, 'S':2, 'W':3}
    # dir_coord = [(0,1),(1,0),(0,-1),(-1,0)] # n, e, s, w

    # robots=[]
    # for num in range(n):
    #     x,y,z = sys.stdin.readline().split()
    #     x,y = map(lambda t : int(t)-1, (x,y))
    #     robots.append([x, y, dir_word[z]])
    #     world[x][y] = num # num 은 로봇 번호

    # question = [sys.stdin.readline().split() for _ in range(m)]

    # def f():
    #     global robots
    #     global world

    #     for k in range(len(question)):
    #         num, order, count = map(lambda x: int(x) if x.isdigit() else x, question[k])
    #         num -= 1    # 로봇 번호는 0부터 시작
    #         if order == 'L':
    #             robots[num][2] = (robots[num][2] + 3*count)%4
    #         elif order == 'R':
    #             robots[num][2] = (robots[num][2] + count)%4
    #         elif order == 'F':
    #             n_x, n_y = robots[num][:2]
    #             x, y = dir_coord[robots[num][2]]
    #             for i in range(count):
    #                 n_x += x
    #                 n_y += y
    #                 if not(0 <= n_x < a and 0 <= n_y < b) : 
    #                     print(f"Robot {num+1} crashes into the wall")
    #                     return 
    #                 if world[n_x][n_y] != -1: 
    #                     print(f"Robot {num+1} crashes into robot {world[n_x][n_y]+1}")
    #                     return
    #                 if i == count-1:
    #                     world[n_x][n_y], world[robots[num][0]][robots[num][1]] = world[robots[num][0]][robots[num][1]], world[n_x][n_y]
    #                     robots[num][0], robots[num][1] = n_x, n_y
    #     else: print("OK")
    # f()
# BOJ2174()

# def BOJ16931(): # 겉넓이 구하기 (https://www.acmicpc.net/problem/16931)
    # import sys

    # n,m = map(int, input().split())
    # dice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # def f(matrix): # 작은값에서 큰값으로 갈때 더한다.
    #     area = 0
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if j-1 <0: pre = 0
    #             else: pre = matrix[i][j-1]
    #             if matrix[i][j] > pre:
    #                 area += matrix[i][j] - pre
    #     return area

    # row_side = f(dice)
    # col_side = f(list(zip(*dice)))
    # up_side = 0
    # for i in dice:
    #     for j in i:
    #         if j != 0: up_side += 1

    # answer = (row_side + col_side + up_side) * 2
    # print(answer)
# BOJ16931()

# def BOJ20055(): # 컨베이어 벨트 위의 로봇 (https://www.acmicpc.net/problem/20055)

    # import sys
    # from collections import deque

    # n,k = map(int, sys.stdin.readline().split())
    # belt = deque()
    # belt.extend(map(int,sys.stdin.readline().split()))

    # robot = deque()
    # robot.extend([0]*n)

    # cycle = 0

    # def f():
    #     cycle = 0
    #     cnt = 0
    #     for i in belt:
    #         if i == 0: cnt += 1
    #     while True:
    #         cycle += 1
    #         # 1
    #         robot.appendleft(0)
    #         robot.pop()
    #         belt.appendleft(belt.pop())

    #         if robot[-1] == 1: # 로봇이 내리는 위치에 있는 경우, 내린다.
    #             robot[-1] = 0

    #         # 2
    #         for i in range(n-2,-1,-1): #마지막 칸은 로봇이 없으므로 제외
    #             if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
    #                 robot[i+1] = 1
    #                 belt[i+1] -= 1
    #                 if belt[i+1] == 0: cnt += 1
    #                 robot[i] = 0

    #         if robot[-1] == 1: # 로봇이 내리는 위치에 있는 경우, 내린다.
    #             robot[-1] = 0

    #         # 3
    #         if belt[0] != 0:
    #             robot[0] = 1
    #             belt[0] -= 1
    #             if belt[0] == 0: cnt += 1

    #         # 4
            
    #         if cnt == k: return cycle
            
    # print(f())
# BOJ20055()

# def BOJ17276(): # 배열 돌리기 (https://www.acmicpc.net/problem/17276)
    # import sys

    # def turn(n,d,board):
    #     for i in range(n//2):
    #         # 이동하는 8개의 좌표를 시계방향으로 나열
    #         # cw = [[i,i], [i, n//2], [i, n-1-i], [n//2, n-1-i], [n-1-i, n-1-i], [n-1-i, n//2], [n-1-i, i], [n//2, i]]
    #         ccw = [[i,i], [n//2, i], [n-1-i, i], [n-1-i, n//2], [n-1-i, n-1-i], [n//2, n-1-i], [i, n-1-i], [i, n//2]]
    #         # before : 원래 데이터를 백업
    #         before = [board[a][b] for a,b in ccw]
    #         for idx,(x,y) in enumerate(ccw):
    #             board[x][y] = before[(idx+d)%8] # 회전시킨 데이터로 교체
    #     # 출력
    #     for r in board:
    #         for c in r:
    #             print(c, end = " ")
    #         print()

    # t = int(input())
    # for _ in range(t):
    #     n,d = map(int, sys.stdin.readline().split())
    #     d = d//45 if d>=0 else (360+d)//45  # 음수, 양수 통일
    #     board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    #     turn(n,d,board)
# BOJ17276()

# def BOJ2799(): # 블라인드 (https://www.acmicpc.net/problem/2799)
    # import sys

    # m,n = map(int, sys.stdin.readline().split())
    # windows= list(sys.stdin.readline() for _ in range(m*5+1))
    # blind = [0]*5
    # count_star = [0]*4

    # for x in range(m):
    #     for i in range(1+x*5, 5+x*5):
    #         count_star[i-x*5-1] += windows[i].count('*')//4
    # blind[0] = n*m-count_star[0]

    # while count_star.count(0) != 4:
    #     idx = 4-count_star.count(0)
    #     blind[idx] += 1
    #     for i in range(4):
    #         if count_star[i] != 0: count_star[i] -= 1


    # print(*blind)
# BOJ2799()

# def BOJ3613(): # Java VS C++ (https://www.acmicpc.net/problem/3613)
    # import sys

    # name = sys.stdin.readline().strip()

    # c,java = False,False
    # answer = ''
    # for i in name:
    #     if i == "_" :
    #         c = True
    #     if i.isupper(): 
    #         java = True
    # if name[-1]== '_' or name[0].isupper() or name[0]=='_': print('Error!')
    # elif c and java:
    #     print('Error!')
    # elif c:
    #     cnt = 0
    #     answer = list(name)
    #     while cnt<len(name):
    #         if cnt+1<len(name) and answer[cnt] =='_':
    #             if answer[cnt+1]=='_':
    #                 answer = 'Error!'
    #                 break
    #             answer[cnt+1] = answer[cnt+1].upper()
    #         cnt += 1
    #     for i in answer:
    #         if i != '_':print(i, end = '')
    # else:
    #     for i in name:
    #         if i.isupper():print('_'+i.lower(),end = '')
    #         else: print(i, end = '')
# BOJ3613()

# def BOJ23253(): # 자료구조는 정말 최고야 (시공의 폭풍 아님) (https://www.acmicpc.net/problem/23253)
    # import sys

    # n, m = map(int, sys.stdin.readline().split())
    # stacks = {}
    # for i in range(m):
    #     k = sys.stdin.readline().strip()
    #     stacks[i] = list(map(int, sys.stdin.readline().split()))
    
    # cnt = 1
    # while cnt <= n: # 교과서 수만큼 반복
    #     for i in range(m):
    #         if len(stacks[i]) !=0 and stacks[i][-1] == cnt:
    #             cnt += 1
    #             stacks[i].pop()
    #             break
    #     else:
    #         print("No")
    #         break
    # else:
    #     print("Yes")
# BOJ23253()

# def BOJ20157(): # 화살을 쏘자! (https://www.acmicpc.net/problem/20157)
    # import sys
    # from collections import defaultdict
    # from math import gcd

    # n = int(input())

    # dic = defaultdict(int)
    # # 각 x,y를 최대공약수로 나눠서 같은 x,y조합 수를 구한다.
    # for _ in range(n):
    #     x,y = map(int, sys.stdin.readline().split())
    #     choidae = gcd(x,y)
    #     dic[(x//choidae, y//choidae)] += 1

    # answer = max(dic.keys(), key = lambda x: dic[x])
    # print(dic[answer])
# BOJ20157()

# def BOJ1476(): # 날짜 계산 (https://www.acmicpc.net/problem/1476)
    # a, b, c = map(int, input().split())
    # count = 1
    # while True:
    #     if (count-1) % 15 == a-1:
    #         if (count-1) % 28 == b-1:
    #             if (count-1) % 19 == c-1:
    #                 break
    #     count += 1
    # print(count)
# BOJ1476()

# def BOJ1748(): # 수 이어 쓰기 1 (https://www.acmicpc.net/problem/1748)
    # def e(): # 10 의 제곱근 반환
    #     x = n
    #     answer = 0 # 지수
    #     while x!=0:
    #         x//=10
    #         answer += 1
    #     return answer

    # n = int(input())
    # k = e()

    # answer = 0
    # for i in range(1,k):
    #     answer += 9*(10**(i-1))*i
    # answer += (n-10**(k-1)+1)*k

    # print(answer)
# BOJ1748()

# def BOJ14676(): # 영우는 사기꾼? (https://www.acmicpc.net/problem/14676)
    # import sys
    # global tower

    # n, m, k = map(int, sys.stdin.readline().split())
    # condition = [[] for _ in range(n+1)]
    # tower = [0]*(n+1)
    # for _ in range(m):
    #     x,y = map(int, sys.stdin.readline().split())
    #     condition[y].append(x) # y를 건설하기 위해서는 x를 건설해야 함
    
    # def f():
    #     global tower
    #     for _ in range(k):
    #         order, num = map(int, sys.stdin.readline().split())
    #         # 건물 짓기
    #         if order == 1:
    #             for i in condition[num]:
    #                 if tower[i] == 0: # 조건이 되는 건물이 안 지어진 경우
    #                     print("Lier!")
    #                     return
    #             tower[num] += 1

    #         if order == 2:
    #             if tower[num] == 0: # 파괴할 건물이 없는 경우
    #                 print("Lier!")
    #                 return
    #             else: 
    #                 tower[num] -= 1

    #     print("King-God-Emperor")

    # f()
# BOJ14676()

# def BOJ16466(): # 콘서트 (https://www.acmicpc.net/problem/16466)
    # import sys
    # from heapq import heapify, heappop

    # n=int(sys.stdin.readline().strip())
    # heap = list(map(int,sys.stdin.readline().split()))
    # heapify(heap)

    # for i in range(1,10**6+1):
    #     if len(heap) == 0 or i != heappop(heap):
    #         print(i)
    #         break
# BOJ16466()

# def BOJ16466_2(): # 콘서트 2nd solution
    # import sys
    
    # n=int(sys.stdin.readline().strip())
    # # arr 가 list 인경우, 시간초과가 나온다.
    # arr = set(map(int,sys.stdin.readline().split()))

    # for i in range(1,10**6+1):
    #     # set 에서와 list 에서 in 함수의 작동이 다르게 이루어지는 것 같다.
    #     if i not in arr:
    #         print(i)
    #         break
# BOJ16466_2()

# def BOJ14676_2(): # 영우는 사기꾼? 2nd solution (위상정렬?)
    # import sys
    # global tower

    # n, m, k = map(int, sys.stdin.readline().split())
    # condition = [[] for _ in range(n+1)]
    # indegree = [0]*(n+1)
    # tower = [0]*(n+1)

    # for _ in range(m):
    #     x,y = map(int, sys.stdin.readline().split())
    #     condition[x].append(y) # y를 건설하기 위해서는 x를 건설해야 함
    #     indegree[y] += 1

    
    # make_check, delete_check = True, True
    # for _ in range(k):
    #     order, num = map(int, sys.stdin.readline().split())
    #     # 건물 짓기
    #     if order == 1:
    #         if indegree[num] == 0:
    #             tower[num] += 1
    #             if tower[num] == 1:
    #                 for i in condition[num]:
    #                     indegree[i] -= 1
    #         else:
    #             make_check = False
    #             break

    #     # 건물 부수기
    #     if order == 2:
    #         if tower[num] > 0: # 파괴할 건물이 있는 경우
    #             tower[num] -= 1
    #             if tower[num] == 0:
    #                 for i in condition[num]:
    #                     indegree[i] += 1
    #         else: 
    #             delete_check = False
    #             break

    # if make_check and delete_check:
    #     print('King-God-Emperor')
    # else:
    #     print('Lier!')
# BOJ14676_2()

# def BOJ23253_2(): # 자료구조는 정말 최고야 2nd solution
    # import sys

    # n, m = map(int, sys.stdin.readline().split())
    # stacks = []
    # for i in range(m):
    #     k = sys.stdin.readline().strip()
    #     stacks.append(list(map(int, sys.stdin.readline().split())))
    # cnt = 1
    # stacks.sort(key = lambda x: x[-1])

    # while cnt <= n: # stacks 가 빈 리스트일 때 종료
    #     for i in range(len(stacks)):
    #         if len(stacks[i]) == 0: continue
    #         if stacks[i][-1] == cnt:
    #             stacks[i].pop()
    #             cnt += 1
    #         else:
    #             break
        
    #     stacks.sort(key = lambda x: x[-1] if len(x)!=0 else 999999)
    #     if len(stacks[0]) !=0 and stacks[0][-1] != cnt:
    #         print("No")
    #         break
    # else:
    #     print("Yes")
# BOJ23253_2()

# def BOJ23253_3(): # 자료구조는 정말 최고야 3rd solution
    # import sys

    # def is_sorted(arr):
    #     return all(arr[i]>arr[i+1] for i in range(len(arr)-1))

    # n, m = map(int, sys.stdin.readline().split())
    # for i in range(m):
    #     k = int(sys.stdin.readline().strip())
    #     stack = list(map(int, sys.stdin.readline().split()))
    #     if is_sorted(stack) == False:
    #         print("No")
    #         break
    # else:
    #     print("Yes")
# BOJ23253_3()

# def BOJ8911(): # 거북이 (https://www.acmicpc.net/problem/8911)
    # import sys

    # t = int(input())
    # dir = [(0,1),(1,0),(0,-1),(-1,0)] # x,y 기준 상, 우, 하, 좌 - 시계방향

    # for _ in range(t):
    #     order = sys.stdin.readline().strip()
    #     min_x, max_x, min_y, max_y = 0,0,0,0
    #     turtle_dir = 0
    #     turtle_x, turtle_y = 0,0
    #     for i in order:
    #         if i == 'F':
    #             turtle_x += dir[turtle_dir][0]
    #             turtle_y += dir[turtle_dir][1]
    #         elif i == 'B':
    #             turtle_x -= dir[turtle_dir][0]
    #             turtle_y -= dir[turtle_dir][1]
    #         elif i == 'L':
    #             turtle_dir = (turtle_dir+3)%4
    #             continue
    #         elif i == 'R':
    #             turtle_dir = (turtle_dir+1)%4
    #             continue
    #         min_x = min(turtle_x, min_x)
    #         max_x = max(turtle_x, max_x)
    #         min_y = min(turtle_y, min_y)
    #         max_y = max(turtle_y, max_y)

    #     print((max_x-min_x)*(max_y-min_y))
# BOJ8911()

# def BOJ17359(): # 전구 길만 걷자 (https://www.acmicpc.net/problem/17359)
    # import sys
    # from itertools import permutations

    # n = int(input())
    # bulbs = [list(*map(list,sys.stdin.readline().split())) for _ in range(n)]
    # changes = [0]*n
    # for i in range(n):
    #     for j in range(len(bulbs[i])-1):
    #         x = bulbs[i][j] + bulbs[i][j+1]
    #         if x == "10" or x == "01":
    #             changes[i] += 1

    # permute = permutations(bulbs)
    # min_change = 99
    # for i in permute:
    #     change = 0
    #     for j in range(n-1):
    #         if i[j][-1] != i[j+1][0] : change += 1
    #     min_change = min(change, min_change)
    # answer = sum(changes) + min_change
    # print(answer)
# BOJ17359()

# def BOJ16923(): # 다음 다양한 단어 (https://www.acmicpc.net/problem/16923)
    # import sys
    # from collections import defaultdict

    # s = sys.stdin.readline().strip()
    
    # def f(s):
    #     all_alpha = set('abcdefghijklmnopqrstuvwxyz')
    #     next_s = s
    #     while next_s:
    #         left_alpha = sorted(list(all_alpha - set(next_s)))

    #         # left_alpha 중 가장 작은거를 추가해서 다음 단어 만들기
    #         if len(left_alpha) > 0: 
    #             for i in left_alpha:
    #                 if s < next_s+i:
    #                     print(next_s+i)
    #                     return
    #         # 다음 단어들 중 다양한 단어 찾기
    #         next_s = next_s[:-1]
    #     else:
    #         print(-1)
    #         return
    # f(s)
# BOJ16923()

# def BOJ14500(): # 테트로미노 (https://www.acmicpc.net/problem/14500)
    # import sys

    # dir = [(-1,0),(0,1),(1,0),(0,-1)]
    # tetromino = [[[1],[1],[1]],
    #             [[1],[2],[3]],
    #             [[2],[2],[1]],
    #             [[2],[2],[3]],
    #             [[2],[1],[2]],
    #             [[2],[3],[2]],
    #             [[1],[1,2]]]

    
    # def tetro_sum(x,y,shape):
    #     answer = paper[x][y]
    #     for arr in shape:
    #         for num in arr:
    #             i,j = dir[num]
    #             n_x, n_y = x+i, y+j
    #             if not(0<=n_x<n and 0<=n_y<m): return -1
    #             answer += paper[n_x][n_y]
    #         x, y = n_x, n_y

    #     return answer
        

    # n,m = map(int,sys.stdin.readline().split())
    # paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # total = []

    # for shape in tetromino:
    #     for i in range(4):
    #         rotate = list(map(lambda x: list(map(lambda y: (y+i)%4, x)),shape))
    #         for x in range(n):
    #             for y in range(m):
    #                 value = tetro_sum(x,y,rotate)
    #                 total.append(value)
    # answer = max(total)
    # print(answer)
# BOJ14500()

# def BOJ14500_2(): # 테트로미노 2nd solution
    # import sys
    # global max_val

    # dir = [(-1,0),(0,1),(1,0),(0,-1)]
    # tetromino = [[[1],[2],[3]],     # ㅁ 한가지 모양
    #             [[1],[1],[1]],    # ㅡ,ㅣ 두가지 모양
    #             [[2],[1],[2]],     # ㄱㄴ 대중 이런 모양 두가지 모양
    #             [[2],[3],[2]],     # 이것도 두가지 모양
    #             [[2],[2],[1]],     # ㄱ 세운 모양 4방향 다 다름
    #             [[2],[2],[3]],     # ㄴ 대칭 4방향 다 다름
    #             [[1],[1,2]]]       # 4방향 다 다름


    # def tetro_sum(x,y,shape):

    #     answer = paper[x][y]
    #     for arr in shape:
    #         for num in arr:
    #             i,j = dir[num]
    #             n_x, n_y = x+i, y+j
    #             if not(0<=n_x<n and 0<=n_y<m): return -1
    #             answer += paper[n_x][n_y]
    #         x, y = n_x, n_y

    #     return answer

    # n,m = map(int,sys.stdin.readline().split())
    # paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # max_val = 0

    # for idx, shape in enumerate(tetromino):
    #     for i in range(4):
    #         if idx == 0 and i>=1 : break
    #         elif idx < 4 and i>=2 : break
    #         rotate = list(map(lambda x: list(map(lambda y: (y+i)%4, x)),shape))
    #         for x in range(n):
    #             for y in range(m):
    #                 value = tetro_sum(x,y,rotate)
    #                 max_val = max(value, max_val)
    # print(max_val)
# BOJ14500_2()


# def BOJ16926(): # 배열 돌리기 (https://www.acmicpc.net/problem/16926)
    # import sys

    # n,m,r = map(int, sys.stdin.readline().split())
    # matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # dir = [(0,1),(1,0),(0,-1),(-1,0)]

    # layers = []

    # for k in range(min(n//2, m//2)):
    #     x,y = k,k
    #     layer = []
    #     for i in range(4):
    #         a_x, a_y = dir[i]
    #         if i%2 == 0: bounder = m-1
    #         else : bounder = n-1

    #         for j in range(k,bounder-k):
    #             layer.append(matrix[x][y])
    #             x, y = x+a_x, y+a_y
    #     layers.append(layer)

    # answer = [[0]*m for _ in range(n)]

    # for k in range(min(n//2, m//2)):
    #     count = 0
    #     x,y = k,k
    #     for i in range(4):
    #         a_x, a_y = dir[i]
    #         if i%2 == 0: bounder = m-1
    #         else : bounder = n-1

    #         for j in range(k,bounder-k):
    #             answer[x][y] = layers[k][(count+r)%len(layers[k])]
    #             count += 1
    #             x, y = x+a_x, y+a_y

    # for j in answer:
    #     for k in j:
    #         print(k, end= " ")
    #     print()
    # print()
# BOJ16926()

# def BOJ4673(): # 셀프 넘버 (https://www.acmicpc.net/problem/4673)
    # def d(n):
    #     answer = n
    #     for i in map(int, list(str(n))):
    #         answer += i
    #         if answer > 10000: return -1
    #     return answer

    # a = set([i for i in range(1,10001)])
    # b = set([])
    # for i in range(1,10001):
    #     b.add(d(i))

    # for i in sorted(list(a-b)):
    #     print(i)
# BOJ4673()

# def palindrome_date(): # 대칭절 (자작 문제)
    ## 앞 뒤 방향으로 볼 때 같은 순서의 숫자로 구성된 날짜를 대칭절이라 한다. ex) 2021.12.02 는 20211202 로 대칭절이다.
    ## 문제 : 오늘은 2021.12.05 이다. 오늘로부터 4000.12.31 까지 모든 대칭절을 출력하는 코드를 작성해라

    # def is_palindrome(word): # 대칭 여부 파악
    #     for i in range(len(word)//2):
    #         if word[i] != word[len(word)-1-i]:
    #             return False
    #     return True
    
    # def is_leapyear(year): # 윤년 여부 파악
    #     if year%4 == 0:
    #         if year%100 == 0:
    #             if year%400 == 0:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return True
    #     else:
    #         return False

    # year, mm, dd = 2021, 12, 5
    # month_with_31 = [1,3,5,7,8,10,12]
    # month_with_30 = [4,6,9,11]
    # leap = is_leapyear(year)
    # boundary = 31

    # while year < 4001:
    #     word = str(year) + (str(mm) if len(str(mm))==2 else '0'+str(mm)) + (str(dd) if len(str(dd))==2 else '0'+str(dd))
    #     if is_palindrome(word):
    #         print(word[:4]+'.'+word[4:6]+'.'+word[6:])
        
    #     if mm == 2:
    #         if leap:
    #             boundary == 29
    #         else:
    #             boundary == 28

    #     elif mm in month_with_30:
    #         boundary == 30

    #     elif mm in month_with_31:
    #         boundary == 31

    #     dd += 1
    #     if dd > boundary:
    #         dd = 1
    #         mm += 1
    #     if mm > 12:
    #         mm = 1
    #         year +=1
    #         leap = is_leapyear(year)
# palindrome_date()

# def BOJ15954(): # 인형들 (https://www.acmicpc.net/problem/15954)
    # # k 개 이상 ~~~!! 조건을 잘 읽을 것
    # import sys
    # from decimal import Decimal
    
    # n, k = map(int, input().split())
    # dolls = list(map(int,sys.stdin.readline().split()))
    # answer = 9999999999

    # for x in range(n-k+1):
    #     for y in range(n-x,k-1,-1):
    #         mean = 0
    #         variance = 0
    #         for z in range(y):
    #             mean += dolls[x+z]
    #         mean /= k
    #         for z in range(y):
    #             variance += (Decimal(str(dolls[x+z]))-Decimal(str(mean)))**2
    #         variance /= k
    #         # print(mean, variance**(1/2))
    #         answer = min(answer, Decimal(str(variance))**Decimal(str((1/2))))
    # print(answer)
# BOJ15954()

# def BOJ15954_2(): # 인형들 2nd solution
    # import sys
    # import math
    
    # n, k = map(int, input().split())
    # dolls = list(map(int,sys.stdin.readline().split()))
    # answer = []
    
    # def variance(m,arr):
    #     var = 0
    #     for a in arr:
    #         var += (a-m)**2
    #     return var/len(arr)


    # for x in range(n-k+1):
    #     for y in range(n-x-k+2):
    #         arr = dolls[x:x+k+y]
    #         mean = sum(arr)/len(arr)
    #         var = variance(mean,arr)
    #         answer.append(var)
    # print(math.sqrt(min(answer)))
# BOJ15954_2()

# def BOJ18808(): # 스티커 붙이기 (https://www.acmicpc.net/problem/18808)
    # import sys
    # from copy import deepcopy

    # global answer

    # n,m,k = map(int, sys.stdin.readline().split())
    # class Sticker:
    #     def __init__(self,x,y,shape):
    #         self.size = [x,y]
    #         self.shape = shape
    
    # stickers = []
    # for i in range(k):
    #     x,y = map(int,sys.stdin.readline().split())
    #     shape = [list(map(int,sys.stdin.readline().split())) for _ in range(x)]
    #     stickers.append(Sticker(x,y,shape))
    

    # # 어떻게 회전??
    # def rotate(shape): # 90도 회전
    #     n,m = len(shape[0]), len(shape)

    #     rotated_shape = [[0]*m for _ in range(n)]
    #     for i in range(n):
    #         for j in range(m):
    #             rotated_shape[i][j] = shape[m-1-j][i]

    #     return rotated_shape

    # # 붙이기
    # def sticky(x,y,shape):
    #     copy = deepcopy(board)
    #     for i in range(len(shape)):
    #         for j in range(len(shape[0])):
    #             if not(0<=x+i<n and 0<=y+j<m): return None
    #             if copy[x+i][y+j]+shape[i][j] >1: return None
    #             copy[x+i][y+j] += shape[i][j]
    #     return copy


    # board = [[0]*m for _ in range(n)]
    
    # flag = 0
    # for sticker in stickers:
    #     for x in range(4):
    #         for i in range(n-len(sticker.shape)+1):
    #             for j in range(m-len(sticker.shape[0])+2):
    #                 copy = sticky(i,j,sticker.shape)
    #                 if copy:
    #                     board = copy
    #                     flag = 1
    #                     break
    #                 else: flag = 0
    #             if flag: break
    #         if flag: break
    #         sticker.shape = rotate(sticker.shape)

    # answer = 0
    # for i in board:
    #     for j in i:
    #         print(j, end =" ")
    #         answer += j
    #     print()
    # print(answer)
# BOJ18808()

# def BOJ18808_2(): # 스티커 붙이기 2nd solution
    # import sys

    # global board
    # global answer

    # n,m,k = map(int, sys.stdin.readline().split())
    # class Sticker:
    #     def __init__(self,x,y,shape):
    #         self.size = [x,y]   # -> 회전시킬 때 값 바뀜
    #         self.shape = []     # -> 회전시킬 때 값 바뀜
    #         for i in range(x):
    #             for j in range(y):
    #                 if shape[i][j]:
    #                     self.shape.append([i,j])

    
    # stickers = []
    # for i in range(k):
    #     x,y = map(int,sys.stdin.readline().split())
    #     shape = [list(map(int,sys.stdin.readline().split())) for _ in range(x)]
    #     stickers.append(Sticker(x,y,shape))

    # # 어떻게 회전??
    # def rotate(sticker): # 90도 회전
    #     x,y = sticker.size
    #     sticker.size = [y,x]   # size 정보 수정

    #     for idx, [i,j] in enumerate(sticker.shape):
    #         sticker.shape[idx] = [j, x-1-i]

    # # 붙이기
    # def attach(x,y,sticker):
    #     global board

    #     for i,j in sticker.shape:
    #         if not(0<=x+i<n and 0<=y+j<m): break   # 스티커가 범위를 벗어난 경우  -> 0
    #         if board[x+i][y+j]: break              # 이전 스티커와 겹쳐지는 경우  -> 0
    #     else:
    #         for i,j in sticker.shape:              # 겹쳐지지 않는 경우  -> 1
    #             board[x+i][y+j] = 1           
    #         return 1
    #     return 0


    # board = [[0]*m for _ in range(n)]
    
    
    # for sticker in stickers:
    #     for _ in range(4):
    #         flag = 0
    #         for i in range(n):
    #             for j in range(m):
    #                 flag = attach(i,j,sticker)
    #                 if flag: break
    #             if flag: break
    #         if flag: break
    #         rotate(sticker)

    # answer = 0
    # for i in board:
    #     for j in i:
    #         # print(j, end =" ")
    #         answer += j
    #     # print()
    # print(answer)
# BOJ18808_2()

# def BOJ18808_3(): # 스티커 붙이기 3rd solution
    # import sys
    # global answer

    # def is_possible(x,y,sticker,notebook): # x,y 기준으로 스티커를 붙일 수 있는 지 판단
    #     for i,j in sticker:
    #         if notebook[x+i][y+j]: break # 이미 스티커가 붙은 부분인 경우
    #     else:
    #         return True
    #     return False


    # def attach(n, m, R, C, sticker, notebook):
    #     for x in range(n-R+1):
    #         for y in range(m-C+1):
    #             if is_possible(x,y,sticker,notebook):
    #                 for i,j in sticker:
    #                     notebook[x+i][y+j] = 1
    #                 return True
    #     return False   


    # def rotation(R,C,sticker):
    #     r,c = C,R
    #     for idx, [i,j] in enumerate(sticker):
    #         sticker[idx] = [j, R-1-i]
    #     return r,c,sticker


    # n,m,k = map(int, sys.stdin.readline().split())
    # notebook = [[0]*m for _ in range(n)]
    # for _ in range(k):
    #     R,C = map(int,sys.stdin.readline().split())
    #     shape = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
    #     sticker = []
    #     for i in range(R):
    #         for j in range(C):
    #             if shape[i][j]: sticker.append([i,j])

    #     for i in range(4):
    #         if attach(n,m,R,C,sticker,notebook):   # n,m,notebook 은 직접 수정하지 않지만 인자로 넘겨주는 이유 - 파란 밑줄이 안생기기 때문에?
    #             break
    #         elif i < 3:
    #             R,C,sticker = rotation(R,C,sticker)

    # print(sum(map(sum, notebook)))
# BOJ18808_3()

# def BOJ10799(): # 쇠막대기 (https://www.acmicpc.net/problem/10799)
    # import sys
    # global count

    # def f(idx):
    #     global count
    #     # laser 는 이 함수(괄호) 안에서만 계산된 총 레이저 개수. 
    #     laser = 0
    #     while idx < len(arrange):
    #         # '()' 인 경우는 레이저. 레이저의 개수를 늘린다.
    #         if arrange[idx] == '(':
    #             if arrange[idx+1] == ')':
    #                 laser += 1
    #             # '()' 가 아닌 경우 괄호가 새로 열렸으므로 함수를 새로 호출한다.
    #             else:
    #                 idx, in_laser = f(idx+1)
    #                 laser += in_laser
    #         else:
    #             if arrange[idx-1] == '(': 
    #                 idx += 1
    #                 continue
    #             else:
    #                 count += laser+1
    #                 return idx, laser
    #         idx += 1

    # arrange = sys.stdin.readline().strip()

    # count = 0
    # f(0)
    # print(count)
# BOJ10799()

# def BOJ10799_2(): # 쇠막대기 2nd solution
    # import sys
    
    # def f(arrange):
    #     arrange = arrange.replace('()','0')

    #     pipe = 0  # 현재 겹쳐진 쇠막대기의 갯수
    #     piece = 0   # 쇠막대기 족각 총 개수

    #     for i in arrange:
    #         if i == "(":
    #             pipe += 1
    #         elif i == "0":
    #             piece += pipe
    #         else:
    #             pipe -= 1
    #             piece += 1    # 쇠막대기의 끝에 다다른 경우, 조각에 +1 을 해주고 stack에서 뺀다.
    #     return piece

    # arrange = sys.stdin.readline().strip()

    # print(f(arrange))
# BOJ10799_2()