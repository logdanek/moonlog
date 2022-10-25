import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
circles = turtle.Turtle()
circles.speed(20)
circles.color(colors[0])

SIZE = 243

circles.penup()
circles.goto(0, -SIZE)
circles.pendown()


def circle(SIZE):
    """
        Функция, рисующая фрактал на основе контактного числа
        окружностей
    """
    if SIZE <= 4:
        return
    for j in range(6):
        circles.color(colors[j])
        circles.circle(SIZE // 3)
        circles.circle(SIZE, 60)
        circle(SIZE // 3)


circles.circle(SIZE)
circle(SIZE)
circle(SIZE // 3)
turtle.done()
