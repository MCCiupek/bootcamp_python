import numpy as np
import copy
from NumPyCreator import NumPyCreator

class ColorFilter():

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        return 1 - array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        res = np.zeros(array.shape)
        for row in range(0, res.shape[0]):
            for col in range(0, res.shape[1]):
                res[row, col] = np.dstack((np.zeros(1), np.zeros(1), array[row, col][-1:]))
        return res
        

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        return copy.deepcopy(array[:, :][:] * [0, 1, 0])

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        return array - self.to_green(array) - self.to_blue(array)

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        interval = np.linspace(0, 1, 5)
        for i in np.arange(1, 5):
            array[(array>=interval[i - 1]) & (array<interval[i])] = interval[i - 1]
        return array

    def to_grayscale(self, array, filter, w=None):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if array is None:
            return None
        if filter in ['m', 'mean']:
            return np.dstack((np.sum(array, -1), np.sum(array, -1), np.sum(array, -1))) / 3
        elif filter in ['w', 'weight']:
            npc = NumPyCreator()
            w = npc.from_list(w)
            if w is not None and w.shape == (3,) and np.sum(w, axis=0) == 1.0 and (np.sum(((w >= 0) & (w <= 1)).astype(int)) == 3):
                means = np.sum(array * np.broadcast_to(w, array.shape), -1) / 3
                return np.dstack((means, means, means))
        return None

if __name__ == "__main__":

    from ImageProcessor import ImageProcessor

    imp = ImageProcessor()
    #arr = imp.load("../ressources/42AI.png")
    arr = imp.load("../ressources/elon_canaGAN.png")
    arr = arr[:,:,:3]

    from ColorFilter import ColorFilter
    
    cf = ColorFilter()

    arr_inv = cf.invert(arr)
    arr_b = cf.to_blue(arr)
    arr_g = cf.to_green(arr)
    arr_r = cf.to_red(arr)
    arr_g1 = cf.to_grayscale(arr, 'm')
    arr_g2 = cf.to_grayscale(arr, 'weight', [0.2, 0.3, 0.5])
    arr_c = cf.to_celluloid(arr)

    imp.display(arr)
    imp.display(arr_inv)  
    imp.display(arr_b)
    imp.display(arr_g)
    imp.display(arr_r)
    imp.display(arr_g1)
    imp.display(arr_g2)
    imp.display(arr_c)