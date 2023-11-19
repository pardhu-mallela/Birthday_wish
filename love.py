import turtle


def code():
    turtle.setup(1250, 700)  # the window size
    turtle.title("Ramya Birthday")
    # draw the heart

    love = turtle.Turtle()
    love.color("black", "red")

    love.pensize(2)
    love.speed(10)

    love.up()  # about the brush
    love.goto(-200, 50)
    love.down()

    def draw_heart(r, angle=45):
        """

        :param r: the radius of a heart circle

        :param angle: initial brush angle

        :return: returns the coordinates of the heart tip of the peach

        """

        love.begin_fill()  # start filling

        love.seth(0)
        love.seth(angle)  # set brush orientation
        love.circle(-r, 180)  # draw a semicircle counterclockwise
        love.fd(2 * r)  # to move forward
        love.begin_poly()  # record the position of the brush
        x, y = love.get_poly()[0]  # gets the position of the brush
        love.right(90)  # counterclockwise rotating brush
        love.fd(2 * r)  # to move forward
        love.circle(-r, 180)
        love.end_fill()  # fill the end
        return x, y

    # draw the peach heart

    x_y = []

    start_x = -200

    for _ in range(4):
        love.goto(start_x, 50)
        love.down()  # put down the pen

        x_y.append(draw_heart(8))
        start_x += 50
        love.up()  # about the brush

    # painting leaves

    def draw_flower(x, y):
        """

        draw the flower under the heart

        :param x: peach-centered x shaft

        :param y: peach-centered y shaft

        :return:

        """

        love.up()
        love.goto(x, y)
        love.seth(0)  # restore brush to right
        love.seth(-90)
        love.down()

        love.fd(60)
        love.goto(x, y)
        love.right(60)
        love.fd(20)
        love.left(90)
        love.fd(10)
        love.left(120)
        love.fd(20)

        love.up()
        love.goto(x, y)

        love.seth(0)  # restore brush to right
        love.seth(-115)
        love.down()

        love.fd(25)

        love.up()
        love.goto(x, y)

        love.seth(0)  # restore brush to right
        love.seth(-10)
        love.down()

        love.fd(20)
        love.right(90)
        love.fd(8)
        love.right(120)
        love.fd(20)
        love.goto(x, y)
        love.seth(-60)
        love.fd(20)
        love.up()

    for x, y in x_y:
        draw_flower(x, y)

    # draw a worm

    love.up()
    love.goto(-400, -50)
    love.down()

    love.seth(0)  # restore brush to right , good direction control
    love.seth(45)
    love.fd(40)
    love.begin_poly()  # record the position of the brush , the position of the foot fork
    x, y = love.get_poly()[0]  # gets the position of the brush
    love.right(90)
    love.fd(35)
    love.goto(x, y)
    love.left(135)
    love.fd(90)
    love.seth(0)
    love.circle(30)  # a circle
    love.goto(x, y + 60)  # the position of the hand
    love.fd(40)
    love.circle(30, 70)  # a circle , take the radian of the flower hand
    love.seth(0)

    love.up()
    love.goto(x, y + 50)  # the position of the hand
    love.down()

    love.fd(50)
    love.begin_poly()  # note the position of the hand to be used later to draw the flower
    f_x, f_y = love.get_poly()[0]

    # eyes

    love.up()
    love.goto(x - 15, y + 120)  # eye position
    love.down()

    love.pensize(4)
    love.seth(45)
    love.circle(-10, 70)  # draw arc , take the radian of the flower hand
    love.dot(10)  # eye circle
    love.up()
    love.goto(x + 10, y + 120)  # eye position
    love.down()
    love.pensize(4)
    love.seth(45)
    love.circle(-10, 70)  # draw arc , take the radian of the flower hand
    love.dot(10)  # eyes    a circle

    love.up()
    # the mouth

    love.goto(x, y + 105)  # eye position
    love.down()

    love.circle(10, 70)  # draw arc , take the radian of the flower hand

    # the flowers and leaves in the picture

    love.pensize(3)  # brush size
    love.up()
    love.goto(f_x, f_y)  # the position of the hand
    love.left(20)
    love.down()
    love.fd(60)
    love.pensize(2)  # turn down the paint
    love.begin_poly()  # note the position of the hand to be used later to draw the flower
    x, y = love.get_poly()[0]
    love.backward(80)

    love.up()
    love.goto(x, y)
    love.down()

    love.right(90)
    love.fd(20)
    love.right(90)
    love.fd(8)
    love.right(120)
    love.fd(25)
    love.right(200)
    love.fd(25)

    love.up()
    love.goto(x, y)
    love.down()

    love.right(60)
    love.fd(25)
    love.goto(x, y)

    love.right(40)
    love.fd(25)
    love.left(90)
    love.fd(8)
    love.left(110)
    love.fd(25)
    love.goto(f_x + 34, f_y + 75)

    draw_heart(8, angle=20)  # heart in hand

    # write a word

    love.up()
    love.goto(150, 200)

    love.pencolor("PINK")  # the brush color

    love.goto(180, 140)
    love.goto(-405, -150)
    love.pendown()
    love.pencolor("black")

    love.hideturtle()

    love.write("HaPpY BirThDaY", font=("Verdana", 30, ''))

    turtle.hideturtle()

    r = turtle.Turtle()
    screen = turtle.Screen()
    screen.addshape('ramya_gif.gif')

    r.penup()
    r.goto(320, 10)
    r.pendown()

    r.shape('ramya_gif.gif')
    screen.mainloop()
