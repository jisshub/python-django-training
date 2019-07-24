even = lambda num: num % 2 == 0
print(even(5))

# filter

numbers = range(1, 200)
odd = list(filter(lambda x: x % 2 is not 0, numbers))
print(odd)

num = list(range(3, 20))
even = list(filter(lambda num: num % 2 is 0, num))
print(even)


# map function
# without using lambda function,

def isEven(num):
    if num % 2 is 0:
        return True
    else:
        return False


even = list(filter(isEven, num))
print(even)

# filter names strts with 's'
names = ['jissmon', 'jose', 'justin', 'ajith', 'sachin']
new = (list(filter(lambda n: n[0] is 's', names)))
print(new)

# convert to upper case
new = list(map(lambda n: n.upper(), names))
print(new)

# using list comprehensions to convert to upper case
new = [each.upper() for each in names]
print(new)





#