import turtle

def fibonacci_spiral():
    # Set up turtle graphics
    turtle.speed(0)  # Adjust the speed of drawing (0 is the fastest)
    turtle.pensize(2)  # Adjust the thickness of the lines
    
    # Generate the Fibonacci sequence
    fib_sequence = [0, 1]
    while fib_sequence[-1] < 500:  # Adjust the limit to control the size of the spiral
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Draw the Fibonacci spiral
    x, y = 0, 0  # Starting point of the spiral
    angle = 90  # Initial angle of the turtle
    
    for length in fib_sequence:
        turtle.setheading(angle)  # Set the turtle's heading
        turtle.forward(length)  # Move the turtle forward
        turtle.right(90)  # Turn the turtle right by 90 degrees
        angle -= 90  # Update the angle for the next arc
    
    turtle.done()

# Call the function to generate the Fibonacci spiral
fibonacci_spiral()
