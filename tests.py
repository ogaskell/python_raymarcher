from tools import Vector3
import unittest

class TestVector3(unittest.TestCase):
    vector = Vector3(-1, 2.3, 5)

    def test_set_get(self):
        self.assertEqual(self.vector.x, -1.0)
        self.assertEqual(self.vector.y,  2.3)
        self.assertEqual(self.vector.z,  5.0)

        self.vector.__set__(self, [0,-2,2])

        self.assertEqual(self.vector.x,  0.0)
        self.assertEqual(self.vector.y, -2.0)
        self.assertEqual(self.vector.z,  2.0)

    def test_repr(self):
        self.assertEqual(str(self.vector),
                         "<Vector3 {:f}, {:f}, {:f}>".format(self.vector.x,
                                                             self.vector.y,
                                                             self.vector.z))

    def test_unary_operators(self):
        self.assertEqual(- self.vector,
                         Vector3(-self.vector.x,
                                 -self.vector.y,
                                 -self.vector.z))

        self.assertEqual(+ self.vector, self.vector)

        self.assertEqual(abs(self.vector),
                         Vector3(abs(self.vector.x),
                                 abs(self.vector.y),
                                 abs(self.vector.z)))

    def test_binary_operators(self):
        ## Add
        self.assertEqual(self.vector + 2,
                         Vector3(self.vector.x+2,
                                 self.vector.y+2,
                                 self.vector.z+2))

        self.assertEqual(self.vector + Vector3(1,3,-1),
                         Vector3(self.vector.x+1,
                                 self.vector.y+3,
                                 self.vector.z-1))

        with self.assertRaises(TypeError):
            self.vector + "abc"

        ## Sub
        self.assertEqual(self.vector - 2,
                         Vector3(self.vector.x-2,
                                 self.vector.y-2,
                                 self.vector.z-2))

        self.assertEqual(self.vector - Vector3(1,3,-1),
                         Vector3(self.vector.x-1,
                                 self.vector.y-3,
                                 self.vector.z+1))

        with self.assertRaises(TypeError):
            self.vector - "abc"

        ## Mul
        self.assertEqual(self.vector * 2,
                         Vector3(self.vector.x*2,
                                 self.vector.y*2,
                                 self.vector.z*2))

        self.assertEqual(self.vector * Vector3(1.5,3,-1),
                         Vector3(self.vector.x*1.5,
                                 self.vector.y*3,
                                 self.vector.z*-1))

        with self.assertRaises(TypeError):
            self.vector * "abc"

        ## Floor Div
        self.assertEqual(self.vector // 1.3,
                         Vector3(self.vector.x//1.3,
                                 self.vector.y//1.3,
                                 self.vector.z//1.3))

        self.assertEqual(self.vector // Vector3(1.2,3.3,-1),
                         Vector3(self.vector.x//1.2,
                                 self.vector.y//3.3,
                                 self.vector.z//-1))

        with self.assertRaises(TypeError):
            self.vector // "abc"

        ## True Div
        self.assertEqual(self.vector / 1.3,
                         Vector3(self.vector.x/1.3,
                                 self.vector.y/1.3,
                                 self.vector.z/1.3))

        self.assertEqual(self.vector / Vector3(1.2,3.3,-1),
                         Vector3(self.vector.x/1.2,
                                 self.vector.y/3.3,
                                 self.vector.z/-1))

        with self.assertRaises(TypeError):
            self.vector / "abc"

        ## Mod
        self.assertEqual(self.vector % 2,
                         Vector3(self.vector.x%2,
                                 self.vector.y%2,
                                 self.vector.z%2))

        self.assertEqual(self.vector % Vector3(1,3,-1),
                         Vector3(self.vector.x%1,
                                 self.vector.y%3,
                                 self.vector.z%-1))

        with self.assertRaises(TypeError):
            self.vector % "abc"

        ## Pow
        self.assertEqual(self.vector ** 2,
                         Vector3(self.vector.x**2,
                                 self.vector.y**2,
                                 self.vector.z**2))

        self.assertEqual(self.vector ** Vector3(1,3,-1),
                         Vector3(self.vector.x**1,
                                 self.vector.y**3,
                                 self.vector.z**-1))

        with self.assertRaises(TypeError):
            self.vector ** "abc"

    def test_extended_assignments(self):
        pass

    def test_comparison_operators(self):
        pass

if __name__ == "__main__":
    unittest.main()
        