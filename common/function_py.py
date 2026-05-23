def my_function():
    print("Hello from my_function")

my_function()
my_function()

def fehrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fehrenheit_to_celsius(100))

def add_first_name(fname):
    print(f"{fname} dasharath")

add_first_name("sindhav")

# Default Parameter Values

def default_name(fname = "darbar"):
    print(fname, "sindhav")

default_name()
default_name(fname = "karana")

def my_country(country="india"):
    return f"I am from {country}"

print(my_country())
print(my_country("UK"))
print(my_country("US"))

def my_function(animal, name = "test"):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
my_function( animal = "dog")

def tuple_example(*fruites):
    return f"I love {fruites[1]}"

print(tuple_example("banana","mango","apple"))