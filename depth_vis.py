"""
find suitable color map from: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
"""


import matplotlib.pyplot as plt

img=plt.imread('depth.png')

plt.imshow(img, cmap='jet')
plt.show()



