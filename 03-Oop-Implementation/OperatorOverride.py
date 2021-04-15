class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __repr__(self):
        return "<Point<{0},{1}> 0x0000017CA2C4F7F0>".format(self.x, self.y)


if __name__ == "__main__":
    point_1 = Point(10, 10)
    point_2 = Point(10, 10)
    point_1 += point_2
    point_3 = point_1 + point_2
    print(point_3)
