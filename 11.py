with open('input.txt', encoding='utf-8') as file:
    s = list()
    for line in file.readlines():
        if line.split()[0] == 'exit':
            print('bye', end='')
            break
        elif line.split()[0] == 'push':
            s.append(int(line.split()[1]))
            print('ok')
        elif line.split()[0] == 'pop':
            if s:
                print(s.pop())
            else:
                print('error')
        elif line.split()[0] == 'back':
            if s:
                print(s[-1])
            else:
                print('error')
        elif line.split()[0] == 'size':
            print(len(s))
        elif line.split()[0] == 'clear':
            s.clear()
            print('ok')