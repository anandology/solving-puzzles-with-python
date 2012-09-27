
def read_sudoku(filename):
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid2dict(grid)

def grid2dict(grid):
    d = {}
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            d[r, c] = value
    return d

def dict2grid(values):
    return [[values[r, c] for c in range(9)] for r in range(9)]

positions = [(r, c) for r in range(9) for c in range(9)]
digits = "123456789"

def find_empty_position(values):
    for pos in positions:
        if values[pos] == '.':
            return pos

def get_row(values, pos):
    r, c = pos
    return [values[r,c] for c in range(9)]

def get_col(values, pos):
    r, c = pos
    return [values[r,c] for r in range(9)]

def get_block(values, pos):
    r, c = pos

    br0 = 3 * (r/3)
    bc0 = 3 * (c/3)
    return [values[br0+r,bc0+c] for r in range(3) for c in range(3)]

def solve(grid):
    pos = find_empty_position(grid) 
    if not pos:
        return grid

    possibilities = set("123456789") \
        - set(get_row(grid, pos)) \
        - set(get_col(grid, pos)) \
        - set(get_block(grid, pos))

    grid = dict(grid)
    for n in possibilities:
        grid[pos] = n
        soln = solve(grid)
        if soln:
            return soln

def group(xs, n):
    return [xs[i:i+n] for i in range(0, len(xs), n)]

def display(values):
    grid = dict2grid(values)
    print "\n".join("".join(row) for row in grid)

if __name__ == "__main__":
    import sys
    grid = read_sudoku(sys.argv[1])

    print rows[1,2]
    print cols[1,2]

    #print grid
    display(grid)
    soln = solve(grid)
    print
    print "SOLUTION"
    display(soln)

    
