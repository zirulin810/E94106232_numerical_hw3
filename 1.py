import numpy as np
from scipy.special import factorial

def get_lagrange_polynomial(x_points, y_points):
    n = len(x_points)
    terms = []
    
    for i in range(n):
        numerator_terms = []
        denominator_terms = []
        for j in range(n):
            if i != j:
                numerator_terms.append(f"(x-{x_points[j]:.3f})")
                denominator_terms.append(f"({x_points[i]:.3f}-{x_points[j]:.3f})")
        
        numerator = "*".join(numerator_terms)
        denominator = "*".join(denominator_terms)
        coefficient = y_points[i]
        
        term = f"({coefficient:.4f}*{numerator}/{denominator})"
        terms.append(term)
    
    return "+".join(terms)

def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result

def error_bound(x, x_points, n):
    M_n_plus_1 = 1
    w_x = 1
    for i in range(len(x_points)):
        w_x *= (x - x_points[i])
    
    error = abs(M_n_plus_1 / factorial(len(x_points))) * abs(w_x)
    return error

def print_separator():
    print("-"*80)

if __name__ == "__main__":
    x_points = np.array([0.698, 0.733, 0.768, 0.803])
    y_points = np.array([0.7661, 0.7432, 0.7193, 0.6946])
    x_target = 0.750
    true_value = 0.7317
    
    for n in range(1, 5):
        print_separator()
        print(f"{n}th Lagrange interpolation polynomial：")
        
        if n == 4:
            x_used = np.append(x_points, x_target)
            y_used = np.append(y_points, true_value)
        else:
            x_used = x_points[:n+1]
            y_used = y_points[:n+1]
        
        print("\nPoints used：")
        for i in range(len(x_used)):
            print(f"({x_used[i]:.3f}, {y_used[i]:.4f})")
        
        result = lagrange_interpolation(x_target, x_used, y_used)
        
        bound = error_bound(x_target, x_used, n)
        actual_error = abs(result - true_value)
        relative_error = actual_error / abs(true_value) * 100
        
        print(f"\nResult = {result:.7f}")
        print(f"Error bound = {bound:.7f}")
        print(f"Absolute error = {actual_error:.7f}")
        print(f"Relative error = {relative_error:.7f}%")
