#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <fstream>


std::vector<int> three_n_plus_1(int n)
{
    std::vector<int> y;
    std::unordered_map<int, bool> m;
    int x = n;
    while (m.find(x) == m.end())
    {
        y.push_back(x);
        m[x] = true;
        if (x % 2 == 0)
        {
            x = x / 2;
        }
        else
        {
            x = 3 * x + 1;
        }
    }
    return y;
}

int main()
{
    std::string numbers;
    std::cout << "Enter the numbers (seperated by space): ";
    std::getline(std::cin, numbers);
    std::istringstream iss(numbers);
    std::vector<std::string> numbers_str((std::istream_iterator<std::string>(iss)),
                                         std::istream_iterator<std::string>());
    std::vector<int> numbers_int;
    for (auto &i : numbers_str)
    {
        numbers_int.push_back(std::stoi(i));
    }

    // output the numbers to afile for plotting them using gnuplot
    std::ofstream outfile; 
    outfile.open("three_n_plus_1.dat");


    for (auto &i : numbers_int)
    {
        std::vector<int> y = three_n_plus_1(i);
        for (auto &j : y)
        {
            std::cout << j << " ";
            outfile << j << std::endl;
        }
    }
    std::cout << std::endl;
    outfile.close();
    return 0;
}
