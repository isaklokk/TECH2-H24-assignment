"""
TECH2 mandatory assignment - Part A

"""
from math import sqrt

num_lst = [1, 2, 3 , 4, 5]
x = num_lst

def std_loops(x): 
    N = 0
    for _ in x: # Calculating the length of the list manually
        N += 1

    total_sum = 0
    for i in x: # Calculating the mean of x
        total_sum += i
    mean_x = total_sum / N # The mean of x

    sum_S = 0
    for i in x: # Calculating the mean of squares
        sum_S += i ** 2
        
    mean_S = sum_S / N # The mean of squares
    variance = mean_S - (mean_x ** 2) # The variance
    S_deviation = sqrt(variance) # The standard deviation

    return S_deviation

print('The standard deviation with alternative 1:', std_loops(x))



def std_builtin(x):
    N = len(x)

    mean_x = sum(x) / N # Calculating the mean of x
    
    sum_S = sum(i**2 for i in x) 
    mean_S = sum_S / N # Calculating the mean of squares

    variance = mean_S - mean_x ** 2 # Calculating variance
    s_deviation = sqrt(variance) # Calculating the standard deviation
    return s_deviation

print('The standard deviation with alternative 2:', std_builtin(x))


import numpy as np

std_np = np.std(x) # Calculating the standard deviation
print('The standard deviation with alternative 3:', std_np)

# Compare all three methods
if round(std_loops(x), 5) == round(std_builtin(x), 5) == round(std_np, 5):
    print('All three methods calculate the same standard deviations for num_lst')
else:
    print('There is a difference in the standard deviation calculations')
