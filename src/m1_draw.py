###############################################################################
#   You are going to do a great job on this exam!
#   Read each question carefully.
#   Be sure to commit and push after each question
#   Be sure to right-click on src, and Mark Directory as Sources root
#
#
###############################################################################
import rosegraphics as rg


def main():
    #
    #   Tests are called from here.  Do not make any changes to main
    #
    test_draw_a_picture()


def test_draw_a_picture():
    ###############################################################################
    #   This method tests draw_a_picture
    #
    ###############################################################################
    point1 = rg.Point(150, 150)
    n = 10
    test_window = rg.RoseWindow(500, 500)

    #  tests draw_a_picture with point 1, n=10, and test_window
    print('###################################################')
    print('Test 1 of draw_a_picture.')
    print('Called with point1 =', point1)
    print( 'n =', n, ' color = blue')
    print('###################################################')
    draw_a_picture(point1, n, 'blue', test_window)

    point2 = rg.Point(350, 350)
    n = 4
    #  tests draw_a_picture with point 2, n =4, test_window
    print('###################################################')
    print('Test 2 of draw_a_picture.')
    print('Called with point2 =', point2)
    print( 'n =', n, ' color = green')
    print('###################################################')
    draw_a_picture(point2, n, 'green', test_window)
    test_window.close_on_mouse_click()


###############################################################################
# def draw_a_picture(point, n, color, window):
#     """
#     See   m1_draw_problem_picture.pdf   in this project for pictures
#     that may help you better understand the following specification:
#
#     What comes in:
#       -- An rg.Point.
#       -- A positive integer n.
#       -- A color
#       -- An rg.RoseWindow.
#
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#       Draws an rg.Circle with the given point as the center.
#       The radius of the rg.Circle is 100 pixels
#       Draws an rg.Rectangle with the given point as the center.
#       The width of the Rectangle is 160 pixels and the height is 80 pixels
#       Draws n lines from the Center of the Rectangle to the top line
#       of the Rectangle that are equally spaced
#       The color is used as the line colors unless the number of the line
#       is prime.  If the number of the line is prime,
#       the color should be 'orange'. The fist line drawn should be
#       the color given because one is not considered prime.
#
#       -- There is a 0.5 second pause after each rg.Circle is drawn.
#       Must  ** NOT close **   the window.
#
#     Type hints:
#       :type circle: rg.Circle
#       :type n: int
#       :type window: rg.RoseWindow
#   The is_prime function is supplied.  Do NOT change is_prime
#     """
###############################################################################
# DONE: 1  READ the doc-string for the is_prime function defined below.
# You do NOT need to understand its implementations,
# just its specification (per the doc-string).
# You should  ** CALL **  functions as needed in implementing the
# other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################


def is_prime(n):
    """
    What comes in:  An integer n >= 1.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    if n == 1:
        return False

    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True

# -------------------------------------------------------------------------
#  DONE: 2. Implement and test the draw_a_picture function.
#           Tests have been written for you (above in main).
#  We suggest breaking this into multiple commits.
#     Can you show the correct circle?
#     Can you make the correct rectangle?
#     Are they in the correct location?
#     Can you draw equally spaced lines?  Are they the correct color?
#     Finally, can you make the lines whose numbers are prime orange?
############################################################################
# HINT:   render(0.5)
#         renders with a half-second pause after rendering.
############################################################################
# -------------------------------------------------------------------------
#
#
#
def draw_a_picture(point, n, color, window):

    circle=rg.Circle(point,100)
    rect=rg.Rectangle(rg.Point(point.x-80,point.y-40),rg.Point(point.x+80,point.y+40))

    circle.attach_to(window)
    rect.attach_to(window)

    for k in range(1,n+1):
        seperate=(k-1)*(160/(n-1))
        Line=rg.Line(point,rg.Point(rect.get_upper_right_corner().x-seperate,rect.get_upper_left_corner().y))
        if is_prime(k)==True:
            Line.color='Orange'
        else:
            Line.color=color
        Line.attach_to(window)

    window.render(0.5)

    pass


main()