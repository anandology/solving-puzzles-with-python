"""Solving 8-queens problems with Python.
"""
import itertools


def is_valid(queens):
    """Returns True if the given positions of queens is allowed.
    """
    n = len(queens)
    cols = range(n)
    return n == len(set(queens[i] + i for i in cols)) == len(set(queens[i] - i for i in cols))

def solve1(n):
    """This solves using brute-force.
    """
    for queens in itertools.permutations(range(n)):
        if is_valid(queens):
            yield queens

def main():
    print solve1(12).next()
    #print sum(1 for x in solve1(9))
    #for x in solve1(9):
    #    print x

if __name__ == "__main__":
    main()
