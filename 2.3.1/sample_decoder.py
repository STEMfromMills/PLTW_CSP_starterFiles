#################################################################
#   b231_TR_sample_decoder.py
#   Exampe solution for a custom decoder
#   Note this will not run in the code editor
#   If using a macOS device, change im to open "macOutput2.gif"
################################################################
from PIL import Image

im = Image.open("output2.gif")
rgb_im = im.convert('RGB')
width, height = im.size

BIT_SPACING = int(width/8)
DISTANCE_FROM_TOP = 0
#determine the distance from the top of the screen to the first colored pixel
for i in range(0,height):
  for j in range(0, width):
    r,g,b = rgb_im.getpixel((j,i))
    if r < 20 and DISTANCE_FROM_TOP ==0:
      DISTANCE_FROM_TOP = i
      
print("Bit Spacing: ", BIT_SPACING)
print("Image Width: ", width)
height = height - DISTANCE_FROM_TOP
print("Image Height - border: ", height)
print("Distance from the top: ", DISTANCE_FROM_TOP)

number_of_characters_as_bits = [0,0,0,0,0,0,0,0]
#retrieve byte representation of the number of characters in the message
for i in range(0,8):
  x_pos = int((i*BIT_SPACING) + (BIT_SPACING/2))
  r,g,b =rgb_im.getpixel((x_pos,DISTANCE_FROM_TOP))
  if g < 254:
    number_of_characters_as_bits[i] = 1

print(number_of_characters_as_bits)

#decode number of characters in the message
number_of_characters_as_int = 0
for i in range(0,8):
  if number_of_characters_as_bits[i] == 1:
    if i == 0:
      number_of_characters_as_int = number_of_characters_as_int + 128
    elif i == 1:
      number_of_characters_as_int = number_of_characters_as_int + 64
    elif i == 2:
      number_of_characters_as_int = number_of_characters_as_int + 32
    elif i == 3:
      number_of_characters_as_int = number_of_characters_as_int + 16
    elif i == 4:
      number_of_characters_as_int = number_of_characters_as_int + 8
    elif i == 5:
      number_of_characters_as_int = number_of_characters_as_int + 4
    elif i == 6:
      number_of_characters_as_int = number_of_characters_as_int + 2
    elif i == 7:
      number_of_characters_as_int = number_of_characters_as_int + 1


print("Number of letters is: ", number_of_characters_as_int)

VERTICAL_BIT_SPACING = int(height/number_of_characters_as_int)

BITS_IN_A_BYTE = 8

my_array = []
for letters in range(0,BITS_IN_A_BYTE*number_of_characters_as_int):
  my_array.append(0)

#use the number of characters in the message to extrapolate the size of the rectangles
#that represent bits and thus their spacing
UPPER_PIXEL_ROW = DISTANCE_FROM_TOP  + VERTICAL_BIT_SPACING
LEFT_PIXEL_COL = int(BIT_SPACING/2)
DISTANCE_BETWEEN_BLOCKS = BIT_SPACING
LOW_PIXEL_ROW = UPPER_PIXEL_ROW+(number_of_characters_as_int*VERTICAL_BIT_SPACING)
RIGHT_PIXEL_COL = LEFT_PIXEL_COL+(BITS_IN_A_BYTE*BIT_SPACING)

pos=0
for i in range(UPPER_PIXEL_ROW,LOW_PIXEL_ROW,VERTICAL_BIT_SPACING):
  for j in range(LEFT_PIXEL_COL,RIGHT_PIXEL_COL,DISTANCE_BETWEEN_BLOCKS):
    r,g,b = rgb_im.getpixel((j,i))
    if g < 254: #the white pixels have green values of 254, blue have less
      my_array[pos]=1
    pos = pos + 1
print(my_array)

message_as_bits = ''
for bit in my_array:
  message_as_bits = message_as_bits + str(bit)
print(message_as_bits)

letter = 0
decoded = ''
for n in range(0,len(message_as_bits)):
  if n % 8 == 0:
    if letter != 0:
      decoded = decoded + chr(letter)
      letter = 0
    letter = int(message_as_bits[n]) * 128 + letter
  elif n % 8 == 1:
    letter = int(message_as_bits[n]) * 64 + letter
  elif n % 8 == 2:
    letter = int(message_as_bits[n]) * 32 + letter
  elif n % 8 == 3:
    letter = int(message_as_bits[n]) * 16 + letter
  elif n % 8 == 4:
    letter = int(message_as_bits[n]) * 8 + letter
  elif n % 8 == 5:
    letter = int(message_as_bits[n]) * 4 + letter
  elif n % 8 == 6:
    letter = int(message_as_bits[n]) * 2 + letter
  elif n % 8 == 7:
    letter = int(message_as_bits[n]) * 1 + letter
print(decoded)
