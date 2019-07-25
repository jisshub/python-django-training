# files

# # data can be stored permanently in files
#
# #  opening a sample text file
# # use an open functions
# f = open('sample.txt', 'r')
# print(f.mode)
#
# # new = open('../tasks.py', 'r')
# # print(new)
#
# # # to read the first line of the file.
# # print(f.readline())
# #
# # # can also specify no of limit to be read
# # print(f.readline(5))
#
# # reads the entire data
# print(f.read())


f = open('sample3.txt')
# print(f.read())
for each in f:
    val = int(each)
    # print(val)
    if val % 2 is 0:
        print(val)
    # print(type(each))
    # print(each)
    # if type(each) == str:

# write to  a file


