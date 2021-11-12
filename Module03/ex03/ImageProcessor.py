#import imageio
import sys
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt
import cv2

class ImageProcessor():
    def load(self, path):
        try:
            array = cv2.imread(path, cv2.CV_LOAD_IMAGE_COLOR)
            print("Loading image of dimensions {0} x {1}".format(*array.shape))
            return array
        except FileNotFoundError as err:
            print("Exception: FileNotFoundError -- strerror: {0}".format(err.strerror))
            return None

    def display(self, array):
        cv2.imshow(array)
        # plt.show()


if __name__ == "__main__":

    from ImageProcessor import ImageProcessor

    imp = ImageProcessor()
    arr = imp.load("non_existing_file.png")
    # Output
    # Exception: FileNotFoundError -- strerror: No such file or directory

    print(arr)
    # Output
    # None

    arr = imp.load("empty_file.png")
    # Output
    # Exception: OSError -- strerror: None

    print(arr)
    # Output
    # None

    arr = imp.load("../resources/42AI.png")
    # Output
    # Loading image of dimensions 200 x 200
    print(arr)

    arr = imp.load("../resources/elon_canaGAN.png")
    # Output
    # Loading image of dimensions 200 x 200
    print(arr)
    
    imp.display(arr) 