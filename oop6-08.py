# 覆蓋 __str__，定義 print 出的內容

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def __repr__(self) -> str:
        return f"Point(x={self.x} ,y={self.y})"

p01 = Point(4, 3)
print(p01)
print(repr(p01))
print([p01])