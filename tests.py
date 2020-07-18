from tools import Vector3
import unittest

class TestVector3(unittest.TestCase):
    vector = Vector3(-1, 2.3, 5)

    def test_set_get(self):
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
        #iAdd
        val = [self.vector.x+2,
               self.vector.y+2,
               self.vector.z+2]

        self.vector += 2

        self.assertEqual(self.vector,
                         Vector3(val))

        #iSub
        val = list(map(lambda x: x-2.7, val))
        self.vector -= 2.7

        self.assertEqual(self.vector,
                         Vector3(val))

        #iMul
        val = list(map(lambda x: x*1.3, val))
        self.vector *= 1.3

        self.assertEqual(self.vector,
                         Vector3(val))

        #iFloordiv
        val = list(map(lambda x: x//1.5, val))
        self.vector //= 1.5

        self.assertEqual(self.vector,
                         Vector3(val))

        #iDiv
        val = list(map(lambda x: x/0.3, val))
        self.vector /= 0.3

        self.assertEqual(self.vector,
                         Vector3(val))

        #iMod
        self.vector %= 2
        val = list(map(lambda x: x%2, val))

        self.assertEqual(self.vector,
                         Vector3(val))

        #iPow
        val = list(map(lambda x: x**3, val))
        self.vector **= 3

        self.assertEqual(self.vector,
                         Vector3(val))

    def test_comparison_operators(self):
        self.assertTrue( self.vector == Vector3(self.vector.x,
                                                self.vector.y,
                                                self.vector.z) )

        self.assertFalse( self.vector == Vector3(self.vector.x+1,
                                                 self.vector.y,
                                                 self.vector.z) )

        self.assertFalse( self.vector != Vector3(self.vector.x,
                                                self.vector.y,
                                                self.vector.z) )

        self.assertTrue( self.vector != Vector3(self.vector.x+1,
                                                self.vector.y,
                                                self.vector.z) )

    def test_distance(self):
        self.assertEqual( self.vector.dist(self.vector+5), 75**0.5 )
        self.assertEqual( self.vector.dist([self.vector.x+5,
                                            self.vector.y-5,
                                            self.vector.z+5]),
                          75**0.5 )



if __name__ == "__main__":
    unittest.main()
