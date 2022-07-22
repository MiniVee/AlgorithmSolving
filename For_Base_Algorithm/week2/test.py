class Dog:
    sound = "멍멍"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + "가 " + Dog.sound + "하고 짖는다.")

Dog.sound = "멍멍"
a = "삽살개"
b = "진돗개"
c=Dog("삽살개")
d = Dog("진돗개")
c.bark()
d.bark()