class Geometry:

    # Determining the midpoint of a segment
    @staticmethod
    def middle_segment(point1: tuple, point2: tuple) -> tuple:
        (x1, y1) = point1  # coordinate of the point1
        (x2, y2) = point2  # coordinate of the point2
        A = (x1 + x2) / 2
        B = (y1 + y2) / 2
        return (A, B)

    # Checks for a collision between two rectangles. Takes top left coordinate (l) and bottom right coordinate (r)
    @staticmethod
    def check_collision_between_rectangle(left_point1: tuple, right_point1: tuple,
                                          left_point2: tuple, right_point2: tuple) -> bool:

        x1, y1 = left_point1  # coordinate of the left_point1
        x2, y2 = right_point1  # coordinate of the right_point1
        x3, y3 = left_point2  # coordinate of the left_point2
        x4, y4 = right_point2  # coordinate of the right_point2

        # Checks if one rectangle is on left side of other
        if x1 >= x4 or x3 >= x2:
            return False

        # Checks if one rectangle is above other
        if y1 <= y4 or y3 <= y2:
            return False

        return True
