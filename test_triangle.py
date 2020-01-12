from triangle import Point, is_point_in_triangle, Triangle


def test_is_point_in_triangle():
    a = Point(0, 0)
    b = Point(2, 0)
    c = Point(0, 2)

    for method in ['area']:
        assert is_point_in_triangle(a, b, c, Point(0.5, 0.5), method)
        assert not is_point_in_triangle(a, b, c, Point(2, 2), method)

        eps = 0.001
        assert is_point_in_triangle(a, b, c, Point(0, 0), method)
        assert is_point_in_triangle(a, b, c, Point(eps, eps), method)
        assert not is_point_in_triangle(a, b, c, Point(-eps, -eps), method)
