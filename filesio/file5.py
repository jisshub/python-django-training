file1 = open('names.txt')
file2 = open('phone.txt')
file3 = open('output.txt', 'a')
for each in file1:
    file3.write(each)

for each2 in file2:
    file3.write(each2)
    # file3.write(each)

# take data from a list & store to a file

empty = []
file4 = open('numbers.txt')
for each in file4:
    empty.append(each.rstrip('\n'))
# print(empty)
file5 = open('number_ver.txt', 'a')
for each in empty:
    file5.write(each + '\n')

# names = []
# file4

movies = []
f = open('movies.txt', 'w')
f.write('avengers')
