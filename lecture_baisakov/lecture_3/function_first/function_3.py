def solve(numheads: int, numlegs: int) -> str:
    if numheads >= numlegs or numlegs % 2 == 1:
        return 'No solution'
    if numheads * 4 > numlegs and numheads * 2 > numlegs:
        return 'you have really interesting farm'
    
    rabbit = 0
    chicken = 0
    while (numlegs - numheads * 2 != 0):
        rabbit += 1
        numheads -= 1
        numlegs -= 4
        
    chicken = numheads
    
    return f'rabbit : {rabbit} chicken : {chicken}'

print(solve(4, 12))    