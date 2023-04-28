class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("my name is  "+self.name)

dog = animal("doggy")
dog.speak()
