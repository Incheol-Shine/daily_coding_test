# ## BFS
# def BOJ18405(): # 경쟁적 전염 (https://www.acmicpc.net/problem/18405)
#     import sys
#     from collections import deque

#     n, k = map(int, input().split())
#     flask = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#     s, x, y = map(int, input().split())

#     # bfs
#     count = 0
#     dir = [(1,0),(-1,0),(0,1),(0,-1)]

#     q = deque()
#     init_coord = []
#     for i in range(n):
#         for j in range(n):
#             if flask[i][j] != 0:
#                 init_coord.append((flask[i][j],i,j)) # value, 좌표

#     init_coord.sort(key=lambda x: x[0])  # value 가 작은 숫자부터 정렬
#     q.extend(init_coord)

#     while q:
#         if count == s: break
#         for _ in range(len(q)):
#             value, r, c = q.popleft()
#             for i, j in dir:
#                 n_r, n_c = r+i, c+j
                
#                 if not(0 <= n_r < n and 0 <= n_c < n): continue
#                 if flask[n_r][n_c] != 0: continue
#                 flask[n_r][n_c] = value
#                 q.append((value,n_r,n_c))
#         count += 1

#     print(flask[x-1][y-1])

#     return
# BOJ18405()

# def BOJ2644(): # 촌수계산 (https://www.acmicpc.net/problem/2644)
#     import sys
#     from collections import deque, defaultdict

#     n = int(input())
#     a,b = map(int, input().split())
#     m = int(input())

#     tree = defaultdict(list)
#     for i in range(m):
#         x,y = map(int, sys.stdin.readline().split()) # 방향 있음. 부모, 자식
#         tree[x].append(y)
#         tree[y].append(x)

#     def bfs():
#         visit = [False]*(n+1)
#         visit[0] = True

#         count = 0

#         q = deque()
#         q.append(a)
#         visit[a] = True

#         while q:
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node == b : return count
#                 for i in tree[node]:
#                     if visit[i] == False:
#                         q.append(i)
#                         visit[i] = True
#             count += 1
        
#         else:
#             return -1


#     print(bfs())
# BOJ2644()

# def BOJ16920(): # 확장 게임 (https://www.acmicpc.net/problem/16920)
#     import sys
#     from collections import deque, defaultdict
#     global board
#     global answer

#     n,m,p = map(int, sys.stdin.readline().split())
#     s = list(map(int, sys.stdin.readline().split()))
#     board = [list(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().strip())) for _ in range(n)]
    
#     coord = defaultdict(list)
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] != '.':
#                 num = board[i][j]
#                 coord[num].append((num, i, j)) # q 에 담을 거 : 거리, x, y 좌표

#     q = deque()
#     for i in range(1,p+1):
#         q.extend(coord[i])
        
#     dir = [(0,1),(1,0),(0,-1),(-1,0)]
#     answer = [0]*p

#     def bfs_1(l, num, x, y): # l은 거리, q 는 좌표
#         global board
#         global answer

#         q = deque()
#         q.append((num,x,y))
#         count = 0
#         while q:
#             if count >= l: return q
#             for _ in range(len(q)):
#                 num,x,y = q.popleft()
#                 answer[num-1] += 1

#                 for i,j in dir:
#                     n_x, n_y = x+i, y+j
#                     if not(0<=n_x<n and 0<=n_y<m): continue
#                     if board[n_x][n_y] != '.': continue
                    
#                     board[n_x][n_y] = num
#                     q.append((num,n_x, n_y))
#             count += 1
#         return q

#     def bfs_2(q):
#         global board
#         global answer

#         count = 0
#         while q:
#             num, x, y = q.popleft()

#             board[x][y] = num
#             small_q = bfs_1(s[num-1], num, x, y)
#             q+=small_q

#     bfs_2(q)
#     print(*answer)
# BOJ16920()

# def BOJ2234(): # 성곽 (https://www.acmicpc.net/problem/2234)
#     import sys
#     from collections import deque

#     n,m = map(int, sys.stdin.readline().split())
#     wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
#     visit  = [[-1]*n for _ in range(m)]

#     def BFS(a,b):
#         dir  = [(0,-1),(-1,0),(0,1),(1,0)] # 서 북 동 남
#         count = 0

