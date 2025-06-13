Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... a = 5
... b = 3
... 
... theta = np.linspace(0, 2 * np.pi, 1000)
... x = a * np.cos(theta)
... y = b * np.sin(theta)
... 
... plt.figure(figsize=(6, 6))
... plt.plot(x, y, label='Elliptical Orbit', color='blue')
... plt.plot(0, 0, 'yo', label='Focus (Sun)')
... plt.title('Elliptical Orbit with Focus')
... plt.xlabel('X-axis')
... plt.ylabel('Y-axis')
... plt.grid(True)
... plt.axis('equal')
... plt.legend()
