import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

mat_img = np.array(Image.open('lena_100.png'))
mat_img_gray = mat_img[:, :, 0]
# plt.imshow(mat_img_gray, cmap='gray')
# plt.show()
# mat_img_gray = np.array([[255, 255, 255, 255],[255, 255, 255, 0], [255, 255, 150, 150], [255, 255, 255, 0]])

n = mat_img_gray.size
nx = mat_img_gray.shape[0]
a = 0.2
b = 0.2
mat_A = np.eye(n) * a

for i in range(mat_img_gray.size):
    if i-1 >= 0:
        mat_A[i, i-1] = b
    if i+1 < n:
        mat_A[i, i+1] = b
    if i+nx < n:
        mat_A[i, i+nx] = b
    if i-nx >= 0:
        mat_A[i, i-nx] = b

mat_img_blur = (mat_A @ mat_img_gray.reshape(n)).reshape(mat_img_gray.shape)
mat_img_box = ndimage.uniform_filter(mat_img_gray, size=3)

f, ax = plt.subplots(1,3) 

ax[0].imshow(mat_img_blur, cmap='gray')
ax[1].imshow(mat_img_gray, cmap='gray')
ax[2].imshow(mat_img_box, cmap='gray')
plt.show()