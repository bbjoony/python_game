from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도:{2}]".format(self.name, location, self.speed))

    def damaged(self, damage): #AttckUnit 클래스에서 복사해옴
        print("{0}: {1} 대미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다".format(self.name))    

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력:{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}: {1} 대미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다".format(self.name))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0}: 시즈 모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, flying_speed)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        # print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #unit._init_(self, name, hp, 0)
        super()._init_(name, hp, 0)
        self.location = location

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        else: 
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") #good game
    print("[player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()


for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()