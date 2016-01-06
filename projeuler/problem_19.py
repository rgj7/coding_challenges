days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
sundays = 0

for y in range(1900,2001):
    for m in range(12):
        if m==1 and y%4==0 and y!=1900:
            days += 1
        days += days_in_month[m]
        if days%7==6 and y>1900:
            sundays += 1

print(sundays)