""" Generator program returns even numbers or the word 'odd' """

def gen2(start):
    n = start
    while True:
        if n % 2 == 1:
            result = "odd"
        else:
            result = n
        yield result
        n += 1

x = gen2(1)
print "What is x holding?"
print x
print "Calling generator 8 times"

for i in range(8):
    print x.next()
