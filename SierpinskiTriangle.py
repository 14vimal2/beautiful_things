# Draw Sierpinski Triangle using the chaos game.

import random
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# initialize the points
points = [[0, 0], [1, 0], [0.5, 1]]

# initialize the list of x and y coordinates
xpoints, ypoints = [], []

# initialize the current point
current_point = [0, 0]

# initialize the number of iterations
iterations = int(input('Enter the number of iterations: '))
# iterations = 100000

# iterate through the number of iterations
for i in range(iterations):
    # get a random point from the points
    random_point = random.choice(points)
    # get the midpoint between the current point and the random point
    current_point = [(current_point[0] + random_point[0]) / 2, (current_point[1] + random_point[1]) / 2]
    # append the x and y coordinates to the list
    xpoints.append(current_point[0])
    ypoints.append(current_point[1])

# plot the points
plt.figure(figsize=(6, 6))
plt.title('Sierpinski Triangle', size=20)
# make figure size a square
plt.plot(xpoints, ypoints, 'c.', markersize = 0.1)
# save the figure
plt.savefig('sierpinski_triangle.png')
plt.close()
