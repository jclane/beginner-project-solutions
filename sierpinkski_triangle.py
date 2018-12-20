# If you're like me and I couldn't even figure out what you were
# supposed to do...
#
# All you need to do is draw a triangle.  Then find the mid-point
# between two lines and draw a line between them.  You now have
# another triangle within the first triangle.  Just use recursion
# to keep drawing triangles and you're done.

from turtle import Turtle, Screen


def draw_triangle(points, my_turtle):
    """
    Draws the triangle in the window.

    :param points: List of points to draw between
    :param my_turtle: Turtle object
    """
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])


def get_mid_point(point_a, point_b):
    """Returns the half-way point between two points"""
    return ((point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2)


def sierpinkski(points, depth, my_turtle):
    """
    Draws the intial triangle then calls itself to draw the
    inner triangles.

    :param points: List of points to draw between
    :param depth: Indicates how many times to call itself
    :param my_turtle: Turtle object
    """
    draw_triangle(points, my_turtle)
    if depth > 0:
        sierpinkski([points[0], get_mid_point(points[0], points[1]),
                        get_mid_point(points[0], points[2])],
                    depth - 1, my_turtle)
        sierpinkski([points[1], get_mid_point(points[0], points[1]),
                        get_mid_point(points[1], points[2])],
                    depth - 1, my_turtle)
        sierpinkski([points[2], get_mid_point(points[2], points[1]),
                        get_mid_point(points[0], points[2])],
                    depth - 1, my_turtle)


my_turtle = Turtle()
window = Screen()
points = [[-200,-100], [0,200], [200, -100]]
sierpinkski(points, 5, my_turtle)
window.exitonclick()
