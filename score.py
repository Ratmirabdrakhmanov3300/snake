import turtle as t

class Score():
    def __init__(self, size):
        self.size = size
        self.text = t.Turtle()
        self.text.penup()
        self.text.goto(-size/2, size/2)
        self.score = 0

    def update(self):
        self.text.clear()
        s = 'Счет = ' + str(self.score)
        self.text.write(s, font=('Times', 20, 'bold'))

    def plus(self):
        self.score+=1

    def __delS__(self):
        self.score = 0