import cv2

def img_read(img_path):
    img = cv2.imread(img_path)
    return img