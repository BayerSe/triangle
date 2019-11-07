from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def area_of_triangle(a: Point, b: Point, c: Point) -> float:
    """Computes the area of the triangle abc."""
    return abs((a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2)


def is_point_in_triangle_area(a: Point, b: Point, c: Point, p: Point) -> bool:
    """Tests whether point p is contained in the triangle abc.
    This is done by comparing the area of abc with the areas of abp, apc, and pbc.
    """
    area_abc = area_of_triangle(a, b, c)

    area_abp = area_of_triangle(a, b, p)
    area_apc = area_of_triangle(a, p, c)
    area_pbc = area_of_triangle(p, b, c)

    return isclose(area_abc, area_abp + area_apc + area_pbc)
