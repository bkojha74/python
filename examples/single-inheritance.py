class Parent:
    def method1(self):
        print("Method 1 from Parent")

class Child(Parent):
    def method2(self):
        print("Method 2 from Child")

child_obj = Child()
child_obj.method1()  # Output: Method 1 from Parent
child_obj.method2()  # Output: Method 2 from Child
