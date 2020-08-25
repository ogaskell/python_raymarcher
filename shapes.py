from tools import Vector3, distance, ORIGIN

class Sphere:
    def __init__(self, center: Vector3, radius: int, color=127):
        self.C = center
        self.R = radius

        self.color = color

    def __repr__(self):
        return "Sphere at "+str(self.C)

    def dist(self, pos: Vector3):
        return distance(self.pos, pos) - self.radius

class Cuboid:
    def __init__(self, center: Vector3, semisize: Vector3, color=255):
        self.C = center
        self.R = semisize

        self.color = color

    def __repr__(self):
        return "Cuboid at "+str(self.C)

    def dist(self, P: Vector3):
        rel_P = abs(P) - self.R
        Q = rel_P - self.R

        return Q.max(0).dist()
