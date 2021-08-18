class Unit:
    def __init__(self):
        print("unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
       # super().__init__() #다중상속이 필요할 땐 super()를 사용하지 않는 것이 좋다. 앞의 인자에 해당하는 클래스만 상속받는다. 
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
