class Parent1:
    def method1(self):
        print("Method 1 from Parent 1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent 2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Child Method")

# Create an instance of Child
child_obj = Child()

# Access methods from both Parent1 and Parent2
child_obj.method1()  # Output: Method 1 from Parent 1
child_obj.method2()  # Output: Method 2 from Parent 2
child_obj.method3()  # Output: Child Method
