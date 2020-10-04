# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:07:09 2020

@author: Hp
"""

#Matplotlib

import matplotlib.pyplot as plt
import numpy as np

#line plot
x = [5, 11, 17]
y = [12, 14, 21]
plt.plot(x,y)
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#bar graph
over = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
runs = [12, 14, 21, 14, 23, 8, 32, 12, 12, 7]
plt.bar(over, runs)
plt.title("bar graph")
plt.xlabel("over")
plt.ylabel("runs")
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([5, 10, 15, 20, 25, 30])
plt.show()

#histogram
p1 = np.random.randint(0, 200, 30)
bins = np.arange(0, 201, 40)
plt.hist(p1, bins, rwidth=0.9)
plt.title("histogram")
plt.xlabel("player 1")
plt.ylabel("bins")
plt.xticks(np.arange(0, 201, 40))
plt.show()
print(p1)

#scatter plot
x = [2, 7, 12]
y = [6, 16, 23]
plt.scatter(x, y, c='r')
plt.plot(x, y)
plt.show()

xup = np.random.randint(30, 50, 30)
yup = np.random.randint(30, 50, 30)
xlow = np.random.randint(5, 25, 30)
ylow = np.random.randint(5, 25, 30)

plt.figure(figsize=(10, 8))
plt.scatter(xup, yup, c='r', label='class A', marker='*')
plt.scatter(xlow, ylow, c='g', label='class B', marker='+')
plt.legend()   #used to show the label
plt.show()

#pie chart


