cars = ["Ford", "Volvo", "BMW"]

print(cars[0])

cars[0] = "Toyota"

print(cars[0])
print(f"length {len(cars)}")

for car in cars:
    print(f"loop {car}")

cars.pop(0)
print(cars)
cars.remove("BMW")
print(cars)
cars.append("Honda")
print(cars)
print(cars.count("Honda"))
print(cars.index("Honda"))