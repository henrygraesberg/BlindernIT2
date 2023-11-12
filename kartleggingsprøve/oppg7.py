import turtle, random, math

class Runner:
    def __init__(self, color, placement, heading = 0):
        self.turtle = turtle.Turtle("turtle")
        self.turtle.color(color)
        self.turtle.pu()
        self.turtle.setpos(placement, 0)
        self.turtle.setheading(heading)
        self.heading = heading
    
    def move(self, movement):
        if self.heading == 0:
            self.turtle.setx(self.turtle.xcor() + movement)
        else:
            self.turtle.setx(self.turtle.xcor() - movement)
    
class Block:
    def __init__(self, color, placement = 0):
        self.turtle = turtle.Turtle("square")
        self.turtle.shapesize(2, 1)
        self.turtle.color(color)
        self.turtle.pu()
        self.turtle.setpos(placement, 200)
        self.velo = random.randint(-20, -10)
    
    def move(self):
        turtle_obj = self.turtle

        turtle_obj.sety(turtle_obj.ycor() + self.velo)
        if turtle_obj.ycor() >= 200 or turtle_obj.ycor() <= -200:
            self.velo = -self.velo

def check_collision(racers: "list[Runner]", blocks: "list[Block]"):
    for i in range(len(racers)):
        between_y = False
        between_x = False
        for block in blocks:
            if(racers[i].turtle.ycor() < block.turtle.ycor() + 15 and
            racers[i].turtle.ycor() > block.turtle.ycor() - 15):
                between_y = True
            if(racers[i].turtle.xcor() < block.turtle.xcor() + 10 and
            racers[i].turtle.xcor() > block.turtle.xcor() - 10):
                between_x = True

            if between_x is True and between_y is True:
                if i == 0:
                    return 1
                return 0
    return -1

def check_winner(racers: "list[Runner]"):
    if racers[0].turtle.xcor() >= 300:
        return 0
    if racers[1].turtle.xcor() <= -300:
        return 1
    else:
        return -1

def main():
    screen = turtle.Screen()
    runners = [Runner("green", -300), Runner("blue", 300, -180)]
    blocks = [Block("red", -150), Block("black"), Block("orange", 150)]

    winner = -1

    while winner == -1:
        for runner in runners:
           runner.move(random.randint(5, 15))
        for block in blocks:
           block.move()
        
        winner = check_winner(runners)
        winner = check_collision(runners, blocks)

    turtle.done()

if __name__ == "__main__":
    main()