#         q = deque()
#         q.append((a,b))
#         count += 1
#         visit[a][b] = room_num # 방 번호
#         while q:
#             x,y = q.popleft()
#             for idx in range(4):
#                 if wall[x][y] & 1<<idx: continue # 벽이 있는 경우
#                 i,j = dir[idx]
#                 if not(0<=x+i<m and 0<=y+j<n): continue # 범위를 벗어난 경우
#                 if visit[x+i][y+j] != -1: continue

#                 q.append((x+i,y+j))
#                 visit[x+i][y+j] = room_num
#                 count += 1
        
#         return count

#     room_num = 0    # 1. 방 개수  
#     area = []       # 2. 가장 넓은 방 넓이 = max(area)
#     answer3 = []    # 3. 벽 하나 제거 후 가장 넓은 방 넓이 = max(answer3)

#     for i in range(m):
#         prev_room = visit[i][0] if i != 0 else 0
#         for j in range(n):
#             if visit[i][j] == -1:
#                 area.append(BFS(i,j))
#                 room_num += 1
#                 answer3.append(prev_room+area[-1])
#             prev_room = area[visit[i][j]]
    
#     for j in range(n):
#         prev_num = visit[0][j]
#         for i in range(m):
#             if visit[i][j] != prev_num:
#                 answer3.append(area[prev_num]+area[visit[i][j]])
#             prev_num = visit[i][j]
    
#     print(room_num)
#     print(max(area))
#     print(max(answer3))
# BOJ2234()

# def BOJ7576(): # 토마토 (https://www.acmicpc.net/problem/7576)
#     import sys
#     from collections import deque
#     global box

#     def bfs(q):
#         global box
#         dir = [(0,1),(1,0),(0,-1),(-1,0)]
#         count = -1

#         while q:
#             count += 1
#             for _ in range(len(q)):
#                 x,y = q.popleft()
#                 for i, j in dir:
#                     n_x, n_y = x+i, y+j
#                     if not(0<=n_x<n and 0<=n_y<m): continue
#                     if box[n_x][n_y] !=0: continue
                    
#                     box[n_x][n_y] = 1
#                     q.append((n_x,n_y))
#         return count if count != 0 else -1

#     m,n = map(int, input().split()) # n행 m열
#     box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#     q=deque()
#     normal_tomato = 0
#     for i in range(n):
#         for j in range(m):
#             if box[i][j] == 1:
#                 q.append((i,j))
#             elif box[i][j] == 0:
#                 normal_tomato += 1

#     if normal_tomato == 0: answer = 0
#     else: answer = bfs(q)

#     for i in range(n):
#         for j in range(m):
#             if box[i][j] == 0:
#                 answer = -1
#                 break
#         if answer == -1: break

#     print(answer)
# BOJ7576()

# def BOJ16234(): # 인구이동 (https://www.acmicpc.net/problem/16234)
#     import sys
#     from collections import deque 

#     def bfs(i,j): # return population, size, union_xy
#         d_r = [0,-1,0,1] ## [서, 북, 동, 남]
#         d_c = [-1,0,1,0]

#         q = deque()
#         q.append([i,j])

#         population, size = 0, 0     # 인구수, 연합의 크기를 저장하는 변수
#         union_xy = []               # 연합국가의 좌표들을 저장하는 리스트

#         while q:
#             r, c = q.popleft()
            
#             if visit[r][c] == 0:
#                 size += 1
#                 population += nations[r][c]
#                 union_xy.append([r,c])
#                 visit[r][c] = size

#                 for k in range(4):
#                     if doors[r][c] & 1<<k == 0:                 # bit 연산. [서, 북, 동, 남] 방향으로 벽이 없는 경우
#                         if visit[r + d_r[k]][c + d_c[k]] == 0 : # 벽 없는 쪽 좌표를 방문하지 않은 경우
#                             q.append([r + d_r[k], c + d_c[k]])

#         return population, size, union_xy

#     n, l, r = map(int, input().split())
#     nations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#     ans = 0
#     while True:
#         # 국경 : bit mask 로 표시 ex) 서: 1, 북: 10, 동: 100, 남: 1000, 전부 다 막음 = 1111 = 15
#         doors = [[15]*n for _ in range(n)]
        
#         # 1. 국경 열기

#         for i in range(n):  
#             for j in range(n-1): # 두개씩 비교하므로 마지막은 생략
#                 if l <= abs(nations[i][j] - nations[i][j+1]) <= r:
#                     doors[i][j] -= 4    # 동쪽 국경 개방
#                     doors[i][j+1] -= 1  # 서쪽 국경 개방
            
