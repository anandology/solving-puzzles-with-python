
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = yrange(4)
for a in y:
    print a
