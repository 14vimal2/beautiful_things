import matplotlib.pyplot as plt
from math import cos, sin
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')




def drawSpirograph(R, r, l, times=25):

    # initialize the list of x and y coordinates
    xpoints, ypoints = [], []

    # iterate through the number of degrees
    for theta in range(0, 360 * times):

        # convert the degrees to radians
        theta = theta * 3.14 / 180

        # get the x coordinate
        x = (R - r) * cos(theta) + l * cos((R - r) * theta / r)

        # get the y coordinate
        y = (R - r) * sin(theta) - l * sin((R - r) * theta / r)

        # append the x and y coordinates to the list
        xpoints.append(x)
        ypoints.append(y)

    # plot the points
    # make figure size a square
    return xpoints, ypoints
    # plt.plot(xpoints, ypoints, '.', markersize=0.8)
    # save the figure


fig = plt.figure(figsize=(4, 4))

ax = fig.add_subplot(111)

ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)


plt.title('Spirograph', size=20)


# draw the spirograph
data = [
    drawSpirograph(100, 30, 20),
    drawSpirograph(130, 10, 8),
    drawSpirograph(110, 50, 35),
    drawSpirograph(105, 70, 65),
    drawSpirograph(150, 35, 25)
]

lines = [ax.plot([], []) for _ in range(len(data))]


def update(frame):
    xdata = [datai[0][:frame*50] for datai in data]
    ydata = [datai[1][:frame*50] for datai in data]
    for i, line in enumerate(lines):
        line[0].set_xdata(xdata[i])
        line[0].set_ydata(ydata[i])
    return lines


ani = FuncAnimation(fig, update, frames=len(data[0][0]), interval=1)

# ani.save('spirograph.gif', writer='pillow')
plt.show()
ani.save('spirograph.gif', writer='pillow')

# ani.save('spirograph.mp4', writer='ffmpeg')

# plt.savefig('spirograph.png', dpi=1000)
plt.close()