#         for j in range(n):  
#             for i in range(n-1): 
#                 if l <= abs(nations[i][j] - nations[i+1][j]) <= r:
#                     doors[i][j] -= 8    # 남쪽 국경 개방
#                     doors[i+1][j] -= 2  # 북쪽 국경 개방

#         flag = 0                    # 전부 15(국경이 개방되지 않는 경우) 이면 0 => 반복 그만
#         for i in doors:
#             for j in i:
#                 if j != 15: 
#                     flag = 1 # 하나라도 15 가 아니면 flag = 1 => 반복문 계속 반복
#                     break
#         if flag == 0: break
                
#         # 2. 인구 이동하기 -> bfs
        
#         visit = [[0]*n for _ in range(n)]

#         for i in range(n):
#             for j in range(n):
#                 if visit[i][j] == 0:
#                     population, size, union_xy = bfs(i,j)
                    
#                     # print('size',size)
#                     # print('union',union_xy)
#                     # print('population',population)
                    
#                     for a,b in union_xy:
#                         nations[a][b] = population//size
#         ans += 1
#         # for i in doors:
#         #     for j in i:
#         #         print(j, end = " ")
#         #     print()
#     print(ans)
# BOJ16234()

# def BOJ7562(): # 나이트의 이동 (https://www.acmicpc.net/problem/7562)
#     import sys
#     from collections import deque

#     def bfs(start, goal, L):
#         if start == goal: return 0

#         visit = [[-1]*L for _ in range(L)]
#         dir = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]  # 시계방향
#         count = 0

#         q = deque()
#         q.append(start)
#         visit[start[0]][start[1]] = count
#         while q:
#             count += 1
#             for _ in range(len(q)):

#                 x,y = q.popleft()
#                 for i,j in dir:
#                     n_x, n_y = x+i, y+j
#                     if not(0<=n_x<L and 0<=n_y<L): continue
#                     if visit[n_x][n_y] != -1: continue

#                     visit[n_x][n_y] = count
#                     q.append((n_x, n_y))
#                     if (n_x, n_y) == goal: return count
#         return 0

#     t = int(input())

#     for _ in range(t):
#         L = int(sys.stdin.readline().strip())
#         start = tuple(map(int, sys.stdin.readline().split()))
#         goal = tuple(map(int, sys.stdin.readline().split()))

#         print(bfs(start, goal, L))
# BOJ7562()

# def BOJ7562_2(): # 나이트의 이동 2nd solution
#     import sys
#     from collections import deque

#     def short(start,goal):
#         x,y = abs(start[0]-goal[0]), abs(start[1]-goal[1])
#         count = 0
#         while x>5 or y>5:
#             if x>y:
#                 x-=2
#                 if y>0: y-=1
#                 else: y+=1
#             else:
#                 y-=2
#                 if x>0: x-=1
#                 else: x+=1
#             count +=1

#         return start, goal, count

#     def bfs(start, goal, L):
#         if start == goal: return 0

#         visit = [[-1]*L for _ in range(L)]
#         dir = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]  # 시계방향
#         count = 0

#         q = deque()
#         q.append(start)
#         visit[start[0]][start[1]] = count
#         while q:
#             count += 1
#             for _ in range(len(q)):

#                 x,y = q.popleft()
#                 for i,j in dir:
#                     n_x, n_y = x+i, y+j
#                     if not(0<=n_x<L and 0<=n_y<L): continue
#                     if visit[n_x][n_y] != -1: continue

#                     visit[n_x][n_y] = count
#                     q.append((n_x, n_y))
#                     if (n_x, n_y) == goal: return count
#         return 0

#     t = int(input())

#     for _ in range(t):
#         L = int(sys.stdin.readline().strip())
#         start = tuple(map(int, sys.stdin.readline().split()))
#         goal = tuple(map(int, sys.stdin.readline().split()))

#         n_start, n_goal, i = short(start, goal)
#         print(i+bfs(n_start, n_goal, L))
# BOJ7562_2()

# def BOJ16953(): # A -> B (https://www.acmicpc.net/problem/16953)
#     from collections import deque

#     def BFS(a, b):
#         q = deque()
#         q.append(a)
#         count = 0
#         while(q):
#             for _ in range(len(q)):
#                 num = q.popleft()
#                 if (num == b): return (count + 1)
#                 if (num * 2 <= b):
#                     q.append(num * 2)
#                 if ((num * 10) + 1 <= b):
#                     q.append((num * 10) + 1)
#             count += 1
#         return (-1)

