def triangle_area(p1,p2,p3):
    """
    Calculate the area of a triangle given its vertices p1, p2, and p3.
    Each point is represented as a tuple (x, y).
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)


