import unittest
from syl_pat_rep.geometry import geometryclass

class MyTestCase(unittest.TestCase):

    def test_middle_segment_01(self):
        self.segment = geometryclass.Geometry()
        middle = self.segment.middle_segment((3,2), (5,6))
        self.assertEquals(middle, (4,4))

    def test_middle_segment_02(self):
        self.segment = geometryclass.Geometry()
        middle = self.segment.middle_segment((-5,-2), (5,6))
        self.assertEquals(middle, (0,2))

    def test_check_collision_between_rectangle_01(self):
        self.rectangles = geometryclass.Geometry()
        rectangles = self.rectangles.check_collision_between_rectangle((-3, 6), (-2, 0), (1,3), (3, 1))
        self.assertEquals(rectangles, False)

    def test_check_collision_between_rectangle_02(self):
        self.rectangles = geometryclass.Geometry()
        rectangles = self.rectangles.check_collision_between_rectangle((-1, -2), (2, -5), (0, -3), (1, -4))
        self.assertEquals(rectangles, True)