class Animal(object):
    def __init__(self, color):
        self.color = color
    def call(self):
        print("这条鱼叫大白鲨")
class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.tail = True
    def call(self):
        print("%s的鱼在吐泡泡" % self.color)
fish = Fish("银白色")
fish.call()
animal = Animal(" ")
animal.call()