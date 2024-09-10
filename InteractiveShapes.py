import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.shape("turtle")
drawer.color("black")
drawer.speed(0)  # Fastest drawing speed

# Function to draw a square
def draw_square(size):
    
    drawer.forward(size)
    drawer.right(90)
    drawer.forward(size)
    drawer.right(90)
    drawer.forward(size)
    drawer.right(90)
    drawer.forward(size)
    drawer.right(90)

# Function to draw a circle
def draw_circle(radius):
    drawer.circle(radius)

# Function to draw a hexagon
def draw_hexagon(size):

    drawer.forward(size)
    drawer.right(60)
    drawer.forward(size)
    drawer.right(60)
    drawer.forward(size)
    drawer.right(60)
    drawer.forward(size)
    drawer.right(60)
    drawer.forward(size)
    drawer.right(60)
    drawer.forward(size)
    drawer.right(60)
        

# Function to clear the screen
def clear_screen():
    drawer.clear()

# Function to draw a pattern
def draw_pattern():
    for _ in range(36):  # 36 shapes in a circle
        draw_square(50)
        drawer.right(10)  # Adjust angle to create a pattern

# Setup keyboard bindings
screen.listen()
screen.onkey(lambda:draw_square(50), "s")  # Press 's' to draw a square
screen.onkey(lambda: draw_circle(50), "c")  # Press 'c' to draw a circle
screen.onkey(lambda: draw_hexagon(50), "h")  # Press 'h' to draw a hexagon
screen.onkey(clear_screen, "x")  # Press 'x' to clear the screen


# Main loop
turtle.done()
