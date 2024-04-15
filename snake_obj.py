import turtle as t
import time


class Snake():

    def __init__(self, TAIL, CLR, SHAPE):
        self.step_size = 20
        self.window = t.Screen()
        self.window.setup(width=600, height=600)

        t.tracer(0)
        t.penup()
        self.head = t.Turtle()
        self.head.shape('turtle')
        self.head.color(CLR)
        self.head.penup()

        self.tail = []
        for i in range(TAIL):
            x = t.Turtle()
            x.shape('turtle')
            x.color(CLR)
            x.penup()
            x.goto(-20 - 20 * i, 0)
            self.tail.append(x)

        t.onkey(lambda: self.head.setheading(180), 'Left')
        t.onkey(lambda: self.head.setheading(0), 'Right')
        t.onkey(lambda: self.head.setheading(90), 'Up')
        t.onkey(lambda: self.head.setheading(270), 'Down')
        t.listen()

    def step(self, STEP):
        (x, y) = self.head.pos()
        h = self.head.heading()
        for el in self.tail:
            (xe, ye) = el.pos()
            he = el.heading()
            el.goto(x, y)
            el.setheading(h)
            (x, y, h) = (xe, ye, he)
        self.head.forward(STEP)

    def update(self, DELAY):
        t.update()
        time.sleep(DELAY)

    def __del__(self):
        self.head.hideturtle()
        for el in self.tail:
            el.hideturtle()

    def plus(self, CLR):
        (xx,yy) = self.tail[-1].pos()
        x = t.Turtle()
        x.shape('turtle')
        x.color(CLR)
        x.penup()
        x.goto(xx,yy)
        self.tail.append(x)

    def check_kus(self):
        for element in self.tail:
            if self.head.distance(element)<self.step_size/2:
                return True
        return False
