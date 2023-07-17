# penrose_tiles.py
import matplotlib.pyplot as plt

# plt.style.use('dark_background')


import numpy as np

def draw_penrose_tiling(ax, depth, points):
    if depth == 0:
        return

    new_points = []
    for x, y, label in points:
        if label == 'A':
            # Draw an orange triangle
            ax.fill(x, y, 'orange', edgecolor='black')

            # Apply the substitution rules for A
            p1 = x + (2/3) * (y - x)
            p2 = x + (1/3) * (y - x)
            p3 = y - (1/3) * (y - x)

            new_points.append((x, p1, 'A'))
            new_points.append((p2, p3, 'B'))
        elif label == 'B':
            # Draw a blue triangle
            ax.fill(x, y, 'blue', edgecolor='black')

            # Apply the substitution rules for B
            p1 = y + (2/3) * (x - y)
            p2 = y + (1/3) * (x - y)
            p3 = x - (1/3) * (x - y)

            new_points.append((p1, y, 'A'))
            new_points.append((p3, p2, 'B'))

    draw_penrose_tiling(ax, depth - 1, new_points)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Set the initial points for the Penrose tiling
points = [(0, 0, 'A'), (1, 0, 'B')]

# Set the depth for the Penrose tiling
depth = 4

# Draw the Penrose tiling
draw_penrose_tiling(ax, depth, points)

# Display the plot
plt.show()

