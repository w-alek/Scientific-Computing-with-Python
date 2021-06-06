from math import sqrt


class Vector:
    '''3D vectors class'''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        ''' string "Vector(x, y, z)'''
        return '{}({}, {}, {})'.format(type(self).__name__, self.x, self.y, self.z)
        # or just 'Vector instead of type(self).__name__'

    def __eq__(self, other):
        '''v == w'''
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        '''v != w'''
        return not self == other

    def __add__(self, other):
        '''v + w'''
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        '''v - w'''
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        '''dot product'''
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        '''cross product'''
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def length(self):
        '''length of the vector'''
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __hash__(self):
        '''hash of the vector'''
        # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended
