import matplotlib.pyplot as plt

img=plt.imread('depth.png')

plt.imshow(img, cmap='jet')
plt.show()