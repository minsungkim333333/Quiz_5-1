class Bread:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total = 0

    def sell(self):
        print(self.contents + "을" + str(self.price) + "에 팔았습니다.")
        self.total = self.total + self.price

    def eat(self):
        print(self.contents + "붕어빵을 먹습니다.")

슈크림붕어빵 = Bread("슈크림", 1500)
팥붕어빵 = Bread("팥", 500)
민트붕어빵 = Bread("민트", 240000)
슈크림붕어빵.sell()
슈크림붕어빵.sell()
슈크림붕어빵.eat()
print(슈크림붕어빵.total)

팥붕어빵.sell()
팥붕어빵.sell()
팥붕어빵.eat()
print(팥붕어빵.total)

민트붕어빵.sell()
민트붕어빵.sell()
민트붕어빵.sell()
민트붕어빵.sell()
민트붕어빵.eat()
민트붕어빵.eat()
민트붕어빵.eat()
민트붕어빵.eat()
민트붕어빵.eat()
print(민트붕어빵.total)


