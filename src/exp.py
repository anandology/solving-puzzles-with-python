
def exponent(x, n):
    if n == 0:
        return 1
    else:
        return x * exponent(x, n-1)

if __name__ == "__main__":
    import sys
    x = int(sys.argv[1])
    n = int(sys.argv[2])
    print exponent(x, n)
    
