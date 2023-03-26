A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))
C = list(map(int, input().split(':')))

t_sec_24 = 60 * 60 * 24
A_sec = (60 * A[0] + A[1]) * 60 + A[2]
B_sec = (60 * B[0] + B[1]) * 60 + B[2]
C_sec = (60 * C[0] + C[1]) * 60 + C[2]

if C_sec < A_sec:
    C_sec += t_sec_24


result_sec = ((C_sec - A_sec) / 2 + B_sec) % t_sec_24
h = result_sec // 3600
m = (result_sec - h * 3600) // 60
s = result_sec - h * 3600 - m * 60

h = int(h // 1 if h - h // 1 < 0.5 else h // 1 + 1)
m = int(m // 1 if m - m // 1 < 0.5 else m // 1 + 1)
s = int(s // 1 if s - s // 1 < 0.5 else s // 1 + 1)
if s == 60:
    s = 0
    m += 1
if m == 60:
    m = 0
    h += 1
if h == 24:
    h = 0

print(f'{"{:02d}".format(h)}:{"{:02d}".format(m)}:{"{:02d}".format(s)}', end='')
