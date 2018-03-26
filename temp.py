import cv2
import numpy as np
img_rgb = cv2.imread('paper.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('tick.jpg',0)
w, h = template.shape[::-1]
print(w)
print(h)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where( res >= threshold)
count=0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
cv2.imwrite('results.png',img_rgb)

