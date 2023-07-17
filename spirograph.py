import matplotlib.pyplot as plt
from math import cos, sin

plt.style.use('dark_background')


plt.figure(figsize=(4, 4))
plt.title('Spirograph', size=20)


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
    plt.plot(xpoints, ypoints, '.', markersize=0.8)
    # save the figure


# draw the spirograph
drawSpirograph(100, 30, 20)
drawSpirograph(130, 10, 8)
drawSpirograph(110, 50, 35)
drawSpirograph(105, 70, 65)
drawSpirograph(150, 35, 25)

plt.savefig('spirograph.png', dpi=1000)
plt.close()
