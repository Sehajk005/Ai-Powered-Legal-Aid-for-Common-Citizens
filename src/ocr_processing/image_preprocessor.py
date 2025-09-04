import cv2
from pathlib import Path


# Extract text from dirty image
def preprocess_image(image_path):
    img = cv2.imread(str(image_path)) # read the image using cv2.imread
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    _, thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # Applying binary threshold to the image, .THRESH_OTSU is a global thresholding method

    return thresh_img