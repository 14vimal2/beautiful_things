import matplotlib.pyplot as plt
import math

# make black background
plt.style.use('dark_background')


number = int(input("Enter the number: "))

def fib(n):
    '''Return the list of n fibonacci number.'''
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        # initialize the list of values
        x = [0, 1]
        for i in range(2, n + 1):
            x.append(x[i - 1] + x[i - 2])
        return x
    
def drawQuarter(point, radius, starting_angle):
    '''Draw a quarter of a circle.'''
    # set the starting angle
    angle_ = starting_angle
    # initialize the list of points
    xpoints, ypoints = [], []
    # while the angle is less than 90 degrees
    while angle_ <= starting_angle + 90:
        # append the point to the list
        xpoints.append((point[0] + radius * math.cos(math.radians(angle_)))) 
        ypoints.append((point[1] + radius * math.sin(math.radians(angle_))))
        # increment the angle
        angle_ += 1
    # return the list of points
    # print(xpoints, ypoints) 
    plt.plot(xpoints, ypoints, 'w')
    # plt.show()


numbers = fib(number)


# points radius angle
# [0, 0] 1 180
# [0, 0] 1 270
# [-1, 0] 2 0
# [-1, -1] 3 90
# [ 1, -1] 5 180
# [ 1,  2] 8 270

# numbers are like
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
angle = 180
point = [0, 0]
# iterate through numbers and draw arcs, then change angle, point and radius
axis = 1
positive_direction = True
counter = 1
for i in range(1, len(numbers)):
    radius = numbers[i]
    drawQuarter(point, radius, angle)
    # check for direction and change points accordingly
    if positive_direction:
        point[axis] += numbers[i-1]
    else:
        point[axis] -= numbers[i-1]

    counter += 1
    # change angle
    angle = (angle + 90) % 360
    axis = (axis + 1) % 2
    
    # change axis if counter is 2
    if counter == 2:
        counter = 0
        positive_direction = not positive_direction

plt.title('Fibonacci Spiral', size=20)
plt.savefig('fibspiral.png')
