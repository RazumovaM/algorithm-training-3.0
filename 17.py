class Dequeue:

    def __init__(self, cards):
        self.deq = cards

    def push(self, card):
        self.deq.append(card)

    def pop(self):
        if self.deq:
            s_ = self.deq[0]
            self.deq = self.deq[1:]
            return s_
        else:
            print('error')

    def front(self):
        if self.deq:
            return self.deq[0]
        else:
            print('error')

    def size(self):
        return len(self.deq)


first = Dequeue(list(map(int, input().split())))
second = Dequeue(list(map(int, input().split())))
i = 0
while first.size() * second.size() > 0:
    i += 1
    if i == 10**6:
        print('botva', end='')
        break
    else:
        if first.front() == 0 and second.front() == 9:
            first.push(first.pop())
            first.push(second.pop())
        elif first.front() == 9 and second.front() == 0:
            second.push(first.pop())
            second.push(second.pop())
        elif first.front() > second.front():
            first.push(first.pop())
            first.push(second.pop())
        elif second.front() > first.front():
            second.push(first.pop())
            second.push(second.pop())

if i < 10**6:
    if first.size() == 0:
        print(f'second {i}', end='')
    else:
        print(f'first {i}', end='')



