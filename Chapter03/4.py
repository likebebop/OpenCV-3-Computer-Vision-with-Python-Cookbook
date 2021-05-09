import cv2
import numpy as np
import random


img = np.full((512, 512, 3), 255, np.uint8)

cv2.imshow('img', img)

pts = np.arange(512).reshape(-1, 1)
# pts = np.arange(512)
print(f'pts {pts.shape} {pts.dtype}')

pts = np.hstack((pts, pts))
print(pts)
pts += np.random.uniform(-10, 10, pts.shape).astype(np.int32)
print(f'pts 2 {pts.shape} {pts.dtype}')
print('===begin===')
print(pts)
print('===end===')

cv2.line(img, (0,0), (512, 512), (0, 255, 0), 3)

for pt in pts:
    cv2.circle(img, (int(pt[0]), int(pt[1])), 3, (0, 0, 255))

cv2.imshow('Fit line', img)
cv2.waitKey()
cv2.destroyAllWindows()

vx,vy,x,y = cv2.fitLine(pts, cv2.DIST_L2, 0, 0.01, 0.01)
y0 = int(y - x*vy/vx)
y1 = int((512 - x)*vy/vx + y)
cv2.line(img, (0, y0), (512, y1), (0, 0, 0), 3)

cv2.imshow('Fit line', img)
cv2.waitKey()
cv2.destroyAllWindows()