n = int(input())
x = n + 1

for i in range(1, n + 1):
    print(f'{x * " "}{"* " * i}')
    x -= 1