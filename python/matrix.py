class Vector:
    """a class for vectors, adding and scaling"""

    def __init__(self, *data):
        self.data = data

    def __repr__(self):
        return f"{type(self).__name__}{self.data}"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __eq__(self, other):
        return all(x == y for x, y in zip(self, other))

    def __add__(self, other):
        return type(self)(*[x + y for x, y in zip(self, other)])

    def __rmul__(self, other):
        return type(self)(*[other * x for x in self])

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        return self + -other

    def __and__(self, other):
        return sum(x * y for x, y in zip(self, other))

class Matrix(Vector):
    """a class for matrices and matrix multiplication"""

    def transpose(self):
        return Matrix(*[Vector(*x) for x in zip(*self)])

    def __and__(self, other):
        return Vector(*[x & other for x in self])

    def __matmul__(self, other):
        return Matrix(*[self &  x for x in other.transpose()]).transpose()
