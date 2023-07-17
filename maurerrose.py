import sys
import numpy as np
import matplotlib.pyplot as plt

"""Plot a "Maurer Rose" with (integer) parameters n, d."""
plt.style.use('dark_background')

def get_rose_xy(n, d):
    """Get the Cartesian coordinates for points on the rose."""

    # The rose is (r = sin(nk), k) in polar coordinates, for
    # k = d, 2d, 3d, ..., 360d.
    # Add a final point at 361d to close the curve when plotted.
    k = d * np.linspace(0, 361, 361)
    r = np.sin(np.radians(n * k))
    x = r * np.cos(np.radians(k))
    y = r * np.sin(np.radians(k))
    return x, y

def draw_rose(ax, n, d, c='r'):
    """Draw the Maurer rose defined by (n, d) in colour c."""

    x, y = get_rose_xy(n, d)
    ax.plot(x, y, c=c, lw=0.5)
    ax.axis('equal')
    ax.axis('off')

if __name__ == '__main__':
    n, d = int(sys.argv[1]), int(sys.argv[2])
    fig, ax = plt.subplots()
    draw_rose(ax, n, d, 'tab:red')
    plt.savefig('maurer_rose.png', dpi=500)
    plt.show()
