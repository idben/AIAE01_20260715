# 悠遊卡做為繼承範例

class EasyCard:
    DISCOUNT: float = 1.0
    def __init__(self, card_id: str, name: str, balance: int) -> None:
        self.__card_id = card_id
        self.__name = name
        self.__balance = balance
    def get_card_id(self) -> str:
        return self.__card_id
    def get_name(self) -> str:
        return self.__name
    def get_balance(self) -> int:
        return self.__balance
    # 儲值
    def top_up(self, amount: int) -> None:
        self.__balance += amount
    # 取得折扣後的車資
    def fare(self, full_money: int) -> int:
        return int(full_money * self.DISCOUNT)
    # 付款
    def pay(self, full_money) -> int:
        money = self.fare(full_money)
        # 如果餘額不足, 要抛出錯誤, 先跳過
        self.__balance -= money
        return money

class StudendCard(EasyCard):
    DISCOUNT: float = 0.8
    # 打八折
    def __init__(self, card_id, name, balance):
        super().__init__(card_id, name, balance)

class SeniorCard(EasyCard):
    DISCOUNT: float = 0.5
    # 打五折
    def __init__(self, card_id, name, balance):
        super().__init__(card_id, name, balance)

# class TpassCard(EasyCard):
#     pass

# 車站
class FareGate:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__recoeds: list[tuple[str, int]] = []
    # 取得站名的方法
    def get_name(self) -> str:
        return self.__name
    # 收費
    def charge(self, card: EasyCard, full_money: int):
        paid = card.pay(full_money)
        self.__recoeds.append((card.get_card_id(), paid))
        print(f"{card.get_name()} 在 {self.get_name()} 出站，付款 {paid}，卡片餘額是 {card.get_balance()} 元")
    def get_total_money(self) -> int:
        total_money = 0
        for recoed in self.__recoeds:
            total_money += recoed[1]
        return total_money

gate01 = FareGate("台北車站")
card01 = EasyCard("c000001", "王小明", 500)
card02 = StudendCard("c000002", "陳小華", 500)
card03 = SeniorCard("c000003", "萬老鈴", 500)
# card04 = TpassCard("c000004", "呂先生", 500)

gate01.charge(card01, 100)
gate01.charge(card02, 100)
gate01.charge(card03, 100)
# gate01.charge(card04, 100)
print(gate01.get_total_money())