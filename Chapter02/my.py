import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('../data/Lena.png', 0).astype(np.float32) / 255

dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(image, cv2.CV_32F, 0, 1)
dxdy = cv2.Sobel(image, cv2.CV_32F, 1, 1)

plt.figure(figsize=(8,4))
plt.subplot(141)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')
plt.subplot(142)
plt.axis('off')
plt.imshow(dx, cmap='gray')
plt.title(r'$\frac{dI}{dx}$')
plt.subplot(143)
plt.axis('off')
plt.title(r'$\frac{dI}{dy}$')
plt.imshow(dy, cmap='gray')
plt.subplot(144)
plt.axis('off')
plt.title(r'$\frac{dI}{dy}$')
plt.imshow(dxdy, cmap='gray')
plt.tight_layout()
plt.show()