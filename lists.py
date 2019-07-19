types = ['A+', 'B+', 'O+']
for blood in types:
    print(blood)

prices = [4000, 3000, 10000, 1000, 8000]
for each in prices:
    if each > 7000 and each <= 10000:
        print('costlier')
    elif each > 5000 and each <= 7000:
        print('not so cost')
    else:
        print('less xpensive')

# Slices

prices = [4000, 3000, 10000, 1000, 8000]
print(prices[0::2])

print(prices[0:-2])

print(prices[::-1])

# list methods

# append

weights = []
weights.append(50)

# len functions
len(weights)

# max nd min functions
print(max(weights))
print(min(weights))

# sorting a list
sorted(weights)

# sorting in reverse order
sorted(weights, reverse=True)

# join method
# takes an iterable of string values ie a list of string values and joins
# a string b/w each item of the list.
# o/p is a new string
# note: iterables shud be string values.

# Examples:

email = ['jissmon', 'gmail.com']
after_join = "@".join(email)
print(after_join)


def jointhem(data):
    after_join = "-".join(data)
    return after_join


data = ['4589', '7278', '5673', '5934']
phone = jointhem(data)
print(phone)



