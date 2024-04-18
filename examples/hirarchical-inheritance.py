class Parent:
    def method1(self):
        print("Method 1 from Parent")

class Child1(Parent):
    def method2(self):
        print("Method 2 from Child 1")

class Child2(Parent):
    def method2(self):
        print("Method 2 from Child 2")

class GrandChild(Child2, Child1):
    def method3(self):
        print("Method 3 from Children")

child1_obj = Child1()
child2_obj = Child2()
child3_obj = GrandChild()

''' This dynamic dispatch mechanism allows Python to determine the appropriate method to call
 based on the type of the object at runtime
'''
child1_obj.method1()  # Output: Method 1 from Parent
child1_obj.method2()  # Output: Method 2 from Child 1

child2_obj.method1()  # Output: Method 1 from Parent
child2_obj.method2()  # Output: Method 3 from Child 2

child3_obj.method1()  # Output: Method 1 from Parent
'''
Now, child3_obj.method2() will indeed output "Method 2 from Child 2"
because GrandChild's method resolution order (MRO) prioritizes Child2's methods
over Child1's methods due to their order in the inheritance list.
'''
child3_obj.method2()
child3_obj.method3()