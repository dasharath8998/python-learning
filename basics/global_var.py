x = 'good morning'

def myFunc():
    x = "Good evening"
    global y 
    y = 'How are you!'
    print('hi,', x)

myFunc()
print(y)