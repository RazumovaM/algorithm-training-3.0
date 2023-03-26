l = input().split()
s = list()

for l_ in l:
    if l_.isdigit():
        s.append(int(l_))
    else:
        s_front = s.pop()
        s_back = s.pop()
        if l_ == '+':
            s.append(s_front + s_back)
        elif l_ == '*':
            s.append(s_front * s_back)
        elif l_ == '-':
            s.append(s_back - s_front)


print(s[0])
