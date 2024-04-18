'''
A generator in Python is a function that returns an iterator and generates values lazily,
one at a time, using the yield keyword. Generators are memory-efficient as they don't store
all generated values in memory at once, unlike regular functions that return a complete collection of values.

'''
def my_generator():
    yield(2)
    yield(4)
    yield(3)

gen = my_generator()
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4
print(next(gen))  # Output: 3
