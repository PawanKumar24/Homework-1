from datetime import date


def calculateAge(birthDate, today):
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


print("Birthday Calculator")

print("Current day")
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
currentDay = date(year, month, day)

print('Birthday')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
birthday = date(year, month, day)

age = calculateAge(birthday, currentDay)

if age:
    print(f'You are {age} years old.')
else:
     print("Happy Birthday!")
