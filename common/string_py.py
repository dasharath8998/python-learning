print('THis is string')
a = """Hi There
How are you"""
b = "Hi Learning python"
c = '*'

print(a)
print(b)
print(c * 9)
print(b[1])
print(b[0:5])
print(b[3:-1])
print(b[:-1])
print(b[:])
print(b[-1])
print(len(b))

txt = "The best things in life are free"
strip_ex = "  Hi there.  "
if "free" in txt:
    print('Free, is present')

print(txt.lower())
print(txt.upper())
print(txt.title())
print(strip_ex)
print(strip_ex.rstrip())
print(strip_ex.lstrip())
print(strip_ex.strip())
age = 18

msg = f"My Age is {age}"
for char in b:
    print(char)

print(msg)
price = 59
txt = f"The price is {price:.2f} dollars"
good_morning = "Good \"morning\""
print(good_morning)