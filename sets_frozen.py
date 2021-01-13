basket = {'apple', 'mango', 'apple', 'orange' , 'mango', 'apple'}
print(basket)
print(type(basket))

#iterable
for i in basket:
    print(i)

a = set()
a.add('Saanika')
a.add('Sharv')
print(a)
a.add('Sharv')
print(a)

#frozen set... you cannot add to it
fs = frozenset(a)
print(type(fs))
print(fs)

x = {'a', 'b', 'c', 'd', 'e'}
y = {'f', 'g', 'e'}

print('a' in x)
print('x' in x)

print(x)
print(y)
print()

#finding the unions of the two sets... 2 different ways
print(x|y)
print(x.union(y))
print()

#finding the intersection.. 2 different ways
print(x&y)
print(x.intersection(y))
print()

#finding the different between two sets... 2 different ways
print(x-y)
print(x.difference(y))

m = {'d', 'e'}
n = {'w', 'v', 'l'}
#see if subset or not
print(m.issubset(x))
print(m.issubset(y))

print(n.isdisjoint(x))

