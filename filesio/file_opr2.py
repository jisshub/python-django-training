# # using limit argument while reading
with open('sample_dir/text.txt') as f:
    f_con = f.read(150)
    print(f_con, end='')
    f_con = f.read(150)
    print(f_con)
#     # here v pass the limit as an arg to read(). so it reads first 50 chracters in the file.
#     # if again print the contents read() returns an empty string
    f_con = f.read(10)
    print(f_con)

with open('sample_dir/text.txt') as f:
    size_to_read = 150
    f_con = f.read(size_to_read)
    while len(f_con) > 0:
        print(f_con, end='')
        f_con = f.read(size_to_read)
    print('size ends')
