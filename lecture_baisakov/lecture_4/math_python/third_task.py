from math import tan, pi

n, s = int(input('Input number of sides: ')), float(input('Input the length of a side: '))
area = (1 / 4) * n * s ** 2 * (1 / tan(pi / n))

print(f'The area of the polygon is: {int(area)}')
