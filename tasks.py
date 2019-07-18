# Dictionaries

artist = {'first': 'Neil', 'last': 'Young', 'age': 34, 'insrtuctor': 'Colt Steele'}
full_name = artist['first'] + ' ' + artist['last']
print(full_name)
for key, value in artist.items():
    print(f"Key is {key} and Value is {value}")

# Exercise
# Totaling Donations
total = 0


def donations_total(data):
    global total
    for value in data.values():
        total += value
    return total


# dictionaries

# {}.fromkeys('age', 10)

data = {}.fromkeys(range(1, 10), 'unknown')

# get method of dictionaries- retrieves the value of a key
data.get(3)
movie = dict(name='SpiderMan', release_date='10/02/2019', actor='Ajith')


movie.get('name')

# movie.get('name') and movie['name'] returns the same result
# movie.clear() :- to clear the entire dictionary. ie makes it an empty dictionary

donations = dict(sam=25, lena=88, chuck=13, linus=99.5)
print(donations_total(donations))


# functions

# allows us to reuse the code


# here v need to make changes to all line of code
# print('hello greed')
# print('hello greed')
# print('hello greed')
# print('hello greed')

# instead use functions and just make a change in print() and later execute  the fucntion no of times v need.
def hello_func():
    print('hello greed')


hello_func()
hello_func()
hello_func()
hello_func()


def return_it():
    return 'data'


print(return_it())


def list_remove(data):
    return data.pop()


print(list_remove([4, 5, 6, 8]))


def append_to_list(sales_data):
    for value in sales_data.values():
        print(value)


sales_dict = dict(lg=1000, huawei=2000, hp=400, dell=1330)
print(append_to_list(sales_dict))




