
def remove(x, xs):
    xs = xs[:]
    xs.remove(x)
    return xs

def permutations(xs):
    if not xs: 
        return [[]]       
    else:
        return ([x] + xs1 for x in xs
                          for xs1 in permutations(remove(x, xs)))

def is_valid(queens):
    """Returns True if the given positions of queens is allowed.
    """
    n = len(queens)
    cols = range(n)
    return n == len(set(queens[i] + i for i in cols)) == len(set(queens[i] - i for i in cols))

p = permutations(range(10))
for queens in p:
    if is_valid(queens):
        print queens
        break
