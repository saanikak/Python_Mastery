
nums = [1,2,3,4,5,6,7,8]
#output - loop - condition
even = [i for i in nums if i %2 ==0 ]
print(even)

#output - loop
squares = [i**2 for i in nums]
print(squares)

#SET COMPREHENSION
s = set([2,3,3,3,1,5,56,67,7,34,4,4,5,3])
print(s)
#set comprehensions should have curly braces, NOT square brackets
set_evens = {i for i in s if i %2 == 0}
print(set_evens)

#Dictionary comprehensions
cities = ['New York', 'Mumbai', 'Paris']
countries = ['USA', 'India', 'France']

#we'll be using the 'zip' function which merges two lists together
z = zip(cities, countries)
for i, j in z:
    print(i + ' is in ' + j) 

dcomp = {i:j for i,j in zip(cities, countries)}
print(dcomp)

