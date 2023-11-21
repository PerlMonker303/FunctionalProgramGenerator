f = lambda x, y: x * y + 8 * (x + y) + 56

inputs = [(0,0), (1,0), (0,1), (1,1), (2,1), (1,2), (2,2), (3,3)]
[print(f'{inp} => {f(inp[0], inp[1])}') for inp in inputs]