import sys
sys.setrecursionlimit(200000)

Nv = int(input())

graph = [[] for v in range(Nv + 1)]
for v in range(1, Nv + 1):
    list_m = list(map(int, input().split()))
    for m in range(len(list_m)):
        if list_m[m] == 1:
            graph[v].append(m + 1)

result = [0, 0, 0, 0]
result_list = list()


def dfs(graph_, colors, now, parent, result_, result_list_):
    colors[now] = 1
    for neig in graph_[now]:
        if colors[neig] == 0 and result_[0] == 0:
            dfs(graph_, colors, neig, now, result_, result_list_)
            colors[neig] = 2
            if result_[0] == 1:
                if result[2] != neig and result_[0] == 1 and result[3] == 0:
                    result_[1] += 1
                    result_list_.append(now)
                else:
                    result[3] = 1
                    break
        elif colors[neig] == 1 and parent != neig and result_[0] == 0:
            result_[0] = 1
            result_[1] = 1
            result_[2] = neig
            result_list_.append(now)

    colors[now] = 2


colors_ = [0 for _ in range(Nv + 1)]

for v_ in range(1, Nv + 1):
    if colors_[v_] == 0 and result[0] == 0:
        dfs(graph, colors_, v_, 0, result, result_list)

if result[0] == 1:
    print('YES')
    print(result[1])
    print(*result_list)
else:
    print('NO')