import turtle
from typing import Any

class CustomTurtle:
    def __init__(self,
                 shape: str = "turtle",
                 color: str = "black",
                 position: "tuple[int, int]" = (0, 0),
                 visiblilty: bool = True,
                 pen: bool = True):
        self.turtle = turtle.Turtle(shape, visible=False)
        
        self.turtle.pu()
        self.turtle.color(color)
        self.turtle.setpos(position)
        if visiblilty is True:
            self.turtle.st()
        if pen is True:
          self.turtle.pd()

    def __str__(self) -> str:
       return f'position: {self.position}, shape: {self.shape}, color: {self.color}'
    
    def move_x(self, movement: int):
        newpos = self.turtle.xcor() + movement

        self.turtle.setx(newpos)
      
    def move_y(self, movement: int):
       newpos = self.turtle.xcor() + movement

       self.turtle.sety(newpos)

    def move_all(self, movement: "tuple[int, int]"):
       newpos = (movement[0] + self.turtle.xcor(),
                 movement[1] + self.turtle.ycor())
       
       self.turtle.setpos(newpos)

    def write_text(self,
                   message: str,
                   align: str = "left",
                   font_type: str = "Arial",
                   font_size: int = 12):
        self.turtle.clear()
        self.turtle.write(message, False, align, (font_type,
                                                  font_size,
                                                  "normal"))
class TurtleMove:
  def move_relative_all(turtle_obj: turtle.Turtle,
                        movement_x: int,
                        movement_y: int):
    """
    Moves a turtle.Turtle object from its current position in both axes

    Args:
        turtle_obj (turtle.Turtle): turtle.Turtle object to be moved
        movement_x (int): Movement in the x axis
        movement_y (int): Movement in the y axis
    """
    newpos_x = turtle_obj.xcor() + movement_x
    newpos_y = turtle_obj.ycor() + movement_y
    turtle_obj.setpos(newpos_x, newpos_y)

  def move_relative_x(turtle_obj: turtle.Turtle, movement: int):
    """
    Moves a turtle.Turtle object from its current position in the x axis

    Args:
        turtle_obj (turtle.Turtle): turtle.Turtle object to be moved
        movement (int): Movement in the x axis
    """
    newpos = turtle_obj.xcor() + movement
    turtle_obj.setx(newpos)

  def move_relative_y(turtle_obj: turtle.Turtle, movement: int):
    """
    Moves a turtle.Turtle object from its current position in the y axis

    Args:
        turtle_obj (turtle.Turtle): turtle.Turtle object to be moved
        movement (int): Movement in the y axis
    """
    newpos = turtle_obj.ycor() + movement
    turtle_obj.sety(newpos)

class TurlteDraw:
  def turtle_write(turtle_obj: turtle.Turtle,
                  message: str,
                  align: str = "left",
                  font_type: str = "Arial",
                  font_size: int = 12):
    """Clears everything drawn or written by the turtle object and writes 
    a message

    Args:
        turtle_obj (turtle.Turtle): turtle.Turtle object which writes the
        message
        message (str): Message to be written
        align (str, optional): How to align the text
        ("left", "center" or "right"). Defaults to "left".
        font_type (str, optional): Font the message is written in.
        Defaults to "Arial"
        font_size (int, optional): Font size of the message. Defaults to 12.
    """
    turtle_obj.clear()
    turtle_obj.write(message, False, align, (font_type, font_size, "normal"))