
// input box where user gives commands
const INPUT_BOX = document.getElementById('input-box');
const SCREEN = document.getElementById('screen');
const AFTER_CURSOR = document.getElementById('after-cursor');
const CURSOR = document.getElementById('cursor');
// list of available terminal commands

const PATTERNS = [
    {
        name: "3n+1",
        desc: "description of pattern1",
        code: 
            `
            import matplotlib.pyplot as plt
            # make black background
            plt.style.use('dark_background')

            numbers = input("Enter the numbers (seperated by space): ")

            # split the numbers by spaces or commas where spaces may be irregular
            numbers = numbers.split(" ")

            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])

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

            for i in numbers:
                plt.plot(three_n_plus_1(i), label="%d" % i)
            plt.title("3n+1", size=20)
            plt.legend()
            plt.savefig('3nplus1.png')
            `,
        image: "3nplus1.png"
    },
    {
        name: "collatz",
        desc: "description of pattern2",
        code: 
            `
            import networkx as nx
            import matplotlib.pyplot as plt
            import matplotlib.cm as cm
            
            # make it dark theme
            plt.style.use('dark_background')
            
            def collatz_sequence(n):
                sequence = [n]
                while n != 1:
                    if n % 2 == 0:
                        n = n // 2
                    else:
                        n = 3 * n + 1
                    sequence.append(n)
                return sequence
            
            def create_collatz_tree(starting_numbers):
                G = nx.Graph()
                for start in starting_numbers:
                    sequence = collatz_sequence(start)
                    for i in range(len(sequence) - 1):
                        G.add_edge(sequence[i], sequence[i+1])
                return G
            
            def visualize_collatz_tree(G: nx.Graph):
                pos = nx.spring_layout(G)
                # make figure size square
                plt.figure(figsize=(6,6))
                plt.title('Collatz tree', size=20)
                nx.draw_networkx(G, 
                                pos,
                                with_labels=False,
                                node_size=10,
                                node_color='r',
                                edge_color=range(2, G.number_of_edges() + 2),
                                edge_cmap=cm.get_cmap('viridis')
                                )
                # save figure
                plt.savefig('collatz.png', dpi=1000)
                plt.show()
            
            # Example usage
            starting_numbers = [6, 9, 27, 10, 24, 3, 7, 15, 96, 9663]
            collatz_tree = create_collatz_tree(starting_numbers)
            visualize_collatz_tree(collatz_tree)
            `,
        image: "collatz.png"
    },
    {
        name: "sierpinski",
        desc: "description of pattern3",
        code: 
            `
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
            plt.savefig('sierpinski_triangle.png', dpi=1000)
            plt.close()
            `,
        image: "sierpinski_triangle.png"
    },
    {
        name: "fibonacci",
        desc: "description of pattern4",
        code: 
            `
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
                plt.plot(xpoints, ypoints, 'c')
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
            `,
        image: "fibspiral.png"
    },
    {
        name: "ulam",
        desc: "description of pattern5",
        code: 
            `
            # generate prime number list
            import matplotlib.pyplot as plt
            
            plt.style.use('dark_background')         
            
            
            
            N = int(input('Enter the max limit N: '))
            
            sieve = [True] * (N + 1)
            primes = []
            
            for i in range(2, N+1):
                if sieve[i]:
                    primes.append(i)
                    for j in range(i, N+1,i):
                        sieve[j] = False
            # print(primes)
            
            
            # plotting of ulam spiral
            x, y = 0, 0
            axis = 0
            xch, ych = 1, 1
            xgoal, ygoal = 1, 1
            current = 1
            xcoordinates, ycoordinates = [], []
            while current <= N:
                if current in primes:
                    xcoordinates.append(x)
                    ycoordinates.append(y)
                    # plt.plot(x, y, 'r.')
                current += 1
                if axis == 0:
                    # check if coordinate will move in +ve or -ve direction
                    if xch & 1 == 1: # if xch is odd then +ve
                        x += 1
                    else:
                        x -= 1
                    
                    if xgoal == x:
                        axis = 1
                        xch += 1
                        if xch & 1 == 1:
                            xgoal = x + xch
                        else:
                            xgoal = x - xch
            
                elif axis == 1:
                    if ych & 1 == 1:
                        y += 1
                    else:
                        y -= 1
                    
                    if ygoal == y:
                        axis = 0
                        ych += 1
                        if ych & 1 == 1:
                            ygoal = y + ych
                        else:
                            ygoal = y - ych
                    
            # make plot size a square
            plt.figure(figsize=(6, 6))
            plt.title('Ulam Spiral', size=20)
            # plt.xlim(-min(xcoordinates), max(xcoordinates))
            # plt.ylim(-min(ycoordinates), max(ycoordinates))
            plt.plot(xcoordinates, ycoordinates, 'r-')
            plt.plot(xcoordinates, ycoordinates, 'ws')
            plt.savefig('prime_spiral.png')
            plt.show()  
            `,
        image: "prime_spiral.png"
    },
    {
        name: "mandelbrot",
        desc: "description of pattern6",
        code: 
            `
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
            
            `,
        image: "mandelbrot_set.png"
    }
]

