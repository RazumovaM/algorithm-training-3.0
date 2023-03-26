N = int(input())
list_ = list(map(int, input().split()))


class Steque:

    def __init__(self, vagons=[]):
        self.nums = vagons

    def push(self, card):
        self.nums.append(card)

    def pop(self):
        return self.nums.pop()

    def back(self):
        if self.nums:
            return self.nums[-1]

    def size(self):
        return len(self.nums)


staq = Steque()
result = [-1] * N
staq.push((list_[0], 0))
for l in range(1, N):
    if list_[l] < staq.back()[0]:
        res = staq.pop()
        result[res[1]] = l
        while staq.size() > 0 and list_[l] < staq.back()[0]:
            res = staq.pop()
            result[res[1]] = l

    staq.push((list_[l], l))

print(*result, end='')
