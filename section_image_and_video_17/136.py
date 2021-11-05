import cv2

# img = cv2.imread("galaxy_1.jpg", -1) # '-1' RBG with Alpha channel
img = cv2.imread("galaxy_1.jpg", 0) # '0' black & white

# print(type(img))
print(img) 
print(img.shape) # pixels
print(img.ndim) # two dimensional


# resize image
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


# create and show image
cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save image
cv2.imwrite("galaxy_resized.jpg", resized_img)