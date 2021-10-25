### BFS
# def BOJ18405(): # 경쟁적 전염 (https://www.acmicpc.net/problem/18405)
    # import sys
    # from collections import deque

    # n, k = map(int, input().split())
    # flask = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # s, x, y = map(int, input().split())

    # # bfs
    # count = 0
    # dir = [(1,0),(-1,0),(0,1),(0,-1)]

    # q = deque()
    # init_coord = []
    # for i in range(n):
    #     for j in range(n):
    #         if flask[i][j] != 0:
    #             init_coord.append((flask[i][j],i,j)) # value, 좌표

    # init_coord.sort(key=lambda x: x[0])  # value 가 작은 숫자부터 정렬
    # q.extend(init_coord)

    # while q:
    #     if count == s: break
    #     for _ in range(len(q)):
    #         value, r, c = q.popleft()
    #         for i, j in dir:
    #             n_r, n_c = r+i, c+j
                
    #             if not(0 <= n_r < n and 0 <= n_c < n): continue
    #             if flask[n_r][n_c] != 0: continue
    #             flask[n_r][n_c] = value
    #             q.append((value,n_r,n_c))
    #     count += 1

    # print(flask[x-1][y-1])

    # return
# BOJ18405()