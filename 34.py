import sys
sys.setrecursionlimit(200000)

Nv, Me = list(map(int, input().split()))

graph = [[] for v in range(Nv + 1)]

for m in range(Me):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)

result = list()
result_1 = [0]

def dfs(graph_, colors_, now, result_, result_1_):
    colors_[now] = 1
    for neig in graph_[now]:
        if colors_[neig] == 0:
            dfs(graph_, colors, neig, result_, result_1_)
            colors_[neig] = 2
        elif colors_[neig] == 1:
            result_1_[0] = -1
    colors_[now] = 2
    result_.append(now)


colors = [0 for _ in range(Nv + 1)]

for v_ in range(1, Nv + 1):
    if colors[v_] == 0:
        dfs(graph, colors, v_, result, result_1)
result.reverse()
if result_1[0] != -1:
    print(*result)
else:
    print(-1)

