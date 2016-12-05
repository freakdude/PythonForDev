def yieldtest(cdown):
    i = cdown
    while i >= 0:
        yield i
        i -=1

x = yieldtest(10)
while True:
        print x.next()
