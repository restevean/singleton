def singleton(cls):
     instances = {}
     def get_instance(*args, **kwargs):
         if cls not in instances:
             instances[cls] = cls(*args, **kwargs)
         return instances[cls]
     return get_instance
 
 @singleton
 class MySingleton:
     def __init__(self, valor):
         self.valor = valor
 
 if __name__ == "__main__":
     a = MySingleton(10)
     b = MySingleton(20) # Does not change values of first instance
 
     print(a.valor) # Output: 10
     print(b.valor) # Output: 10, a and b are the same instance
     print(a is b) # Output: True, both variables point to the same instance
