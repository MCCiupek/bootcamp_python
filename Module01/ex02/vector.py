import sys


def add_lists(list_x, list_y):
    return [x + y for (x, y) in zip(list_x, list_y)]


def mul_lists(list_x, scalar):
    return [x * scalar for x in list_x]


def dot_prod(list_x, list_y):
    return [x * y for (x, y) in zip(list_x, list_y)]


def check_type(values, typ):
    return any(isinstance(val, typ) for val in values)


class Vector:
    def __init__(self, args=None):
        try:
            if args is None:
                self.__init_default__()
            elif isinstance(args, list) and args != []:
                self.__init_list__(args)
            elif isinstance(args, int) and args >= 0:
                self.__init_size__(args)
            elif isinstance(args, range) and len(args) > 0:
                self.__init_range__(args)
            else:
                raise ValueError("Couldn't instanciate object Vector")
        except ValueError as err:
            sys.stderr.write("Error: {0}\n".format(err))
            sys.exit()
    
    def __init_default__(self):
        self.values = []
        self.shape = [0, 0]

    def __init_list__(self, values:list):
        self.values = values
        if type(values[0]) == list:
            if len(values[0]) > 1:
                raise ValueError("Incorrect dimensions")
            self.shape = [len(values), 1]
        else:
            self.shape = [1, len(values)]
        if not self.check_type(float):
            raise ValueError("Values must be only floats")
        

    def __init_size__(self, size:int):
        self.values = [ [float(x)] for x in range(0, size) ]
        self.shape = [size, 1]
        if not self.check_type(float):
            raise ValueError("Values must be only floats")

    def __init_range__(self, rg:range):
        self.values = [ [float(x)] for x in rg ]
        self.shape = [len(self.values), 1]
        if not self.check_type(float):
            raise ValueError("Values must be only floats")

    def check_type(self, typ):
        if self.shape[0] == 1:
            return check_type(self.values, float)
        if self.shape[0] > 1:
            return any(check_type(self.values[i], float) for i in range(0, self.shape[0]))

    def __add__(self, vec):
        try:
            if not isinstance(vec, Vector):
                raise ValueError("Add/Sub with non vector object.")
                return None
            if self.shape != vec.shape:
                raise ValueError("Add/Sub with mismatching dimensions.")
                return None
            elif self.shape[0] == 0:
                return Vector()
            elif self.shape[0] == 1:
                return Vector(add_lists(self.values, vec.values))
            else:
                return Vector([add_lists(self.values[i], vec.values[i]) for i in range(0, self.shape[0])])
        except ValueError as err:
            sys.stderr.write("Error: {0}\n".format(err))
            return None

    def __radd__(self, vec):
        return vec.__add__(self)
    
    def __sub__(self, vec):
        return self + ((-1.0) * vec)
    
    def __rsub__(self, vec):
        return vec.__sub__(self)

    def __mul__(self, scalar):
        try:
            try:
                float(scalar)
            except ValueError:
                raise ValueError("Mult/Div by non scalar object.")
            if self.shape[0] == 0:
                return Vector()
            elif self.shape[0] == 1:
                return Vector(mul_lists(self.values, float(scalar)))
            else:
                return Vector([mul_lists(self.values[i], float(scalar)) for i in range(0, self.shape[0])])
        except ValueError as err:
            sys.stderr.write("Error: {0}\n".format(err))
            return None

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        try:
            try:
                float(scalar)
            except ValueError:
                raise ValueError("__div__: Division by non scalar object.")
            if scalar == 0:
                raise ValueError("__div__: Division by zero.")
                return None
            if self.shape[0] == 0:
                return Vector()
            elif self.shape[0] == 1:
                return Vector(mul_lists(self.values, 1 / float(scalar)))
            else:
                return Vector([mul_lists(self.values[i], 1 / float(scalar)) for i in range(0, self.shape[0])])
        except ValueError as err:
            sys.stderr.write("Error: {0}\n".format(err))
            return None

    def __rtruediv__(self, scalar):
        return self / scalar

    def __str__(self):
        return "Vector{0}: {1}".format(self.shape, self.values)
    
    def __repr__(self):
        return "vector.Vector({0})".format(self.values)

    def dot(self, vec):
        try:
            if not isinstance(vec, Vector):
                raise ValueError("Dot product with non vector object.")
            elif self.shape != vec.shape:
                raise ValueError("Dot product with mismatching dimensions.")
            elif self.shape[0] == 0:
                return self
            elif self.shape[0] == 1:
                self.values = dot_prod(self.values, vec.values)
            else:
                self.values = [dot_prod(self.values[i], vec.values[i]) for i in range(0, self.shape[0])]
            return self
        except ValueError as err:
            sys.stderr.write("Error: {0}\n".format(err))
            return self
    
    def T(self):
        if self.shape[0] == 1:
            self.values = [[x] for x in self.values]
        if self.shape[1] == 1:
            self.values = [x[0] for x in self.values]
        self.shape = self.shape[::-1]
        return self
