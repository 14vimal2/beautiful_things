import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors
from copy import deepcopy

# use dark background
plt.style.use('dark_background')

def tower_of_hanoi(n, source, destination, auxiliary, steps):
    if n == 1:
        steps.append([source, destination]) # append the step
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination, steps)
    steps.append([source, destination]) # append the step
    tower_of_hanoi(n - 1, auxiliary, destination, source, steps)


n = int(input("Enter the number of disks: "))
steps = []
tower_of_hanoi(n, 0, 1, 2, steps)
print("Total number of steps required: ", len(steps))
print("Steps: ", steps)
# plot the steps


## represent each steps as disks movement where each disk is represented by a number
## and each number is a disk size
## for example, [[1,2,3], [], []] is one of the steps where 1, 2, 3 are the disk sizes
## and the first list represents the source, second list represents the auxiliary and
## third list represents the destination
## the following code plots the disks movement for each step

# create a list of lists where each list represents the disks in each step
configuration = [[i+1 for i in range(n)], [], []]
disks = [deepcopy(configuration)]
# change disk color for each size
disk_color = [i[4:] for i in list(mcolors.TABLEAU_COLORS)]


for step in steps:
    source = step[0]
    destination = step[1]
    disk = configuration[source].pop(0)
    configuration[destination].insert(0, disk)
    disks.append(deepcopy(configuration))


# plot distribution of disks in each step
    
fig, ax = plt.subplots(figsize=(3*n+3, n))


def update(i):
    ax.clear()
    ax.axis('off')
    ax.set_xlim(-0.5, 3*n +  5)
    ax.set_ylim(-0.5, n+0.5)

    ## add poles

    ## make the disks as thick as the number of disks
    # size of figure is 3*N x N where N is the number of disks, so that x axis is 3*N accomodates all the disks
    # set the limits of x and y axis
    for k in range(3):
        ## for each pole the coordinate of their center is (k+1)* (n+1)
        ## so for each disks their x coordinate of starting point is (k+1)* (n+1) - size_of_disk/2
        y = 0
        for disk_size in disks[i][k][::-1]:
            # now add rectange at coordinate x = (k+1)* (n+1) - disk_size/2, and y with dimension disk_size * 1
            ax.add_patch(Rectangle([(k+1)*(n+1) - disk_size/2, y ], disk_size, 1, color = disk_color[disk_size-1]))
            y += 1
    return ax


## make animation of each steps and save it as mp4 file with good dpi
from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, update, frames=len(disks), interval=1000, repeat=False)
anim.save('tower_of_hanoi.mp4', dpi=200, writer='ffmpeg')






plt.show()
