#   a123_apple_1.py
import turtle as trtl
import random as rand
from typing import TypedDict

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

applelist = []
appleletters = []
letters = ["a","s","d","f"]

for i in range(5):
  tempapple = trtl.Turtle()
  applelist.append(tempapple)
  appleletters.append(rand.choice(letters))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  global appleletter
  wn.tracer(False)
  applelist[index].penup()
  applelist[index].shape(apple_image)
  applelist[index].setx(rand.randint(-150,150))
  applelist[index].sety(rand.randint(-25,100))

  applelist[index].sety(applelist[index].ycor() - 30)
  applelist[index].color("white")
  applelist[index].write(appleletters[index], align="center", font=("Arial",40,"normal"))
  applelist[index].sety(applelist[index].ycor() + 30)
  applelist[index].showturtle()
  wn.tracer(True)
  wn.update()

def apple_falls(index):
  applelist[index].penup()
  applelist[index].clear()
  applelist[index].sety(-200)
  applelist[index].hideturtle()
  appleletters[index] = rand.choice(letters)
  draw_apple(index)

def typedA():
  for i in range(5):
    if appleletters[i] == "a":
      apple_falls(i)
  
def typedS():
  for i in range(5):
    if appleletters[i] == "s":
      apple_falls(i)

def typedD():
  for i in range(5):
    if appleletters[i] == "d":
      apple_falls(i)

def typedF():
  for i in range(5):
    if appleletters[i] == "f":
      apple_falls(i)

#-----function calls-----
for i in range(5):
  draw_apple(i)

wn.onkeypress(typedA, "a")
wn.onkeypress(typedS, "s")
wn.onkeypress(typedS, "d")
wn.onkeypress(typedS, "f")

wn.listen()
wn.mainloop()