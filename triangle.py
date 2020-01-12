from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Triangle:
    a: Point
    b: Point
    c: Point

    def get_area(self) -> float:
        """Computes the area of the triangle abc."""
        area = (
            abs(
                self.a.x * (self.b.y - self.c.y)
                + self.b.x * (self.c.y - self.a.y)
                + self.c.x * (self.a.y - self.b.y)
            )
            / 2
        )
        return area


def is_point_in_triangle(
    a: Point, b: Point, c: Point, p: Point, method: str
) -> bool:
    """Tests whether point p is contained in the triangle formed by a, b, and c."""
    if method == "area":
        return is_point_in_triangle_area(a, b, c, p)
    else:
        raise NotImplementedError(f"Method: {method} is not supported.")


def is_point_in_triangle_area(a: Point, b: Point, c: Point, p: Point) -> bool:
    """Tests whether point p is contained in the triangle formed by a, b, and c.
    This is done by comparing the area of abc with the areas of abp, apc, and pbc.
    """
    t_abc = Triangle(a, b, c)
    t_abp = Triangle(a, b, p)
    t_apc = Triangle(a, p, c)
    t_pbc = Triangle(p, b, c)

    area_triangles = t_abp.get_area() + t_apc.get_area() + t_pbc.get_area()

    return isclose(t_abc.get_area(), area_triangles)
