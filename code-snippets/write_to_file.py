# Writing to a file
# to mmodes: w - write mode which overwrites the content
#            a - append the new contents to the existing contents in thefile
# with open('sample_dir/write.txt', 'w') as file:
#     pass
#     # file.write('Test')
#     # file.write('idea')
#     file.write('hello')
# just using open with write mode automatically creates a file. ven though v doesnt write anything to it.


# reading and writing to a file.
# with open('sample_dir/movies') as file:
#     f_contents = file.read()
#     # print(f_contents)
# with open('sample_dir/movies_new.txt', 'w') as file2:
#     file2.write(f_contents)


# easy method to write contents to a file after reading it
with open('sample_dir/movies') as file:
    with open('sample_dir/movies_2', 'w') as file2:
        for line in file:
            # print(line, end='')
            file2.write(line)
