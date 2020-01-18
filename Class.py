# Creating a simple class
class SimpleClass:
    '''This is indicating the simple class'''
    def __init__(self):
        self.a = 10
        self.name = 'Python_class'

'''creating class object'''
s = SimpleClass()
'''To check the instance variable present inside class'''
print(s.__dict__)




