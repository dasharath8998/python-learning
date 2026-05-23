for x in range(6):
    print(x)
    # if x == 3:
    #     break
else:
    print("finally completed")

fruites = ["apple", "banana", "cherry"]

for x in fruites:
    if x == "banana":
        continue
    print(x)
