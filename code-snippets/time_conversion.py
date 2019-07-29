# hour_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
hour_dt = {'12': '00', '1': '13', '2': '14', '3': '15', '4': '16', '5': '17', '6': '18', '07': '19'}
hr_key = []
hr_values = []
import re


def timeConversion(time):
    global hour_dt, hr_key
    new = time.split(':')
    # return new
    if 'PM' or 'AM' in new[2]:
        for k in hour_dt.keys():
            hr_key.append(k)

        if new[0] in hr_key:
            hour = hour_dt[new[0]]
            pattern = re.compile(r'[AM]+|[PM]+')
            time_pr = pattern.search(time).group()
            return f"{hour}:{new[1]}:{new[2].strip(time_pr)}"
    return f'{time} is invalid'


print(timeConversion('07:05:22PM'))
