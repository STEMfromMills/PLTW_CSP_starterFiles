#   encode.py
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw

message = "changeme" # Change this to encode a different message. Length limit 20 characters.

characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))
print(characters_as_ints)

characters_as_bits = []
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)

bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)
print(bits_as_ints)

screen = trtl.getscreen()
painter = trtl.Turtle()

painter.penup()
painter.goto(-200,221)
painter.shape("square")
painter.color("blue")

message_length = len(bits_as_ints)
index = 0
while index < message_length:
  if index % 8 == 0:
    painter.goto(-200, painter.ycor()-21)
  if bits_as_ints[index]=='1':
    painter.stamp()
  painter.forward(21)
  index = index + 1

screen = painter.getscreen()
root = trtl.getcanvas().winfo_toplevel()

# draw the message instead of taking a screenshot for macOS users
def draw_message(im_size, x, y):
    im = Image.new("RGBA", im_size, (255,255,255,0))
    draw = ImageDraw.Draw(im)
    message_length = len(bits_as_ints)
    index = 0
    while index < message_length:
      if index % 8 == 0:
        x = im_size[0]/2-200-10.5
        y += 21
      if bits_as_ints[index]=='1':
        draw.rectangle([x,y,x+21,y+21], fill="blue") #stamp
      x += 21
      index = index + 1
    im.save("macOutput.gif")

def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    im = ImageGrab.grab().crop((x,y,x1,y1))
    im.save("output.gif")
    print(im.size)

    # create an image for macOS users
    draw_message(im.size,im.size[0]/2-200-10.5,im.size[1]/2-221-10.5) # (149.5,98) in ImageDraw is equivalent to (205,275) in PIL 


create_image(screen)

#screen.mainloop()
