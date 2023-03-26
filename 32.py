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
    comp_dict[comp].append(now)
    for neig in graph_[now]:
        if not visited_[neig]:
            dfs(graph_, visited_, neig, comp_)


visited = [False for _ in range(Nv + 1)]
comp = 1
comp_dict = {1: []}
for v_ in range(1, Nv + 1):

    if not visited[v_]:
        comp_dict[comp] = []
        dfs(graph, visited, v_, comp)
        comp += 1

print(comp - 1)

for i in comp_dict:
    print(len(comp_dict[i]))
    comp_dict[i].sort()
    print(*comp_dict[i])






