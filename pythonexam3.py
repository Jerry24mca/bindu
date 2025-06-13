Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... import numpy as np
... 
... # 1. PIE CHART
... labels = ['Python', 'Java', 'C++', 'JavaScript']
... sizes = [30, 25, 20, 25]
... plt.figure(figsize=(5, 5))
... plt.title("Pie Chart")
... plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
... plt.show()
... 
... # 2. BAR CHART
... languages = ['Python', 'Java', 'C++', 'JavaScript']
... popularity = [90, 80, 70, 85]
... plt.figure(figsize=(6, 4))
... plt.title("Bar Chart")
... plt.bar(languages, popularity, color='orange')
... plt.xlabel("Programming Languages")
... plt.ylabel("Popularity (%)")
... plt.show()
... 
... # 3. HISTOGRAM
... data = np.random.normal(60, 10, 200)  # mean=60, std=10, 200 data points
... plt.figure(figsize=(6, 4))
... plt.title("Histogram")
... plt.hist(data, bins=10, color='green', edgecolor='black')
... plt.xlabel("Score")
... plt.ylabel("Frequency")
... plt.show()
... 
... # 4. SCATTER PLOT
... x = np.random.rand(50)
... y = np.random.rand(50)
... plt.figure(figsize=(6, 4))
... plt.title("Scatter Plot")
... plt.scatter(x, y, color='purple', marker='o')
... plt.xlabel("X values")
... plt.ylabel("Y values")
... plt.show()
