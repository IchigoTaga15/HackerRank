def is_leap(year):
    leap = False
    leap2 = True
    if float(year % 4) == 0:
        if float(year % 400) == 0 or (float(year % 400) == 0 and float(year % 100) == 0):
            return leap2
        elif float(year % 100) == 0:
            return leap
        else:
            return leap2
    else:
        return leap


year = int(input())
print(is_leap(year))

#print(is_leap(year))