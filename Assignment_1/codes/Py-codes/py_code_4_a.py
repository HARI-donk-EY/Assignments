import matplotlib.pyplot as plt
import numpy as np

p = [1, -4, -5]
# since the equation is K^2 - 4K - 5 = 0.

rts = np.roots(p)

print(rts)
# The roots would be printed as outputs.

# 100 linearly spaced numbers
x = np.linspace(-7,7,100)

# the function, which is y = x^2 - 4x - 5 here
y = x**2 - (4*x) - 5

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.grid()

# show the plot
plt.show()

