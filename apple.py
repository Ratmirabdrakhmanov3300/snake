import turtle as t
import random as rnd

class Apple():

    def __init__(self, color, size, step):
        self.step = step
        self.size = size
        self.color = color
        t.penup()
        self.apple = t.Turtle()
        self.apple.shape('circle')
        self.apple.color(color)
        self.apple.penup()
        x = rnd.randrange(-size/2, size/2, step)
        y = rnd.randrange(-size/2, size/2, step)
        self.apple.goto(x, y)

    def check_apple(self, snake):
        if self.apple.distance(snake.head)<self.step:
            return True
        return False

    def remake(self):
        x = rnd.randrange(-self.size/2+self.step, self.size/2-self.step, self.step)
        y = rnd.randrange(-self.size/2+self.step, self.size/2-self.step, self.step)
        self.apple.goto(x, y)
