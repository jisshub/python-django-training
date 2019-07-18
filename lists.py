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
