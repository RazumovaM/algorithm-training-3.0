import sys
sys.setrecursionlimit(200000)

Nv, Me = list(map(int, input().split()))


graph = [[] for v in range(Nv + 1)]
for m in range(Me):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

result = [0]

def dfs(graph_, colors_, now, color, result_):
    colors_[now] = color
    for neig in graph_[now]:
        if colors_[neig] == 0:
            dfs(graph_, colors, neig, 3 - color, result_)
        elif colors_[neig] != 0 and colors_[neig] == colors_[now]:
            result_[0] = 1

colors = [0 for _ in range(Nv + 1)]

for v_ in range(1, Nv + 1):
    if colors[v_] == 0 and result[0] == 0:
        dfs(graph, colors, v_, 1, result)

if result[0] == 1:
    print('NO')
else:
    print('YES')