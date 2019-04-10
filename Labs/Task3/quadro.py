import point
class quadro:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def is_point_inside(self, p):
        return (p.x > self.v1.x and p.x < self.v2.x and p.y > self.v1.y and p.y < self.v2.y)
