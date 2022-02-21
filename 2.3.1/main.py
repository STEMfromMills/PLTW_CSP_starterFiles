#################################################################
#   b231_TR_sample_encoder.py
#   Exampe solution for a custom encoder
#   Note this will not run in the code editor
################################################################
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw

message = "Change Me!" # Change this to encode a different message. 

screen = trtl.getscreen()

SCREEN_HEIGHT = screen.window_height()
SCREEN_WIDTH = screen.window_width()
SQUARE_LENGTH = 21 

print("Screen height: ", SCREEN_HEIGHT)
print("Screen width: ", SCREEN_WIDTH)

RECTANGLE_WIDTH = int(SCREEN_WIDTH/8) # bytes will now fill the width of the screen

NUMBER_OF_BYTES = len(message)+1
RECTANGLE_HEIGHT = (SCREEN_HEIGHT/NUMBER_OF_BYTES) #the message will now fill the height of the screen
print("The desired Rectangle Width is: ", RECTANGLE_WIDTH, " out of :", SCREEN_WIDTH)
print("The desired Rectangle Height is: ", RECTANGLE_HEIGHT, " out of :", SCREEN_HEIGHT)

characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))
print(characters_as_ints)

characters_as_bits = []
characters_as_bits.append('{0:08b}'.format(len(message))) # Adds a leading byte that encodes the number of letters in the message
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)

bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)
print(bits_as_ints)

painter = trtl.Turtle()
painter.hideturtle()
painter.speed(0)

painter.penup()
#starting point is no longer arbitrary but scales with screen size to the upper left corner
painter.goto((-SCREEN_WIDTH/2)+(RECTANGLE_WIDTH/2),(SCREEN_HEIGHT/2)+(RECTANGLE_HEIGHT/2))
painter.shape("square")
#shape is modified so that the message will fill the screen
print("Scale is: ",RECTANGLE_HEIGHT/SQUARE_LENGTH , ", ", RECTANGLE_WIDTH/SQUARE_LENGTH)
print("Yielding: ",(RECTANGLE_HEIGHT/SQUARE_LENGTH)*SQUARE_LENGTH , ", ", (RECTANGLE_WIDTH/SQUARE_LENGTH)*SQUARE_LENGTH)
painter.shapesize(RECTANGLE_HEIGHT/SQUARE_LENGTH,RECTANGLE_WIDTH/SQUARE_LENGTH)

painter.color("blue")

message_length = len(bits_as_ints)
index = 0
while index < message_length:
  if index % 8 == 0:
    painter.goto((-SCREEN_WIDTH/2)+(RECTANGLE_WIDTH/2), painter.ycor()-(RECTANGLE_HEIGHT))
  if bits_as_ints[index]=='1':
    painter.stamp()
  painter.forward(RECTANGLE_WIDTH)
  index = index + 1

screen = trtl.getscreen()
root = trtl.getcanvas().winfo_toplevel()

# draw the message instead of taking a screenshot for macOS users
def draw_message(im_size, x, y):
    im = Image.new("RGBA", im_size, (255,255,255,0))
    draw = ImageDraw.Draw(im)
    message_length = len(bits_as_ints)
    index = 0
    y = 0
    while index < message_length:
      if index % 8 == 0:
        x = 0
        y += RECTANGLE_HEIGHT
      if bits_as_ints[index]=='1':
        draw.rectangle([x,y-RECTANGLE_HEIGHT,x+RECTANGLE_WIDTH-2,y-1], fill="blue") #stamp
      x += RECTANGLE_WIDTH
      index = index + 1
    im.save("macOutput2.gif")

def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    im = ImageGrab.grab().crop((x,y,x1,y1))
    im.save("output2.gif")
    print(im.size)

    #create an image for macOS users
    draw_message(im.size, 0, 0)

create_image(screen)

screen.mainloop()