#     a, b = map(int, input().split())
#     print(BFS(a, b))
#     return
# BOJ16953()

# def BOJ1446(): # 지름길 (https://www.acmicpc.net/problem/1446)
#     import sys

#     def dfs(total, answer, current):
#         if (total >= answer or current > d):
#             return answer
#         if (current == d):
#             return total
#         else:
#             for i in range(n):
#                 if (shortcut[i][0] < current): continue
#                 answer = dfs(total + shortcut[i][2] + shortcut[i][0] - current, answer, shortcut[i][1])
#             answer = dfs(total + (d - current), answer, d)
#             return answer

#     n, d = map(int, sys.stdin.readline().split())
#     shortcut = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#     answer = 10000
#     print(dfs(0, answer, 0))
# BOJ1446()

# def BOJ11060(): # 점프 점프 (https://www.acmicpc.net/problem/11060)
#     import sys
#     from collections import deque
    
#     def BFS():
#         q = deque()
#         q.append(0)
#         visit[0] = 1
#         count = 1
#         while (q):
#             for _ in range(len(q)):
#                 cur_idx = q.popleft()
#                 for i in range(a[cur_idx], -1, -1):
#                     if (cur_idx + i >= n): return count
#                     if (visit[cur_idx + i]): continue
#                     q.append(cur_idx + i)
#                     print(q)
#             count += 1
#         return -1

#     n = int(input())
#     a = list(map(int, sys.stdin.readline().split()))
#     visit = [0] * n
#     if (n == 1):
#         print(0)
#     else:
#         print(BFS())
# BOJ11060()

# def BOJ14226(): # 이모티콘(https://www.acmicpc.net/problem/14226)
#     from collections import deque

#     q = deque()
#     q.append((0, 1, 0))         # 행동(0: 복사, 1: 붙여넣기, 2: 삭제), 이모티콘 수, 클립보드 수
#     while (q):
#         for _ in range(len(q)):
#             act, emotion, clipboard = q.popleft()
#             for i in range(3):
                
#     return
# BOJ14226()

# def BOJ2178():  # 미로탐색(https://www.acmicpc.net/problem/2178)
#     import sys
#     from collections import deque

#     def BFS():
#         count = 1
#         dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         q = deque()
#         q.append((0, 0))
#         while (q):
#             for _ in range(len(q)):
#                 r, c = q.popleft()
#                 if (r == n - 1 and c == m -1): return count
#                 for i, j in dir:
#                     n_r, n_c = r + i, c + j
#                     if (not(0 <= n_r < n and 0 <= n_c < m)): continue
#                     if (maze[n_r][n_c] == 0):continue
#                     q.append((n_r, n_c))
#                     maze[n_r][n_c] = 0
#             count += 1

#     n, m = map(int, sys.stdin.readline().split())
#     maze = []
#     for i in range(n):
#         maze.append(list(map(int, sys.stdin.readline().strip())))
#     print(BFS())
#     return
# BOJ2178()

# def BOJ1697():	# 숨바꼭질 (https://www.acmicpc.net/problem/1697)
# 	from collections import deque
	
# 	def bfs(n, k):
# 		visit = [0] * 100001
# 		q = deque()
# 		q.append(n)
# 		visit[n] = 1
# 		time = 0
# 		while q:
# 			for _ in range(len(q)):
# 				now = q.popleft()
# 				if now == k: return time
# 				if ((now - 1) >= 0 and visit[now - 1] == 0):
# 					q.append(now - 1)
# 					visit[now - 1] = 1
# 				if ((now + 1) < 100001 and visit[now + 1] == 0):
# 					q.append(now + 1)
# 					visit[now + 1] = 1
# 				if ((now * 2) < 100001 and visit[now * 2] == 0):
# 					q.append(now * 2)
# 					visit[now * 2] = 1
# 			time += 1
			
# 	n, k = map(int, input().split())
# 	print(bfs(n, k))
# BOJ1697()

# def BOJ18428():	# 감시 피하기 (https://www.acmicpc.net/problem/18428)
# 	import sys
# 	input = sys.stdin.readline

# 	def check_sub(x, y, dir):
# 		for dx, dy in dir:
# 			if (corridor[x+dx][y+dy] == 'S'):
# 				return 1
# 			return check_sub(x+dx, y+dy, dir)
# 		return 0

# 	def check():
# 		dir1 = [(0, -1), (0, 1)]
# 		dir2 = [(-1, 0), (0, 1)]
# 		for x, y in teacher:
# 			if (check_sub(x, y, dir1)):
# 				return 1
# 			elif (check_sub(x, y, dir2)):
# 				return 1
# 		return 0

