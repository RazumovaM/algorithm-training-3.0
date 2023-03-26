import sys
import queue as que
sys.setrecursionlimit(200000)

Nv = int(input())

graph = [[] for v in range(Nv + 1)]
for v in range(1, Nv + 1):
    list_m = list(map(int, input().split()))
    for m in range(len(list_m)):
        if list_m[m] == 1:
            graph[v].append(m + 1)

v_start, v_fin = list(map(int, input().split()))
queue_ = que.Queue()
steps = [-1 for _ in range(Nv)]

queue_.put(v_start)
step = 0
steps[v_start - 1] = step
while not queue_.empty():
    step += 1
    g = queue_.get()
    for v_ in graph[g]:
        # print(v_)
        if steps[v_ - 1] == -1:
            steps[v_ - 1] = steps[g - 1] + 1
            queue_.put(v_)

print(steps[v_fin - 1])
