import simple_turtle, turtle, random

def check_winner(turtle_list: "list[simple_turtle.CustomTurtle]") -> int:
    max_distance = 0
    winner = -1

    for i in range(len(turtle_list)):
        xcor = turtle_list[i].turtle.xcor()
        if xcor >= 350 and xcor > max_distance:
            max_distance = xcor
            winner = i
      
    return winner

def main():
    colors = ["red", "green", "blue", "magenta", "cyan"]
    turtles: "list[simple_turtle.CustomTurtle]" = []
    text_turtles: "list[simple_turtle.CustomTurtle]" = []

    nr_of_turtles = -1
    while nr_of_turtles < 2 or nr_of_turtles > 5:
        nr_of_turtles = int(input("Antall skilpadder (mellom 2 og 5): "))

    turtle.screensize(800, 750)

    for i in range(nr_of_turtles):
        new_turtle = simple_turtle.CustomTurtle("turtle",
                                                colors[i],
                                                (-300, -250 + i * 100))
        new_text = simple_turtle.CustomTurtle("turtle",
                                colors[i],
                                (-200 + i * 75, 200),
                                False)
        turtles.append(new_turtle)
        text_turtles.append(new_text)

    finish_line = turtle.Turtle(visible=False)
    finish_line.pu()
    finish_line.setpos(350, -300)
    finish_line.pd()
    finish_line.sety(300)
    del finish_line

    while check_winner(turtles) == -1:
        for i in range(len(turtles)):
            turtles[i].move_x(random.randint(20, 50))
            text_turtles[i].write_text(f'{i + 1}: {turtles[i].turtle.xcor() + 300}')

    winner_text = simple_turtle.CustomTurtle("turtle", colors[check_winner(turtles)],
                               visiblilty=False)
    winner_text.write_text(f'Winner is turtle nr. {check_winner(turtles) + 1}!',
                           "center",
                           font_size=20)

    turtle.done()

if __name__ == "__main__":
    main()