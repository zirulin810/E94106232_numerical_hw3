import numpy as np
from scipy.interpolate import interp1d

def f(x):
    return x - np.exp(-x)

x_data = np.array([-0.3, -0.4, -0.5, -0.6])
y_data = np.array([0.740818, 0.670320, 0.606531, 0.548812])

interpolator = interp1d(y_data, x_data, kind='linear', fill_value='extrapolate')

x_guess = -0.4
tolerance = 1e-6
max_iterations = 100

print("\n")

for i in range(max_iterations):
    y_current = f(x_guess)
    
    if abs(y_current) < tolerance:
        print(f"Converged to solution: x = {x_guess:.6f}")
        break
    
    try:
        x_next = np.exp(-x_guess)
    except ValueError:
        print("Warning: Calculation out of range")
        break
    
    x_guess = x_next
    
    print(f"Iteration {i+1}: x = {x_guess:.6f}, f(x) = {y_current:.6f}")
    
    if i == max_iterations - 1:
        print("Warning: Maximum iterations reached, may not have converged")

print("\n")