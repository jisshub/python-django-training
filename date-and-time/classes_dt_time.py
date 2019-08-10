# Using Classes
import datetime


class Date:
    def __init__(self, y, m, d, fmt_date):
        self.y = y
        self.m = m
        self.d = d
        self.fmt_date = fmt_date

    def convert_me(self):
        self.date = datetime.date(self.y, self.m, self.d)
        self.new = self.date.strftime('%B %d, %Y')
        print(self.new)

    def convert(self):
        self.new_dt = datetime.datetime.strptime(self.fmt_date, '%B %d, %Y')
        # dt = str(ew_dt)
        self.dt = str(self.new_dt.date())
        print(self.dt)

    def write(self):
        with open('string_date.txt', 'w') as file:
            file.write(self.new)
        with open('date.txt', 'w') as file2:
            file2.write(self.dt)


d1 = Date(2017, 12, 3, 'April 12, 2018')
