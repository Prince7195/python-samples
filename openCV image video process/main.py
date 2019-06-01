import cv2

img_grey = cv2.imread("images\galaxy.jpg", 0)

print(img_grey)
print(img_grey.shape)
print(img_grey.ndim)


resized_img = cv2.resize(img_grey, (int(img_grey.shape[1]/2), int(img_grey.shape[0]/2))) # (column, row)
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("resized_images\Galaxy_resized.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()