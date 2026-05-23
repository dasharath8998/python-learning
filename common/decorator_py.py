def changecase(func):
    return (func().upper())
  
#   def myinner():
#   return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())