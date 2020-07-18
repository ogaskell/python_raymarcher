import math, numbers

class Vector3:
    def __init__(self, x=0.0,y=0.0,z=0.0):
        try:
            if min( [isinstance(w, numbers.Number) for w in x] ):
                self.__set__(None, x)
            else:
                raise TypeError
        except:
            self.__set__(None, [x,y,z])

    def __repr__(self):
        return "<Vector3 {:f}, {:f}, {:f}>".format(self.x, self.y, self.z)

    def __get__(self, obj, type=None):
        return self

    def __set__(self, obj, value):
        try:
            if type(value) != type(self):
                if not min( [isinstance(x, numbers.Number) for x in value] ):
                    raise TypeError

                self.x,self.y,self.z = map(float,value)

            else:
                self = value

        except:
            raise TypeError("Must set Vector3 to either a Vector3 or a length-3 iterable")

    def max(self, value):
        return Vector3(max(self.x, value),
                       max(self.y, value),
                       max(self.z, value))

    def min(self, value):
        return Vector3(min(self.x, value),
                       min(self.y, value),
                       min(self.z, value))

    ### Unary Operators
    def __neg__(self):
        return Vector3(- self.x,
                       - self.y,
                       - self.z)

    def __pos__(self):
        return self

    def __abs__(self):
        return Vector3(abs(self.x),
                       abs(self.y),
                       abs(self.z))

    ### Binary Operators

    def __add__(self, other):
        if isinstance(other,type(self)):
            return Vector3(self.x + other.x,
                           self.y + other.y,
                           self.z + other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x + other,
                           self.y + other,
                           self.z + other)

        else:
            raise TypeError("Can only add Vector3 to Vector3 or number")

    def __sub__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x - other.x,
                           self.y - other.y,
                           self.z - other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x - other,
                           self.y - other,
                           self.z - other)

        else:
            raise TypeError("Can only subtract Vector3 or number from Vector3")

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x * other.x,
                           self.y * other.y,
                           self.z * other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x * other,
                           self.y * other,
                           self.z * other)

        else:
            raise TypeError("Can only multiply Vector3 by Vector3 or number")

    def __floordiv__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x // other.x,
                           self.y // other.y,
                           self.z // other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x // other,
                           self.y // other,
                           self.z // other)

        else:
            raise TypeError("Can only divide Vector3 by Vector3 or number")

    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x / other.x,
                           self.y / other.y,
                           self.z / other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x / other,
                           self.y / other,
                           self.z / other)

        else:
            raise TypeError("Can only divide Vector3 by Vector3 or number")

    def __mod__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x % other.x,
                           self.y % other.y,
                           self.z % other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x % other,
                           self.y % other,
                           self.z % other)

        else:
            raise TypeError("Can only modulus Vector3 by Vector3 or number")

    def __pow__(self, other):
        if isinstance(other, type(self)):
            return Vector3(self.x ** other.x,
                           self.y ** other.y,
                           self.z ** other.z)

        elif isinstance(other,numbers.Number):
            return Vector3(self.x ** other,
                           self.y ** other,
                           self.z ** other)

        else:
            raise TypeError("Can only raise Vector3 to the power of a Vector3 or number")

    ### Extended Assignments

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.x += other.x
            self.y += other.y
            self.z += other.z

        elif isinstance(other,numbers.Number):
            self.x += other
            self.y += other
            self.z += other

        else:
            raise TypeError("Can only add Vector3 to Vector3 or number")

        return self

    def __isub__(self, other):
        if isinstance(other, type(self)):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z

        elif isinstance(other,numbers.Number):
            self.x -= other
            self.y -= other
            self.z -= other

        else:
            raise TypeError("Can only subtract Vector3 or number from Vector3")

        return self

    def __imul__(self, other):
        if isinstance(other, type(self)):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z

        elif isinstance(other,numbers.Number):
            self.x *= other
            self.y *= other
            self.z *= other

        else:
            raise TypeError("Can only multiply Vector3 by Vector3 or number")

        return self

    def __ifloordiv__(self, other):
        if isinstance(other, type(self)):
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z

        elif isinstance(other,numbers.Number):
            self.x //= other
            self.y //= other
            self.z //= other

        else:
            raise TypeError("Can only divide Vector3 by Vector3 or number")

        return self

    def __itruediv__(self, other):
        if isinstance(other, type(self)):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z

        elif isinstance(other,numbers.Number):
            self.x /= other
            self.y /= other
            self.z /= other

        else:
            raise TypeError("Can only divide Vector3 by Vector3 or number")

        return self

    def __imod__(self, other):
        if isinstance(other, type(self)):
            self.x %= other.x
            self.y %= other.y
            self.z %= other.z

        elif isinstance(other,numbers.Number):
            self.x %= other
            self.y %= other
            self.z %= other

        else:
            raise TypeError("Can only modulus Vector3 by Vector3 or number")

        return self

    def __ipow__(self, other):
        if isinstance(other, type(self)):
            self.x **= other.x
            self.y **= other.y
            self.z **= other.z

        elif isinstance(other,numbers.Number):
            self.x **= other
            self.y **= other
            self.z **= other

        else:
            raise TypeError("Can only raise Vector3 to the power of a Vector3 or number")

        return self

    def sum(self):
        return self.x + self.y + self.z

    ### Comparison Operators
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        else:
            try:
                if min( [isinstance(x, numbers.Number) for x in value] ):
                    return (self.x == other[0]) and (self.y == other[1]) and (self.z == other[2])
                else:
                    raise TypeError
            except:
                raise TypeError("Can only compare Vector3 to Vector3 or length-3 iterable")

    def __ne__(self, other):
        return not self.__eq__(other)

    def dist(self, other=Vector3()):
        if not isinstance(other, type(self)):
            try:
                if min( [isinstance(x, numbers.Number) for x in other] ):
                    other = Vector3(other)
                else:
                    raise TypeError
            except:
                raise TypeError("Can only find distance between Vector3 and Vector3 or length-3 iterable")

        return math.sqrt( ((self-pos)**2).sum() )
