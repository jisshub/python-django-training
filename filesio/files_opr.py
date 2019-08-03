# empty = []
# file1 = open('sample_dir/file1.txt')
# # file1.read()
# #
# # for each in file1:
# #     print(each)
#
# # print(file1.readline(4))
#
# # storing contents to  a list and striping the new line from it.
#
# for each in file1:
#     empty.append(each.strip('\n'))
# print(empty)

# writing contents to file.


# f = open('new.txt', 'w')
# f.write('Real Madrid\nBarcelona\nIntermillan\n')
#
# f1 = open('new.txt')
# for each in f1:
#     print(each)

# reading from a file and closing it.
# f1 = open('sample_dir/text.txt')
# print(f1.read())
# f1.close()

# its really important to close the file once open it.

# next opening a file using context managers.
# to use context managers, v use with keywrd.
# n need to close the file explicitly

with open('sample_dir/text.txt') as file:
    print(file.read())

# benefit of using this context managers is they allow us to work with in the block
# and after we exit that block it automatically close the file.

# also closes the file if exceptions are thrown.

# to read contents line by line.
with open('sample_dir/text.txt') as file:
    f_contents = file.readline()
    print(f_contents)
    # print(f_contents)
    f_contents = file.readline()
    print(f_contents)

# evry time v read from file it reads the next line from the file.
# bt here print stmt ends with a new line character
# to avoid it pass an empty string at the end of print statements

with open('sample_dir/text.txt') as file:
    f_contents = file.readline()
    print(f_contents, end='')
    f_contents = file.readline()
    print(f_contents, end='')
    f_contents = file.readline()
    print(f_contents, end='')
    f_contents = file.readline()
    print(f_contents, end='')

# iterating thru lines in the file

for each in file:
    print(each, end='')
