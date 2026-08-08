import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

for i in range(72):
    t.color(colors[i % len(colors)])

    # Draw one petal
    for j in range(2):
        t.circle(100, 60)
        t.left(120)

    t.left(5)

turtle.done()
