class Person():
    name=''
    age=''
    def __init__(self,name,age):
        self.name=name
        self.age=age
Fields=[key for key in Person.__dict__.keys() if not key.startswith('__')]
print(Fields)
