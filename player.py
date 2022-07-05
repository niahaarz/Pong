from turtle import Turtle

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.score = 0

 
    def up(self):
        newy = self.ycor() +20
        self.goto(self.xcor(), newy)
        

    def down(self):
        newy = self.ycor() -20
        self.goto(self.xcor(), newy)
