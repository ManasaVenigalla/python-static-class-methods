class Mathutils:
    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print('This is utility class for math operations.')


# a=Mathutils
# print(a.add(3,4))
# a.description()

print(Mathutils.add(5,7))
Mathutils.description()