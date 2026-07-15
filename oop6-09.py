# 覆寫比較運算子
# 以版本編號為例

class Version:
    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor
    def __str__(self) -> str:
        return f"v{self.major}.{self.minor}"
    def __eq__(self, other: object) -> bool:
        # 等於
        if not isinstance(other, Version):
            return False
        return self.major == other.major and self.minor == other.minor
    def __lt__(self, other: "Version"):
        # 小於
        if self.major == other.major:
            return self.minor < other.minor
        return self.major < other.major
    def __gt__(self, other):
        # 大於
        if self.major == other.major:
            return self.minor > other.minor
        return self.major > other.major

v20 = Version(2, 0)
v21 = Version(2, 1)
v19 = Version(1, 9)
print(v20)
print(isinstance(v20, Version)) # 判斷是否為某 class 產生的實體(物件或替身)
print(v20 > v21)
print(v19 < v20)
print(v21 == Version(2, 1))