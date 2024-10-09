class Vector:
    """a class for vectors, adding and scaling"""

    def __init__(self, *data):
        self.data = data

    def __repr__(self):
        return f"Vector{self.data}"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __eq__(self, other):
        return all(x == y for x, y in zip(self, other))

    def __add__(self, other):
        return Vector(*[x + y for x, y in zip(self, other)])

    def __rmul__(self, other):
        return Vector(*[other * x for x in self])

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        return self + -other

    def __and__(self, other):
        return sum(x * y for x, y in zip(self, other))
