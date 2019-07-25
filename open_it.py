from csv import reader

with open('data.csv') as file:
    csv_reader = reader(file)
    for rows in csv_reader:
        print(rows)

from csv import writer

with open('data.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['d', 500])
