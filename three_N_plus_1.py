import matplotlib.pyplot as plt
import matplotlib.animation as animation
# make black background
plt.style.use('dark_background')

number = int(input("Enter the number: "))

# split the numbers by spaces or commas where spaces may be irregular

def three_n_plus_1(n):
    """Return the number of steps required to reach 1."""
    # initialize the list of values
    x  = n
    y = []     # values of expression 3n+1
    m: dict[int,bool] = {} # memoization dictionary
    # while the resulting value is not being repeated add the value to the list
    while m.get(x) is None:
        y.append(x)
        m[x] = True
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    return y


fig = plt.figure()
plt.title("3n+1 : %d" % number, size=20)

ax = fig.add_subplot(111)


# for i in numbers:
#     plt.plot(three_n_plus_1(i), label="%d" % i)

y = three_n_plus_1(number)
x = list(range(len(y)))
line = ax.plot([], [])

ax.set_xlim(0,len(y))
ax.set_ylim(0, max(y))
ax.set_xticks([])
ax.set_yticks([])

def update(frame):
    """Update the graph."""
    xdata = x[:frame]
    ydata = y[:frame]
    line[0].set_xdata(xdata)
    line[0].set_ydata(ydata)
    return line



# animate the graph
ani = animation.FuncAnimation(fig, update,frames=len(y), interval=50)

ani.save('3n+1.gif','pillow')

ani.save('3n+1.mp4', writer='ffmpeg', fps=30)

plt.show()
# plt.savefig('3nplus1.png')
