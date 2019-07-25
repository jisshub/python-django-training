# to write to  a file
#
# f = open('sample4.txt', 'w')
# f.write('sdada')
#
# f = open('sample5.txt', 'w')
# f.write('dsjaada\n'
#         'adadadada')
# f = open('sample5.txt', 'r')
# print(f.read())

# to append to  a file without overwirting contents use mode as a

# f = open('sample5.txt', 'a')
# # f.write('dsadad\n'
# #         'fdfsdfsf')
#
# #
# # f.write('\nsdkhsdk\n'
# #         'khdaskda')
#
# f.write('\nsadasda'
#         '\ndsdsda')


# read from a file and write it to a file.
# f = open('sample5.txt')
# n = f.read()
# f1 = open('newfile.txt', 'w')
# # f1.write('newfile.txt', 'w')
#
# f1.write(n)

# read and write to a file

# f = open('newfile.txt')
# f1 = open('newfile_ver2.txt', 'a')
# f1.write(f.read())


# f1 = open('newfile_ver2.txt')
# f2 = open('new.txt', 'a')
# for each in f1:
#     f2.write(each)

#
# file1 = open('names.txt')
# file2 = open('phone.txt')
# file3 = open('output.txt', 'a')
# for each in file1:
#     file3.write(each)
# for each2 in file2:
#     # file3.write(each)
#     file3.write(each2)

# writin from  a list

# names = ['asd', 'adda']
# f1 = open('list.txt', 'a')
# for each in marks:
#     f1.write(each + '\n')


# marks = [45, 66, 33]
# f1 = open('numbers.txt', 'a')
# for each in marks:
#     f1.write(str(each) + '\n')