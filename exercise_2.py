def extract_s(data):
    i = 0
    for each in data:
        if each[i] == 's':
            print(each)
        else:
            print(f"{each} not start with letter s")


data = ['sachin', 'gambhir', 'sehwag']
print(extract_s(data))

# cartesian Product

num = [1, 2, 3]
num2 = [4, 5, 6]

for i in num:
    for j in num2:
        print(i, j)


