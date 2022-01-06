import turtle as trtl

drawer1 = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()

wn = trtl.Screen()

wn.tracer(False)

drawer1.setheading(45)
drawer1.forward(200)

wn.tracer(True)

drawer2.setheading(315)
drawer2.forward(200)

wn.tracer(False)

drawer3.setheading(135)
drawer3.forward(200)

# Uncomment the line below to see the third turtle's path.
#wn.update()

trtl.mainloop()
