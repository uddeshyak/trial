class student: #student is an object...
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major

    def ranking(self):
        if self.age >= 18:
            return True
        else:
            return False






