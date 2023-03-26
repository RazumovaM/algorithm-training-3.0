import sys
sys.setrecursionlimit(200000)

Nv, Me = list(map(int, input().split()))


graph = [[] for v in range(Nv + 1)]
for m in range(Me):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(graph_, visited_, now, comp_):
    visited_[now] = True
    comp_list[now] = comp
    for neig in graph_[now]:
        if not visited_[neig]:
            dfs(graph_, visited_, neig, comp_)


visited = [False for _ in range(Nv + 1)]
comp_list = [0 for _ in range(Nv + 1)]
comp = 1
for v_ in range(1, Nv + 1):
    if not visited[v_]:
        dfs(graph, visited, v_, comp)
        comp += 1

N1 = 0
result = list()
for v in range(1, len(graph)):
    if comp_list[v] == 1:
        result.append(v)
        N1 += 1
result.sort()
print(N1)
print(*result)


