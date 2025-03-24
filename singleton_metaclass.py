class SingletonMeta(type):
     _instances = {}
 
     def __call__(cls, *args, **kwargs):
         if cls not in cls._instances:
             cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
         return cls._instances[cls]
 
 class MyTestClass(metaclass=SingletonMeta):
     def __init__(self, valor):
         self.valor = valor
 
 if __name__ == "__main__":
     x = MyTestClass("Initial value")
     y = MyTestClass("Different value") # This will not change the value of the first instance
 
     print("x.valor:", x.valor) # Output: Initial value
     print("y.valor:", y.valor) # Output: Initial value, since x and y are the same instance
     print("Are x and y the same?", x is y) # Output: True, both variables point to the same instance
