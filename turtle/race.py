import simple_turtle, turtle, random

def check_winner(turtle_list: list) -> int:
  """Checks if a turtle has won, and finds the turtle with the biggest 
  lead, should multiple have crossed the finish line

  Args:
      turtle_list (list[turtle.Turtle]): List of the turtle.Turtle 
      objects racing

  Returns:
      int: Returns the index of the winner. Returns -1 if there are no winners
  """
  max_distance = 0
  winner = -1

  for i in range(len(turtle_list)):
    xcor = turtle_list[i].xcor()
    if xcor >= 350 and xcor > max_distance:
      max_distance = xcor
      winner = i
      
  return winner

def main():  
  colors = ["red", "green", "blue", "magenta", "cyan"]
  turtles = []
  text_turtles = []

  nr_of_turtles = -1
  while nr_of_turtles < 2 or nr_of_turtles > 5:
    nr_of_turtles = int(input("Antall skilpadder (mellom 2 og 5): "))

  turtle.screensize(800, 750)

  for i in range(nr_of_turtles):
    new_turtle = simple_turtle.turtle_factory("turtle",
                                              colors[i],
                                              -300,
                                              -250 + i * 100)
    new_text = simple_turtle.turtle_factory("turtle",
                                            colors[i],
                                            -200 + i * 75,
                                            200,
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
      simple_turtle.move_relative_x(turtles[i], random.randint(20, 50))
      simple_turtle.turtle_write(text_turtles[i],
                                 f'{i + 1}: {turtles[i].xcor() + 300}')

  winner_text = simple_turtle.turtle_factory("turtle",
                                             colors[check_winner(turtles)],
                                             0,
                                             0,
                                             False)
  simple_turtle.turtle_write(winner_text,
                             f'Winner is turtle nr. {check_winner(turtles) + 1}!',
                             "center",
                             font_size=20)

  turtle.done()

if __name__ == "__main__":
  main()