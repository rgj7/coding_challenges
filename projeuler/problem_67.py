triangle = []
for i in range(100):
    row = list(map(int, input().split()))
    triangle.append(row)

max_t = [triangle[0]]
for h in range(1,len(triangle)):
    l = []
    for i in range(h+1):    
        if i == 0:
            l.append(max_t[h-1][0]+triangle[h][i])
        elif i == h:
            l.append(max_t[h-1][i-1]+triangle[h][i])
        else:
            left = max_t[h-1][i-1]
            right = max_t[h-1][i]
            l.append(max(left, right)+triangle[h][i])
    max_t.append(l)
print(max(max_t[99]))
