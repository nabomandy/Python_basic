class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 다중 상속을 할 때는, 모든 부모에 대한 초기화가 필요할 때는 사용 x - 하나만 나온다.
        Unit.__init__(self)
        Flyable.__init__(self)
    
        
# 드랍쉽
dropship = FlyableUnit()