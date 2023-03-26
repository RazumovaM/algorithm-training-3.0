N = int(input())
list_ = list(map(int, input().split()))
heap = list()

def add(heap, n):
    heap.append(n)
    child = len(heap) - 1
    parent = (child - 1) // 2
    while child > 0 and heap[child] < heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = (child - 1) // 2

def del_(heap):
    result = heap[0]
    heap[0] = heap[-1]
    i = 0
    if len(heap) == 1:
        result = heap[0]
        heap.clear()
        return result
    while i * 2 + 2 < len(heap):
        min_son_ind = i * 2 + 2
        if heap[i * 2 + 2] > heap[i * 2 + 1]:
            min_son_ind = i * 2 + 1
        if heap[min_son_ind] < heap[i]:
            heap[i], heap[min_son_ind] = heap[min_son_ind], heap[i]
        i = min_son_ind
    heap.pop()
    return result

for l in list_:
    add(heap, l)

result = list()
while heap:
    result.append(del_(heap))
print(*result)