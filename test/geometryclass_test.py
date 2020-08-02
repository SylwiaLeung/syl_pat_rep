import unittest
from geometry import geometryclass

class MyTestCase(unittest.TestCase):

    def test_middle_segment(self):
        self.segment = geometryclass.Geometry()
        middle = self.segment.middle_segment([3,2], [5,6])
        self.assertEquals(middle, (4,4))

    def test_middle_segment(self):
        self.segment = geometryclass.Geometry()
        middle = self.segment.middle_segment([-5,-2], [5,6])
        self.assertEquals(middle, (0,2))
