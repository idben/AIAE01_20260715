# 繼承的基本寫法

# 父類別
class Human:
    def __init__(self, name: str) -> None:
        self.name = name

# 子類別
class Archer(Human):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name)
        self.num_arrows = num_arrows

man01 = Human("村民一號")
print(man01.name)
man02 = Archer("弓箭手一號", 10)
print(man02.name)