
def read_sudoku(filename):
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def find_empty_position(grid):
    for ri in range(9):
        for ci in range(9):
            if grid[ri][ci] == '.':
                return (ri, ci)

def get_row(grid, pos):
    ri, ci = pos
    return grid[ri]

def get_col(grid, pos):
    ri, ci = pos
    return [grid[ri][ci] for ri in range(9)]

def get_block(values, pos):
    ri, ci = pos

    br0 = 3 * (ri/3)
    bc0 = 3 * (ci/3)
    return [grid[br0+r][bc0+c] for r in range(3) for c in range(3)]

def find_possible_values(grid, pos):
    return set("123456789") \
        - set(get_row(grid, pos)) \
        - set(get_col(grid, pos)) \
        - set(get_block(grid, pos))

def solve(grid):
    pos = find_empty_position(grid) 
    if not pos:
        return grid

    ri, ci = pos
    for n in find_possible_values(grid, pos):
        grid[ri][ci] = n
        soln = solve(grid)
        if soln:
            return soln

    # failed to find a solution
    # put the original value back
    grid[ri][ci] = '.'

def group(xs, n):
    return [xs[i:i+n] for i in range(0, len(xs), n)]

def display(values):
    #grid = dict2grid(values)
    print "\n".join("".join(row) for row in grid)

if __name__ == "__main__":
    import sys
    grid = read_sudoku(sys.argv[1])

    #print grid
    display(grid)
    soln = solve(grid)
    print
    print "SOLUTION"
    display(soln)

    
