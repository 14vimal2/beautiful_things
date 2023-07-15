// # generate prime number list
// import matplotlib.pyplot as plt

// plt.style.use('dark_background')         



// N = int(input('Enter the max limit N: '))

// sieve = [True] * (N + 1)
// primes = []

// for i in range(2, N+1):
//     if sieve[i]:
//         primes.append(i)
//         for j in range(i, N+1,i):
//             sieve[j] = False
// # print(primes)


// # plotting of ulam spiral
// x, y = 0, 0
// axis = 0
// xch, ych = 1, 1
// xgoal, ygoal = 1, 1
// current = 1
// while current <= N:
//     if current in primes:
//         plt.plot(x, y, 'r.')
//     current += 1
//     if axis == 0:
//         # check if coordinate will move in +ve or -ve direction
//         if xch & 1 == 1: # if xch is odd then +ve
//             x += 1
//         else:
//             x -= 1
        
//         if xgoal == x:
//             axis = 1
//             xch += 1
//             if xch & 1 == 1:
//                 xgoal = x + xch
//             else:
//                 xgoal = x - xch

//     elif axis == 1:
//         if ych & 1 == 1:
//             y += 1
//         else:
//             y -= 1
        
//         if ygoal == y:
//             axis = 0
//             ych += 1
//             if ych & 1 == 1:
//                 ygoal = y + ych
//             else:
//                 ygoal = y - ych
        


// plt.show()  

# include <iostream>
# include <vector>
# include <unordered_set>


int main() {
    int N;
    std::cout << "Enter the max limit N: ";
    std::cin >> N;
    std::vector<bool> sieve(N+1, true);
    // std::vector<int> primes;
    std::unordered_set<int> primes;
    for (int i = 2; i <= N; i++) {
        if (sieve[i]) {
            primes.insert(i);
            for (int j = i; j <= N; j += i) {
                sieve[j] = false;
            }
        }
    }

    for (auto &i : primes) {
        std::cout << i << " ";
    }

    // plotting of ulam spiral
    int x = 0, y = 0;
    int axis = 0;
    int xch = 1, ych = 1;
    int xgoal = 1, ygoal = 1;
    int current = 1;
    // while (current <= N) {
    //     if (std::find(primes.begin(), primes.end(), current) != primes.end()) {
    //         std::cout << x << " " << y << std::endl;
    //     }
    //     current += 1;
    //     if (axis == 0) {
    //         // check if coordinate will move in +ve or -ve direction
    //         if (xch & 1 == 1) { // if xch is odd then +ve
    //             x += 1;
    //         }
    //         else {
    //             x -= 1;
    //         }
            
    //         if (xgoal == x) {
    //             axis = 1;
    //             xch += 1;
    //             if (xch & 1 == 1) {
    //                 xgoal = x + xch;
    //             }
    //             else {
    //                 xgoal = x - xch;
    //             }
    //         }

    //     }
    //     else if (axis == 1) {
    //         if (ych & 1 == 1) {
    //             y += 1;
    //         }
    //         else {
    //             y -= 1;
    //         }
            
    //         if (ygoal == y) {
    //             axis = 0;
    //             ych += 1;
    //             if (ych & 1 == 1) {
    //                 ygoal = y + ych;
    //             }
    //             else {
    //                 ygoal = y - ych;
    //             }
    //         }
    //     }
    // }
}