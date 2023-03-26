N = int(input())
list_ = list(map(int, input().split()))
x_min = list_[0]
x_max = x_min
y_min = list_[1]
y_max = y_min
for _ in range(1, N):
    list_ = list(map(int, input().split()))
    if list_[0] < x_min:
        x_min = list_[0]
    if list_[0] > x_max:
        x_max = list_[0]
    if list_[1] < y_min:
        y_min = list_[1]
    if list_[1] > y_max:
        y_max = list_[1]

print(f'{x_min} {y_min} {x_max} {y_max}', end='')
