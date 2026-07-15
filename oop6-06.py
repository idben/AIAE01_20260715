class Sword:
    def __init__(self, sword_type: str) -> None:
        self.sword_type = sword_type

    def __add__(self, other: "Sword"):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        raise Exception("無法合成")
    

sw01 = Sword("bronze")
sw02 = Sword("bronze")
sw03 = Sword("iron")
sw04 = Sword("iron")
sw05 = sw01 + sw02
sw06 = sw03 + sw04
# sw07 = sw01 + sw04

print(sw05.sword_type)
print(sw06.sword_type)