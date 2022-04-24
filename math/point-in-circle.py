def is_in_circle(point, circle):
    x, y = point
    c_x, c_y, r = circle

    return (c_x - x)**2 + (c_y - y)**2 <= r**2


print(is_in_circle([2, 2], [1, 1, 2]) == True)
print(is_in_circle([2, 2], [1, 1, 1]) == False)
