singles = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tenths = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

# one thousand = 11
sum = 11

for i in range(1,1000):
    s = ""
    h = i//100
    if h > 0:
        s += singles[h-1]
        s += "hundred"
    i -= h*100
    t = i//10
    o = i%10
    if t > 1:
        if h > 0:
            s += "and"
        s += tenths[t-1]
        if o > 0:
            s += singles[o-1]
    elif t == 1:
        if h > 0:
            s += "and"
        if o > 0:
            s += teens[o-1]
        else:
            s += tenths[0]
    else:
        if o > 0:
            if h > 0:
                s += "and"
            s += singles[o-1]
    sum += len(s)
    print(s)
print(sum)