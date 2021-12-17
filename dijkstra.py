### 다익스트라 알고리즘

# def BOJ1753(): # 최단경로 (https://www.acmicpc.net/problem/1753)
    # import sys
    # from heapq import heappush, heappop
    # from collections import defaultdict

    # v, e = map(int, input().split())
    # start = int(input())

    # graph = defaultdict(list)
    # for _ in range(e):
    #     a,b,c = map(int, sys.stdin.readline().split())
    #     graph[a].append([b,c])

    # min_dist = []
    # heappush(min_dist, (0,start)) # 0이 가장 작은 수 이므로 시작의 우선순위는 0으로
    # dp = [1000001]*(v+1) # idx = 노드번호
    # dp[start] = 0
    # while min_dist:       # DFS,BFS 와 같은 느낌. 후보군을 heapq 에 넣는다.
    #     weight, node = heappop(min_dist)
    #     # if dp[node] > weight : # 지금 거리가 DP 에 저장되어있는 값보다 작은 경우
    #     for goal, distance in graph[node]: 
    #         # print('graph',graph)
    #         # print('dp, goal',dp, goal)
    #         if dp[goal] > weight + distance: # 지금 노드의 최소거리(weight) + 그 노드에서 목적 노드의 거리(distance)
    #             dp[goal] = weight + distance    # 작으면 갱신, 크면 스킵 (최단거리를 구하는 것이므로)
    #             heappush(min_dist, (weight + distance, goal))

    # for i in range(1,v+1):
    #     if dp[i] == 1000001: print("INF")
    #     else: print(dp[i])
# BOJ1753()