# 	n = int(input().strip())
# 	corridor = [input().split() for _ in range(n)]
# 	candi = list([i, j] for i in range(n) for j in range(n) if corridor[i][j] == 'X')
# 	teacher = list([i, j] for i in range(n) for j in range(n) if corridor[i][j] == 'T')

# 	def f(depth, c):
# 		if (depth == 3):
# 			if (check()): return 1
# 		else:
# 			for idx, x, y in enumerate(candi[c:]):
# 				if (corridor[x][y] != 'X'): continue
# 				corridor[x][y] = 'O'
# 				f(depth + 1, c + 1)
# 				corridor[x][y] = 'X'
# BOJ18428()

# def BOJ1189():	# 컴백홈 (https://www.acmicpc.net/problem/1189)
# 	import sys
# 	input = sys.stdin.readline

# 	def dfs(x, y, distance, count):
# 		if distance > k: return
# 		if (x, y) == (0, c - 1):
# 			if distance == k:
# 				count[0] += 1
# 			return
# 		info[x][y] = distance
# 		for i, j in dir:
# 			if 0 <= x + i < r and 0 <= y + j < c:
# 				if info[x + i][y + j] == '.':
# 					dfs(x + i, y + j, distance + 1, count)
# 					info[x + i][y + j] = '.'
# 		return

# 	r, c, k = map(int, input().split())
# 	info = [list(input().strip()) for _ in range(r)]
# 	dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 	count = [0]
# 	info[r - 1][0] = 1
# 	dfs(r - 1, 0, 1, count)
# 	print(count[0])
# 	return
# BOJ1189()

# def BOJ5547():	# 일루미네이션 (https://www.acmicpc.net/problem/5547)
# 	import sys
# 	sys.setrecursionlimit(10405)
# 	input = sys.stdin.readline

# 	def dir(idx):	# 1st idx is 0
# 		if idx % 2:	# idx is odd
# 			return [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
# 		else:
# 			return [(0, -1), (-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1)]
	
# 	def fill(x, y):
# 		city[x][y] = 2
# 		for i, j in dir(x):
# 			if ((0 <= x + i < h + 2) and (0 <= y + j < w + 2) and (city[x + i][y + j] == 0)):
# 				fill(x + i, y + j)

# 	def decorate(x, y):
# 		city[x][y] = 3
# 		for i, j in dir(x):
# 			if (0 <= x + i < h + 2) and (0 <= y + j < w + 2):
# 				if city[x + i][y + j] == 2: 
# 					count[0] += 1
# 				elif city[x + i][y + j] == 1:
# 					decorate(x + i, y + j)

# 	w, h = map(int, input().split())
# 	city = [[0] * (w + 2)] + \
# 		[[0] + list(map(int, input().split())) + [0] for _ in range(h)]\
# 			+ [[0] * (w + 2)]
# 	fill(0, 0)
# 	count = [0]
# 	for i in range(h + 2):
# 		for j in range(w + 2):
# 			if city[i][j] == 1:
# 				decorate(i, j)
# 	print(count[0])
# BOJ5547()

# def BOJ5547_2():	# 일루미네이션 2nd (https://www.acmicpc.net/problem/5547)
# 	import sys
# 	sys.setrecursionlimit(10405)
# 	input = sys.stdin.readline
	
# 	def outside(x, y):
# 		city[x][y] = 2
# 		for i, j in dir[x % 2]:
# 			if ((0 <= x + i < h + 2) and (0 <= y + j < w + 2)):
# 				if city[x + i][y + j] == 1: 
# 					count[0] += 1
# 				if city[x + i][y + j] == 0:
# 					outside(x + i, y + j)

# 	odd = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
# 	even = [(0, -1), (-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1)]
# 	dir = {0 : even, 1 : odd}

# 	w, h = map(int, input().split())
# 	city = [[0] * (w + 2)] + \
# 		[[0] + list(map(int, input().split())) + [0] for _ in range(h)]\
# 			+ [[0] * (w + 2)]
# 	count = [0]
# 	outside(0, 0)
# 	print(count[0])
# BOJ5547_2()

# def BOJ1034():	# 램프 (https://www.acmicpc.net/problem/1034) -> 2진법 xor, and 연산 활용 1차원 배열로 풀기
# 	import sys

