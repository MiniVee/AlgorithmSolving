class Animal:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(self.name + " 먹인다.")

    def attack(self):
        print(self.name + " 공격한다.")

class Human(Animal):
    pass

class Cat(Animal):
    pass

human = Human("사람1")
human.feed()

cat = Cat("고양이")
cat.attack()



