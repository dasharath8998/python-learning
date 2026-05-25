class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    def __str__(self): 
        return f"Hi, I am {self.name} and I am {self.age} years old."
    
    def greeting(self):
        return f"Hi I am {self.name}"
    

meera = Person("Merra", 29)
meera = Person("Kiran", 12)
print(meera.age, meera.name)
print(meera)
print(meera.greeting())
print(f"{Person.count} person created")