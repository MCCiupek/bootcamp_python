import numpy as np
from numpy import random


class NumPyCreator():
    def from_list(self, lst):
        try:
            if not isinstance(lst, list):
                raise TypeError
            if len(lst) == 0:
                return np.array(lst)
            if isinstance(lst[0], list) and any(len(elem) != len(lst[0]) for elem in lst):
                raise TypeError
            return np.array(lst)
        except TypeError:
            return None
    
    def from_tuple(self, tpl):
        try:
            if not isinstance(tpl, tuple):
                raise TypeError
            return self.from_list(list(tpl))
        except TypeError:
            return None

    def from_iterable(self, itr):
        try:
            iter(itr)
            return self.from_list(list(itr))
        except TypeError:
            return None

    def from_shape(self, shape, value=0):
        try:
            [isinstance(elem, int) for elem in shape]
            if len(shape) > 2 or any(int(elem) < 0 for elem in shape):
                raise ValueError
            return np.full(shape, value)
        except ValueError:
            return None

    def random(self, shape):
        try:
            [isinstance(elem, int) for elem in shape]
            if len(shape) > 2 or any(int(elem) < 0 for elem in shape):
                raise ValueError
            if len(shape) == 1:
                return np.random.rand(shape[0])
            return np.random.rand(shape[0], shape[1])
        except ValueError:
            return None
    
    def identity(self, n):
        try:
            int(n)
            return np.identity(int(n))
        except ValueError:
            return None


if __name__ == "__main__":

    from NumPyCreator import NumPyCreator
    
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    # Output:
    # array([[1, 2, 3],
    # [6, 3, 4]])
    
    print(npc.from_list([[1,2,3],[6,4]]))
    # Output
    # None
    
    print(npc.from_list([[1,2,3],['a','b','c'],[5.0,6.1,7.8]]))
    # Output
    # array([['1', '2', '3'],
    # ['a', 'b', 'c'],
    # ['5.0', '6.1', '7.8']], dtype='<U21')
    
    print(npc.from_list(((1,2),(3,4))))
    # Output
    # None

    print(npc.from_tuple(("a","b","c")))
    # Output
    # array(['a','b','c'])
    
    print(npc.from_tuple([[1,2,3],[6,3,4]]))
    # Output
    # None
    
    print(npc.from_iterable(iter(range(5))))
    # Output
    # array([0, 1, 2, 3, 4])
    
    shape=(3,5)
    print(npc.from_shape(shape))
    # Output
    # array([[0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0]])
    
    print(npc.random(shape))
    # Output
    # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
    # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
    # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
    
    print(npc.identity(4))
    # Output
    # array([[1., 0., 0., 0.],
    # [0., 1., 0., 0.],
    # [0., 0., 1., 0.],
    # [0., 0., 0., 1.]])