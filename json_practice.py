book = {}
book['tom'] = {'name' : 'tom', 'phone': 2323423423, 'address': '23 Osprey, NY'}
book['jack'] = {'name': 'jack', 'phone':345345345, 'address': '55 Tiana Way'}

print(book)
print(type(book))
print()

import json

s = json.dumps(book)
print(s)
print(type(s))
print()

d = json.loads(s)
print(d)
print(type(d))
print()

print(d['tom'])
print(d['tom']['address'])