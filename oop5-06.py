# 龍噴火攻擊
class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        # return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2
        return (
            self.pos_x >= x_1 and 
            self.pos_x <= x_2 and
            self.pos_y >= y_1 and
            self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        hit: list[Unit] = []
        for unit in units:
            if unit.in_area(
                x - self.__fire_range, 
                y - self.__fire_range, 
                x + self.__fire_range, 
                y + self.__fire_range):
                hit.append(unit)
        return hit


m01 = Dragon("龍", 7, 0, 3)
m02 = Unit("史萊姆", 2, 4)
m03 = Unit("蝙蝠怪", 4, 3)
m04 = Unit("哥布林", -1, -1)
list1 = [m01, m02, m03, m04]
print("龍使用噴火攻擊")
result = m01.breathe_fire(3, 3, list1)
for unit in result:
    print(f"  {unit.name} 受到傷害")