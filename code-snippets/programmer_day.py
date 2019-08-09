from datetime import timedelta, date


def day_of_prgm(d):
    year = d.strftime('%Y')
    if year % 4 != 0:
        current = d + timedelta(days=256)
        return current


d = date.today()
print(day_of_prgm(d))

# pd.to_timedelta(100, unit='D')
