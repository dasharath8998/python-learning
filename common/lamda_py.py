x = lambda a, b: a * b
print(x(5, 6))


def my_fn(n):
    return lambda a: a * n

mydoubler = my_fn(2)
print(mydoubler(5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_number = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_number)

students = [("Das", 29), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_word = sorted(words, key=lambda x: len(x))
print(sorted_word)