def remote_control_next():
    yield 'MSNBC'
    yield 'Fox'
    yield 'CW'

itr = remote_control_next()
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

for i in itr:
    print(i)


def fib():
    a,b = 0,1

    while True:
        yield a
        a,b = b, a+b

for x in fib():
    if x > 50:
        break
    print(x)

    