M = int(input())
N = int(input())

list_ = list()

for n in range(N):

    l_ = list(map(int, input().split()))
    a = l_[0]
    b = l_[1]
    list_l = list()
    if list_:
        for l in list_:
            if (a <= l[0] <= b) or (a <= l[1] <= b) or (a >= l[0] and b < l[1]):
                list_l.append(l)
        for l in list_l:
            list_.remove(l)

    list_.append(l_)

print(len(list_), end='')
