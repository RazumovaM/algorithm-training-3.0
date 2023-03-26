heap = list()

for _ in range(int(input())):
    line = input()
    command = line.split()[0]
    if command == '0':
        heap.append(int(line.split()[1]))
        child = len(heap) - 1
        parent = (child - 1) // 2
        while child > 0 and heap[child] > heap[parent]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = (child - 1) // 2
    else:
        print(heap[0])
        heap[0] = heap[-1]
        i = 0
        while i * 2 + 2 < len(heap):
            min_son_ind = i * 2 + 2
            if heap[i * 2 + 2] < heap[i * 2 + 1]:
                min_son_ind = i * 2 + 1
            if heap[min_son_ind] > heap[i]:
                heap[i], heap[min_son_ind] = heap[min_son_ind], heap[i]
            i = min_son_ind
        heap.pop()

