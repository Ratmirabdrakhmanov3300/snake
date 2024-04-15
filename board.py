import turtle as t

class Board():
    def __init__(self, size):
        self.size = size
        t.penup()
        t.goto(-size/2, -size/2)
        t.pendown()
        for i in range(4):
            t.forward(size)
            t.left(90)
        t.hideturtle()

    def check(self, snake):
        (x,y) = snake.head.pos()
        if x<-self.size/2 or x>self.size/2 or y<-self.size/2 or y>self.size/2:
            return True
        return False
