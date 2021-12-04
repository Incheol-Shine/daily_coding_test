### union_find 

# def BOJ1976(): # 여행가자 (https://www.acmicpc.net/submit/1976/28363407)
    # import sys
    # from collections import defaultdict

    # n = int(input())                                # 도시 개수
    # m = int(input())                                # 방문 도시 개수
    # link = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 연결관계  이차원 list
    # plan = list(map(int, sys.stdin.readline().split()))

    # # Union Find
    # parent = [x for x in range(n)]          # parent[x] = x 로 초기화

    # def find(parent,x):                            # x의 최상단 부모노드 (루트 노드) 를 찾는 함수
    #     if x == parent[x]: return x
    #     else : 
    #         y = find(parent,parent[x])
    #         parent[x] = y
    #         return y                        

    # def union(parent,x,y):                     # x,y 중 rank 가 더 높은 노드 밑에 낮은 노드를 연결해준다.   
    #     x = find(parent, x)                    # ex) x의 rank 가 더 높을 경우, y의 집합을 x의 집합에 합친다. (x가 y의 parent 가 된다.)
    #     y = find(parent, y)
    #     if x == y: return
    #     parent[y] = x


    # for i in range(n):
    #     for j in range(i+1, n):
    #         if link[i][j] == 1 : union(parent,i,j) # i, j 가 연결되어있는 경우 union() 으로 합친다.

    # ans = 'YES'
    # check = find(parent,plan[0]-1)    # 방문 계획 도시중 첫번째 도시의 union 을 check 에 저장

    # for i in plan:
    #     if find(parent, i-1) != check:     # 방문 계획 도시중 하나라도 union 이 다르면 'NO'
    #         ans = 'NO'   
    #         break

    # print(ans)
# BOJ1976()