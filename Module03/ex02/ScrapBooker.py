import numpy as np

class ScrapBooker():

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if array is None or dim is None or len(array.shape) != 2:
            return None
        if position > array.shape or position < (0, 0) or dim < (0, 0):
            return None
        if tuple(sum(x) for x in zip(position, dim)) > array.shape:
            return None
        return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if axis not in [0, 1]:
            return None
        if n not in range(0, array.shape[axis]):
            return None
        if array is None or len(array.shape) != 2:
            return None
        return np.delete(array, list(range(n - 1, array.shape[abs(axis - 1)], n)), axis=abs(axis - 1))

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if axis not in [0, 1]:
            return None
        if n < 0:
            return None
        if array is None or len(array.shape) != 2:
            return None
        cpy = array
        for i in range(1, n):
            array = np.append(array, cpy, axis=axis)
        return array

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        for axis in [0, 1]:
            array = self.juxtapose(array, dim[axis], axis)
        return array


if __name__ == "__main__":

    import numpy as np

    spb = ScrapBooker()

    print("--------------------")
    arr1 = np.arange(0,25).reshape(5,5)
    print(arr1)
    print()
    print(spb.crop(arr1, (3,1),(1,0)))
    print("--------------------")

    print("--------------------")
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(arr2)
    print()
    print(spb.thin(arr2,3,0))
    print("--------------------")

    print("--------------------")
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(arr3)
    print()
    print(spb.juxtapose(arr3, 3, 1))
    print("--------------------")

    print("--------------------")
    arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(arr4)
    print()
    print(spb.mosaic(arr4, (2, 3)))
    print("--------------------")
