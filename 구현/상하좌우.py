n=int(input())
x, y = 1, 1
walk = input()
for i in walk:
    if i == "R":
        if y >= n:
            continue
        else:
            y+=1
    elif i == "L":
        if y <= 1:
            continue
        else:
            y-=1
    elif i == "U":
        if x <=1:
            continue
        else:
            x -=1
    elif i == "D":
        if x >= n:
            continue
        else:
            x +=1
print(x,y)