# 	def toggle_col(m):
# 		for i in range(n):
# 			desk[i][m] = (desk[i][m] + 1) % 2

# 	def check_row(n):
# 		for j in range(m):
# 			if not(desk[n][j]):
# 				return 0
# 		return 1

# 	def check():
# 		count = 0
# 		for i in range(n):
# 			count += check_row(i)
# 		return (count)

# 	def backtrack(count, answer):
# 		if (count == k):
# 			answer = max(check(), answer)
# 		else:
# 			for i in range(m):
# 				toggle_col(i)
# 				answer = backtrack(count + 1, answer)
# 				toggle_col(i)
# 		return answer

# 	input = sys.stdin.readline
# 	n, m = map(int, input().split())
# 	desk = [list(map(int, input().strip())) for _ in range(n)]
# 	k = int(input().strip())
# 	if (k > m):
# 		if ((k - m) % 2):
# 			k = m - 1
# 		else:
# 			k = m
# 	answer = backtrack(0, 0)
# 	print(answer)

# BOJ1034()

# def BOJ1034_2():	# 램프 2진법 xor, and 연산 활용 1차원 배열로 풀기
# 	import sys

# 	def check():
# 		total = 0
# 		total_bit = desk_bit[0]
# 		for i in range(m):
# 			total_bit &= desk_bit[i]
# 		while total_bit:
# 			total += total_bit % 2
# 			total_bit //= 2
# 		return total

# 	def backtrack(answer, count):
# 		if (count == k):
# 			answer[0] = max(check(), answer[0])
# 		else:
# 			for i in range(m):
# 				desk_bit[i] ^= ((2 ** n) - 1)
# 				backtrack(answer, count + 1)
# 				desk_bit[i] ^= ((2 ** n) - 1)

# 	input = sys.stdin.readline
# 	n, m = map(int, input().split())
# 	desk = [list(map(int, input().strip())) for _ in range(n)]
# 	desk = list(zip(*desk))
# 	desk_bit = [0] * m
# 	for i in range(m):
# 		for j in range(n):
# 			desk_bit[i] += desk[i][j] * (2 ** (n - j - 1))
# 	k = int(input().strip())
# 	answer = [0]
# 	if (k > m):
# 		if ((k - m) % 2):
# 			k = m - 1
# 		else:
# 			k = m
# 	backtrack(answer, 0)
# 	print(answer[0])
# BOJ1034_2()

# PCCP 1회 문제 (콘센트 문제)
# def solution(sockets, cnt1, cnt2):
# 	# class Param:
# 	# 	def __init__(self):
# 	# 		self.answer = 0
# 	# 		self.cnt1 = 0
# 	# 		self.cnt2 = 0
# 	# p = Param()

# 	answer = [0]
# 	count1 = [cnt1]
# 	count2 = [cnt2]

# 	def f(sockets, idx):
# 		if count1[0] == 0 and count2[0] == 0:
# 			answer[0] += 1
# 		elif idx == len(sockets):
# 			return
# 		else:
# 			for i in range(4):
# 				if sockets[idx] == 0:
# 					if i < 2 and count1[0] > 0:
# 						count1[0] -= 1
# 						sockets[idx] += 1
# 						print(sockets)
# 						f(sockets, idx + 1)
# 						count1[0] += 1
# 						sockets[idx] -= 1
# 					elif count2[0] > 0:
# 						if i == 2:
# 							if (0 <= idx - 1) or (sockets[idx - 1] != 1):
# 								count2[0] -= 1
# 								sockets[idx] += 1
# 								if 0 <= idx - 1:
# 									sockets[idx - 1] += 0.5
# 								f(sockets, idx + 1)
# 								count2[0] += 1
# 								sockets[idx] -= 1
# 								if 0 <= idx - 1:
# 									sockets[idx - 1] -= 0.5
# 						if i == 3:
# 							if (idx + 1 < len(sockets)) or (sockets[idx - 1] != 1):
# 								count2[0] -= 1
# 								sockets[idx] += 1
# 								if idx + 1 < len(sockets):
# 									sockets[idx + 1] += 0.5
# 								f(sockets, idx + 1)
# 								count2[0] += 1
# 								sockets[idx] -= 1
# 								if idx + 1 < len(sockets):
# 									sockets[idx + 1] -= 0.5
# 				else:
# 					f(sockets, idx + 1)
# 	f(sockets, 0)
# 	if not(answer[0]):
# 		answer[0] = -1
# 	return answer[0]

# print(solution([0, 1, 0], 2, 0))