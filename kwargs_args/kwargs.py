def person(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


person(name='jiss', age=23, location='kochi')

