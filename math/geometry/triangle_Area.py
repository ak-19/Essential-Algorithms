def triangle_area_determinant(p1,p2,p3):
    """
    Calculate the area of a triangle given its vertices p1, p2, and p3.
    Each point is represented as a tuple (x, y).
    expanded determinant method
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def triangle_area_crossproduct(p1,p2,p3):
    """
    Calculate the area of a triangle given its vertices p1, p2, and p3.
    Each point is represented as a tuple (x, y).
    cross product / shoelace formula method
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))/2