
def remove(x, xs):
    xs = xs[:]
    xs.remove(x)
    return xs

def permutations(xs):
    if not xs:
        return [[]]
    else:
        return [[x] + xs1 for x in xs 
                          for xs1 in permutations(remove(x, xs))
                          if can_add(x, xs1)]

def find_not_allowed(queens):
    """Given list of queens, returns an iterator over all the positions that
    are not allowed to place the next queen in.
    """
    n = len(queens)
    for i, q in enumerate(queens):
        d = n-i 
        yield q
        yield q+d
        yield q-d

def place(initial, size, result):
    if len(initial) == size:
        result.append(initial)
    else:
        not_allowed = set(find_not_allowed(initial))
        allowed = [q for q in range(size) if q not in not_allowed]
        for q in allowed:
            place(initial + [q], size, result)
    return result

counter = 0
def can_add(x, xs):
    global counter
    counter += 1
    return True
    return all(abs(x-x2) != i+1 for i, x2 in enumerate(xs))

def is_valid(queens):
    """Returns True if the given positions of queens is allowed.
    """
    n = len(queens)
    cols = range(n)
    return n == len(set(queens[i] + i for i in cols)) == len(set(queens[i] - i for i in cols))

def solve1(n):
    """This solves using brute-force.
    """
    for queens in permutations(range(n)):
        if is_valid(queens):
            yield queens

def main():
    #print sum(1 for x in permutations(range(9)))
    #print counter
    #for x in solve1(8):
    #    print x
    for queens in place([], 12, []):
        print queens

if __name__ == "__main__":
    main()

