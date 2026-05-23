eligibility = True
student = False
credits = False

if eligibility or credits:
    print("eligible for loan")
elif student:
    print("still student")
else:
    print("not eligible")

if (eligibility and credits) and not student:
    print("eligibleeee")
else:
    print("not eligible")

# identify operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x is not y)

# Membership Operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)