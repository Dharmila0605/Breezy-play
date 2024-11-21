import turtle
import time
import random
import tkinter as tk
from tkinter import messagebox

# Function to return to the main menu
def return_to_menu():
  wn.bye() # Close the turtle window
  main_menu()

# Functions to run the games
def start_snake_game():
  global wn
  wn = turtle.Screen()
  wn.title("Snake Game")
  wn.bgcolor("black")
  wn.setup(width=600, height=600)
  wn.tracer(0)

  delay = 0.25
  score = 0
  high_score = 0

  # Snake head
  head = turtle.Turtle()
  head.shape("circle")
  head.color("red")
  head.penup()
  head.goto(0, 0)
  head.direction = "stop"

  # Snake food
  food = turtle.Turtle()
  food.speed(0)
  food.shape("circle")
  food.color("yellow")
  food.penup()
  food.goto(0, 100)

  # Snake body
  segments = []

  # Pen for displaying the score
  pen = turtle.Turtle()
  pen.speed(0)
  pen.color("white")
  pen.penup()
  pen.hideturtle()
  pen.goto(0, 260)
  pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

  # Function to move the snake
  def move():
    if head.direction == "up":
      y = head.ycor()
      head.sety(y + 20)
    if head.direction == "down":
      y = head.ycor()
      head.sety(y - 20)
    if head.direction == "left":
      x = head.xcor()
      head.setx(x - 20)
    if head.direction == "right":
      x = head.xcor()

      head.setx(x + 20)

  # Functions to change the direction
  def go_up():
    if head.direction != "down":
      head.direction = "up"

  def go_down():
    if head.direction != "up":
      head.direction = "down"

  def go_left():
    if head.direction != "right":
      head.direction = "left"

  def go_right():
    if head.direction != "left":
      head.direction = "right"

  # Key bindings
  wn.listen()
  wn.onkey(go_up, "g")
  wn.onkey(go_down, "h")
  wn.onkey(go_left, "f")
  wn.onkey(go_right, "j")

  def game_over():
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    # Back button to go to the menu
    def go_back():
      return_to_menu()

    wn.onkey(go_back, "b")
    wn.listen()

  # Main game loop
  while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = "stop"

      # Hide the segments
      for segment in segments:
        segment.goto(1000, 1000)
      segments.clear()

      # Reset the score
      score = 0
      delay = 0.15
      pen.clear()
      pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

      game_over()
      break

    # Check for collision with the food
    if head.distance(food) < 20:
      # Move the food to a random spot
      x = random.randint(-290, 290)

      y = random.randint(-290, 290)
      food.goto(x, y)

      # Add a segment to the snake
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("circle")
      new_segment.color("green")
      new_segment.penup()
      segments.append(new_segment)

      # Increase the score
      score += 10
      if score > high_score:
        high_score = score

      pen.clear()
      pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

      delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
      x = segments[index - 1].xcor()
      y = segments[index - 1].ycor()
      segments[index].goto(x, y)

    if len(segments) > 0:
      x = head.xcor()
      y = head.ycor()
      segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
      if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
          segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.15
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        game_over()
        break

    time.sleep(delay)


def start_flippy_bird():
  global wn
  wn = turtle.Screen()
  wn.title("Flippy Bird")
  wn.bgcolor("skyblue")
  wn.setup(width=600, height=600)
  wn.tracer(0)

  gravity = -1
  bird_speed = 0
  pillar_speed = -2
  score = 0
  high_score = 0
  passed_pillars = []


  bird = turtle.Turtle()
  bird.shape("square")
  bird.color("yellow")
  bird.shapesize(stretch_wid=1, stretch_len=1)
  bird.penup()
  bird.goto(-200, 0)
  bird.direction = "stop"

  pillars = []

  def create_pillar(x):
    top_pillar = turtle.Turtle()
    top_pillar.shape("square")
    top_pillar.color("green")
    top_pillar.shapesize(stretch_wid=18, stretch_len=3)
    top_pillar.penup()
    top_pillar.goto(x, random.randint(200, 350))

    bottom_pillar = turtle.Turtle()
    bottom_pillar.shape("square")
    bottom_pillar.color("green")
    bottom_pillar.shapesize(stretch_wid=18, stretch_len=3)
    bottom_pillar.penup()
    bottom_pillar.goto(x, top_pillar.ycor() - 460)

    return (top_pillar, bottom_pillar)

  for i in range(5):
    pillar = create_pillar(300 + (i * 200))
    pillars.append(pillar)

  pen = turtle.Turtle()
  pen.speed(0)
  pen.color("white")
  pen.penup()
  pen.hideturtle()
  pen.goto(-250, 260)
  pen.write("Score: 0", align="left", font=("Courier", 24, "normal"))

  def go_up():
    nonlocal bird_speed
    bird_speed = 10

  def go_down():
    nonlocal bird_speed
    bird_speed = -10

  wn.listen()
  wn.onkey(go_up, "u")
  wn.onkey(go_down, "d")

  def move_bird():
    nonlocal bird_speed

    y = bird.ycor()
    y += bird_speed
    bird_speed += gravity
    bird.sety(y)

  def move_pillars():
    nonlocal score, high_score

    for pair in pillars:
      top_pillar = pair[0]
      bottom_pillar = pair[1]

      x = top_pillar.xcor()
      x += pillar_speed
      top_pillar.setx(x)
      bottom_pillar.setx(x)

      if bird.xcor() > top_pillar.xcor() + 30 and (top_pillar, bottom_pillar) not in passed_pillars:
        score += 1
        passed_pillars.append((top_pillar, bottom_pillar))
        if score > high_score:
          high_score = score
        pen.clear()
        pen.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

      if x < -350:
        new_x = 300
        new_y = random.randint(150, 250)
        top_pillar.goto(new_x, new_y)
        bottom_pillar.goto(new_x, new_y - 400)
        passed_pillars.remove((top_pillar, bottom_pillar))

  def check_collisions():
    if bird.ycor() > 290 or bird.ycor() < -290:
      return True
    
    for pair in pillars:
      top_pillar = pair[0]
      bottom_pillar = pair[1]
      if (bird.xcor() + 10 > top_pillar.xcor() - 30 and
        bird.xcor() - 10 < top_pillar.xcor() + 30):
        if (bird.ycor() + 10 > top_pillar.ycor() - 180 or
          bird.ycor() - 10 < bottom_pillar.ycor() + 180):
          return True
    return False

  # Main game loop
  while True:
    wn.update()

    move_bird()
    move_pillars()

    if check_collisions():
      bird.goto(-200, 0) # Reset bird position
      bird_speed = 0
      pen.goto(0, 0)
      pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

      # Back button to go to the menu
      def go_back():
        return_to_menu()

      wn.onkey(go_back, "b")
      wn.listen()
      break

    time.sleep(0.10)


def main_menu():
  menu = tk.Tk()
  menu.title("BreezyPlay Menu")

  def start_snake():
    menu.destroy() # Close the menu
    start_snake_game()

  def start_flippy():
    menu.destroy() # Close the menu
    start_flippy_bird()

  tk.Label(menu, text="Welcome to BreezyPlay", font=("Arial", 24)).pack(pady=20)

  tk.Button(menu, text="Start Snake Game", command=start_snake, font=("Arial", 18)).pack(pady=10)
  tk.Button(menu, text="Start Flippy Bird", command=start_flippy, font=("Arial", 18)).pack(pady=10)

  menu.mainloop()


# Run the main menu
main_menu()