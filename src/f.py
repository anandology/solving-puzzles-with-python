
def square(a):
    print "square", a
    return a * a

def foo():
    return (square(a) for a in range(10))

f = foo()
print f.next()
