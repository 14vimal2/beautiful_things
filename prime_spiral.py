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
