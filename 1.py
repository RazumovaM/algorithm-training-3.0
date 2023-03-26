d = dict()
max_value = 1
with open('input.txt', encoding='utf-8') as file:
      for line in file.readlines():
            for n in list(line.strip()):
                  if n != ' ':
                        if n in d.keys():
                              d[n] += 1
                              if d[n] >= max_value:
                                    max_value = d[n]
                        else:
                              d[n] = 1
for m in range(max_value-1, -1, -1):
      for d_ in sorted(d):
            if d[d_] > m:
                  print('#', end='')
            else:
                  print(' ', end='')
      print()
print(''.join(sorted(d)), end='')
