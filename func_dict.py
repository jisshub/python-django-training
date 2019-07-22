
# dictionary exercise
k = [], v = []


def append_tolist(**kwargs):
    global k, v
    for key, value in kwargs.items():
        k.append(key)
        v.append(value)
    print(k)
    print(v)


append_tolist(name='ada')
