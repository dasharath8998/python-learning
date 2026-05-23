x = 1

while x < 8:
    print(x)
    if x == 2:
        break # if condition exucated then else won't
    x += x
else:
    print("i is no longer less than 6")
