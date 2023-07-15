# Mandelbrot set
import matplotlib.pyplot as plt

# make black background
plt.style.use('dark_background')

def mendelbrot(z, c):
    """Return the value of the mendelbrot function."""
    return z**2 + c

def drawMendelbrotSet(xmin, xmax, ymin, ymax, iterations):
    """Draw the mendelbrot set."""
    # initialize the list of x and y coordinates
    xpoints, ypoints = [], []
    # iterate through the x coordinates
    for x in range(xmin, xmax):
        # iterate through the y coordinates
        for y in range(ymin, ymax):
            # initialize the complex number
            z = complex(0, 0)
            # initialize the complex number
            c = complex(x / 100, y / 100)
            # iterate through the number of iterations
            for i in range(iterations):
                # get the value of the mendelbrot function
                z = mendelbrot(z, c)
                # if the absolute value of the complex number is greater than 2
                if abs(z) > 2:
                    # append the x and y coordinates to the list
                    xpoints.append(x)
                    ypoints.append(y)
                    break
    # plot the points
    plt.figure(figsize=(4, 4))
    plt.title('Mandelbrot Set', size=20)
    # make figure size a square
    plt.plot(xpoints, ypoints, 'c.', markersize = 0.1)
    # save the figure
    # apply x and y limits
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.savefig('mandelbrot_set.png', dpi=1000)
    plt.close()

# draw the mendelbrot set
drawMendelbrotSet(-200, 100, -100, 100, 10000)

