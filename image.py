import cv2

image_path = r'Images\Image2.jpg'    #Image path

image = cv2.imread(image_path)  #Reading the image

if image is not None:  #checking image is read or not
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to read the image.')