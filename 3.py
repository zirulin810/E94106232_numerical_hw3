import numpy as np
from scipy.interpolate import CubicHermiteSpline
import matplotlib.pyplot as plt

T = np.array([0, 3, 5, 8, 13])
D = np.array([0, 200, 375, 620, 990])
V = np.array([75, 77, 80, 74, 72])

hermite = CubicHermiteSpline(T, D, V)

t_10 = 10
position_10 = hermite(t_10)
velocity_10 = hermite.derivative()(t_10)

print(f"a. At t = 10s:")
print(f"   Position = {position_10:.2f} ft")
print(f"   Velocity = {velocity_10:.2f} ft/s")

speed_limit = 80.67
t = np.linspace(0, 13, 1000)
velocity = hermite.derivative()(t)
exceed_limit = velocity > speed_limit

if np.any(exceed_limit):
    first_exceed = t[np.where(exceed_limit)[0][0]]
    print(f"\nb. The car did exceed the speed limit!")
    print(f"   First time exceeding speed limit at {first_exceed:.2f} seconds")
else:
    print(f"\nb. The car did not exceed the speed limit")

max_speed = np.max(velocity)
print(f"\nc. The predicted maximum speed is {max_speed:.2f} ft/s")

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, hermite(t), 'b-', label='Position')
plt.plot(T, D, 'ro', label='Data points')
plt.xlabel('Time (s)')
plt.ylabel('Distance (ft)')
plt.title('Car Position vs Time')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, velocity, 'g-', label='Velocity')
plt.plot(T, V, 'ro', label='Data points')
plt.axhline(y=speed_limit, color='r', linestyle='--', label='Speed limit (55 mi/h)')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (ft/s)')
plt.title('Car Velocity vs Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
