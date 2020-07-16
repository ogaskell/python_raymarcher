from tools import Vector3, distance

class Sphere:
    def __init__(self, center: Vector3, radius: int, color=[255,0,0]):
        self.pos = center
        self.radius = radius

        self.color = color

    def dist(self, pos: Vector3):
        return distance(self.pos, pos) - self.radius
