'''
After attending Amrita summer training camp, N programmers, getting bored of programming, decided to have a car race. Each of them bring their own car to the race.

As the camp also includes school children, to level the playing field, some of the coders are allowed to have a head start. The ith programmer starts his race at a distance Di ahead of the starting line at time T = 0. The speed of the car of the ith coder is equal to Si.

After time T, the position of ith coder will be Pi(T) = Si * T + Di. Let's define f(T) = max(Pi(T)) - min(Pj(T)). The race ends at time T = K. You need to find the minimum value of f(T) during the whole race.

Input:
The first line of the input contains two integers N and K denoting the number of coders and the duration of the race.

The next N lines contains two integers each, ith line contains Si and Di.

Output:
Output the minimum value of f(T) during the whole race exactly upto 6 places after the decimal point.

Example
Input:

2 10
20 0
10 10

Output:

0.000000
Explanation

At t = 1 sec, both the coders will have same position, which makes f(1) = 0.
'''

if __name__ == "__main__":
    pass
