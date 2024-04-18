def my_decorator(funct):
    def wrapper():
        print("Something is happening before the function is called.")
        funct()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello1():
    print("Hello!")
    print("Bipin")

say_hello1()


#Parameterized decorator function
def my_parameterized_decorator(param):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator parameter: {param}")
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@my_parameterized_decorator("Hello")
def say_hello2():
    print("Hello from decorated function!")

say_hello2()


# Class based decorator
class MyClassDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Decorator executing before function.")
        result = self.func(*args, **kwargs)
        print("Decorator executing after function.")
        return result

@MyClassDecorator
def say_hello3():
    print("Hello from decorated function!")

say_hello3()


# Chaning decorator
def decorator1(func):
    def wrapper():
        print("Decorator 1 executing before function.")
        func()
        print("Decorator 1 executing after function.")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 executing before function.")
        func()
        print("Decorator 2 executing after function.")
    return wrapper

@decorator1
@decorator2
def say_hello4():
    print("Hello from decorated function!")

say_hello4()