const COMMANDS = [
    {
        name: "help",
        desc: "displays all available commands",
        execute: function() {
            COMMANDS.forEach(command => {
                SCREEN.innerHTML += `<div><span class="command">${command.name}</span> &emsp; <span>${command.desc}</span> </div>`
            })
        }
    },
    {
        name: "ls",
        desc: "lists all available patterns",
        execute: function() {
            PATTERNS.forEach(pattern => {
                SCREEN.innerHTML += `<div>${pattern.name}</div>`
            })
        }
        
    },
    {
        name: "cat",
        desc: 
        `Usage: cat [OPTION]...  [PATTERN]...
        displays pattern

        when no options, it just displays the image.

        -d, --describe              shows description of the pattern
        -c, --code                  shows code to generate the pattern 
        `,
        execute: function(value) {
            let arguments = value.toString();
            // get last element from value
            var pattern_name = value[value.length-1];
            var pattern = PATTERNS.find(p => p.name === pattern_name)
            if (pattern) {
                SCREEN.innerHTML += '<h3>Figure :</h3>'
                addImage(pattern.image);
                if (arguments.includes('-d') || arguments.includes('--describe')) {
                    SCREEN.innerHTML += `<h3>Description :</h3><pre><p>${pattern.desc}<p></pre>`
                }


                if (arguments.includes('-c') || arguments.includes('--code')) {
                    SCREEN.innerHTML += `<h3>Code :</h3><pre><p>${pattern.code}<p></pre>`
                }

                

            } else {
                SCREEN.innerHTML += 'No such pattern exists.'
            }
        }
    },
    {
        name: "clear",
        desc: "clears the screen"
    }
]

function addImage(imagename) {
    SCREEN.innerHTML += `<img src="${imagename}" alt="pattern" width="600" height="600">`
}


INPUT_BOX.addEventListener('input',resetInputBoxSize);
INPUT_BOX.addEventListener('keydown',handleKeyPress);
INPUT_BOX.addEventListener('focusout', focusOut)
INPUT_BOX.addEventListener('focusin', focusIn)
INPUT_BOX.focus()


function focusOut() {
    // remove blinking effect in cursor
    CURSOR.style.animationPlayState = 'paused';
}

function focusIn() {
    CURSOR.style.animationPlayState = 'running';
}

function resetInputBoxSize() {
    const inputWidth = INPUT_BOX.value;
    var width = inputWidth.length * 8;
    INPUT_BOX.style.width = width + "px";
    
}

function handleKeyPress(event) {
    var key = event.keyCode || event.which;
    if (key == 13) {
        event.preventDefault();
        console.log('Enter key pressed');
        submitInput();
    } 
    else if (key == 37) { // left arrow key then move imaginary cursor to the left
        event.preventDefault();
        console.log('left arrow key pressed');
        if (INPUT_BOX.value.length > 0) {

        // remove the last character from input box and add it to the end
        var input = INPUT_BOX.value;
        var lastChar = input[input.length - 1];
        INPUT_BOX.value = input.slice(0,input.length - 1);
        AFTER_CURSOR.innerHTML += lastChar;
        }

    } else if (key == 39) { // right arrow key then move imaginary cursor to the right
        event.preventDefault();
        console.log('right arrow key pressed');
        if (AFTER_CURSOR.innerHTML.length > 0) {
            var char = AFTER_CURSOR.innerHTML[0];
            AFTER_CURSOR.innerHTML = AFTER_CURSOR.innerHTML.slice(1);
            INPUT_BOX.value += char;
        }
    }

    resetInputBoxSize();
}

function submitInput() {
    // trim INPUT_BOX.value
    const input = (INPUT_BOX.value + AFTER_CURSOR.innerText) .trim();
    if (input === 'clear') {
        SCREEN.innerHTML = '';
        INPUT_BOX.value = '';
        AFTER_CURSOR.innerHTML = '';
        resetInputBoxSize();
        return;
    }
    var prevcommand =  `<div id="input-container">
<span class="username">guest@beautifulthings:</span>
<span class="current-path">~</span>$ ${input}
</div>`

    console.log('this was the input',input);
    // execute command
    SCREEN.innerHTML += prevcommand;

    executeCommand(input)

    INPUT_BOX.value = '';
    AFTER_CURSOR.innerHTML = '';
    resetInputBoxSize();
    INPUT_BOX.focus();
    // add input to history
}

function executeCommand(command) {
    var commandname = command.split(' ')[0];
    var arguments = command.split(' ').slice(1);
    var command = COMMANDS.find(command => command.name == commandname);
    if (command) {
        // execute command with arguments
        command.execute(arguments);        
    }
}