import sys


class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
            self.shape = (len(values), len(values[0]) if values else 0)
        elif isinstance(values, int):
            self.values = [[float(i)] for i in range(values)]
            self.shape = (values, 1)
        elif isinstance(values, tuple) and len(values) == 2:
            self.values = [[float(i)] for i in range(values[1], values[1])]
            self.shape = ((values[1]-values[0]), 1)
        else:
            raise TypeError("Unsupported type for argument")

    def dot(self, vector):
        if self.shape != vector.shape:
            return
        
        if not self.values:
            return
        
        summ = 0
        for index_row, row in enumerate(self.values):
            for index_col, col in enumerate(row):
                summ += col*vector.values[index_row][index_col]
        return summ
    
    def T(self):
        if not self.values:
            return self
        
        return Vector(list(map(list, zip(*self.values))))            

    def __add__(self, vector):
        if not isinstance(vector, Vector):
            return NotImplemented
        
        if self.shape != vector.shape:
            return NotImplemented
        
        if not self.values:
            return vector
        
        return Vector([[self.values[i][j]+vector.values[i][j] for j in range(len(self.values[i]))] for i in range(len(self.values))])

    def __radd__(self, vector):
        return self.__add__(vector)

    def __sub__(self, vector):
        return self.__add__(vector*(-1))

    def __rsub__(self, vector):
        return self.__sub__(vector)

    def __truediv__(self, number):
        try:
            if not number:
                raise ZeroDivisionError
            if not isinstance(number, (int, float)):
                raise NotImplementedError
            if not self.values:
                return self.values
            return Vector([[value/number for value in row] for row in self.values])
        except ZeroDivisionError:
            raise ZeroDivisionError("division by zero.")
        except NotImplementedError:
            raise NotImplementedError("division of a scalar by a Vector is not defined here.")

    def __rtruediv__(self, number):
        raise NotImplementedError("division of a scalar by a Vector is not defined here.")

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        if not self.values:
            return self.values
        return Vector([[value*number for value in row] for row in self.values])

    def __rmul__(self, number):
        return self.__mul__(number)

    def __str__(self):
        # txt = ""
        # for index_row, row in enumerate(self.values):
        #     for index_col, col in enumerate(row):
        #         txt = txt + "{} {}\n".format(col, row[index_col])
        # return txt
        return f"{self.values}"

    def __repr__(self):
        # txt = ""
        # for index_row, row in enumerate(self.values):
        #     for index_col, col in enumerate(row):
        #         txt = txt + "{} {}\n".format(col, row[index_col])
        # return txt
        return f"{self.values}"
