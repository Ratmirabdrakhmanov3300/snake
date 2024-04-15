import snake_obj as snk
import board as brd
import apple
import score

STEP = 20
DELAY = 0.2
SIZE = 400

snake = snk.Snake(3, '#36790d', 'turtle')
board = brd.Board(SIZE)
apple = apple.Apple('#c0090f', SIZE, STEP)
score = score.Score(SIZE)

while True:
    snake.step(STEP)
    if board.check(snake):
        print('lol no')
        snake.__del__()
        snake = snk.Snake(3, '#36790d', 'turtle')
        score.__delS__()

    if apple.check_apple(snake):
        apple.remake()
        snake.plus('#36790d')
        score.plus()

    if snake.check_kus():
        print('lol no')
        snake.__del__()
        snake = snk.Snake(3, '#36790d', 'turtle')
        score.__delS__()

    score.update()
    snake.update(DELAY)
