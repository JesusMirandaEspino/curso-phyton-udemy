import turtle

window = turtle.Screen()
window.title("Pruebas con turtle")
window.bgcolor("#68a0ed")
window.setup(500, 500)

kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(10)

kame.circle(25)
kame.circle(50)
kame.circle(75)
kame.circle(100)
kame.circle(125)

turtle.mainloop()


