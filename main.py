from turtle import Turtle, Screen, colormode
import random

# import colorgram


# image_colors = colorgram.extract('image.jpg', 30)

# new_colors = []
# num = 0

# while num <= 29:
#   for i in image_colors:
#     color = image_colors[num]
#     rgb = color.rgb
#     new_rgb = ()
#     for j in rgb:      
#       new_rgb = new_rgb + (j,)    
#     new_colors.append(new_rgb)
#     num += 1

# print(new_colors)
color_list = [(229, 228, 226), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tom = Turtle()
xcor = -100
ycor = -110


def paint():
  global dots
  global ycor
  for i in range(dots):
    tom.pencolor(random.choice(color_list))
    tom.pendown()
    tom.dot(12)
    tom.penup()
    tom.forward(30)
    tom.pendown()
    dots -= 1
  tom.penup()
  ycor += 20
  dots = 10
  tom.goto(xcor, ycor)
    
colormode(255)
dots = 10
tom.penup()
tom.goto(xcor, ycor)


while ycor <= 70:
  paint()  
  

screen = Screen()
screen.exitonclick()