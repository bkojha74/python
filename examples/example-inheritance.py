class parent1:
    def method1(self):
        print(f"Hello from parent1 method")

class parent2:
    def method2(self):
        print(f"Hello from parent2 method")        

# Single inheritance
class child1(parent1):
    def method3(self):
        print("Hello from child1 method")  

# Multiple inheritance
class child2(parent1, parent2):
    def method4(self):
        print("Hello from child2 method")

class child3(parent1, parent2):
    def method5(self):
        print("Hello from child3 method")            

# Multilevel inheritance
class child4(child2):
    def method6(self):
        print("Hello from child4 method")

# Hirarchical inheritance
class child5(child2, child3):
    def method7(self):
        print("Hello from child5 method")

''' Multiple inheritance
# class child2(parent, child1):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases parent, child1
class child2(parent, child1):
    def method4(self):
        print("Hello from child2 method")        
'''
# single parent
ch1_obj = child1()

# multiple parents
ch2_obj = child2()
ch3_obj = child3()

# multilevel parents
ch4_obj = child4()

# Hirarchical parents
ch5_obj = child5()

if __name__ == "__main__":
    ch1_obj.method1()
    ch1_obj.method3()

    ch2_obj.method1()
    ch2_obj.method2()
    ch2_obj.method4()

    ch3_obj.method1()
    ch3_obj.method2()
    ch3_obj.method5()

    ch4_obj.method1()
    ch4_obj.method2()
    ch4_obj.method4()
    ch4_obj.method6()

    ch5_obj.method1()
    ch5_obj.method2()
    ch5_obj.method4()
    ch5_obj.method5()
    ch5_obj.method7()