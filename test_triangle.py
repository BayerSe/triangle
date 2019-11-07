from triangle import Point, is_point_in_triangle_area


def test_is_point_in_triangle():
    a = Point(0, 0)
    b = Point(2, 0)
    c = Point(0, 2)

    assert is_point_in_triangle_area(a, b, c, Point(0.5, 0.5))
    assert not is_point_in_triangle_area(a, b, c, Point(2, 2))

    eps = 0.001
    assert is_point_in_triangle_area(a, b, c, Point(0, 0))
    assert is_point_in_triangle_area(a, b, c, Point(eps, eps))
    assert not is_point_in_triangle_area(a, b, c, Point(-eps, -eps))
