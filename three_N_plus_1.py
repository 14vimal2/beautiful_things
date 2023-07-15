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
plt.title("3n+1")
plt.legend()
plt.show()