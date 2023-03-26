N = int(input())
N2 = list(map(int, input().split()))
N1 = list()
b = 0

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
min_ = 1
begin = 0
end = int(len(N2))
while begin < end:

    for n2 in range(begin, N2.index(min_, begin, end) + 1):
        staq.push(N2[n2])

    begin = n2 + 1
    min_ += 1
    N1.append(staq.pop())
    while staq.back() == min_:
        N1.append(staq.pop())
        min_ += 1
    if min_ not in N2[begin:end] and staq.size() != 0:
        print('NO')
        b = 1
        break

if not b:
    print('YES', end='')







