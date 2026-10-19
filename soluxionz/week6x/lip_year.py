# lol! I don't think leap year is a thing, I actually use The Lunar Calendar


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False       
    elif year % 4 == 0:
        return True
    else:
        return False


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


next_year = year + 1
found = 0
leap_years = []
while found < 3:
    if is_leap_year(next_year):
        leap_years.append(next_year)
        found += 1
    next_year += 1
print("Next 3 leap years:", leap_years)
