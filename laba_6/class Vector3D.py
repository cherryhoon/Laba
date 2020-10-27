class Vector:

    def __init__(self, a):
        A = list(map(int, a.split(',')))
        self.x = A[0]
        self.y = A[1]
        self.z = A[2]

    def __add__(self, other):
        return Vector('{},{},{}'.format(self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        return Vector('{},{},{}'.format(self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __and__(self, other):
        return Vector('{},{},{}'.format(self.y * other.z - self.z * other.y,
                                        self.z * other.x - self.x * other.z,
                                        self.x * other.y - self.y * other.x))

    def dist(self):
        return round((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5, 2)

    def __str__(self):
        return f"Вектор с координатами {self.x, self.y, self.z}"


v1 = Vector('5,6,7')
v2 = Vector('8,9,10')

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 & v2)


maximum = float('-inf')
N = int(input('Введите количество точек: '))
for i in range(N):
    S = list(map(int, input('Введите координаты точки (x y z): ').split()))
    v = Vector('{},{},{}'.format(S[0], S[1], S[2]))
    distant = Vector.dist(v)
    if distant >= maximum:
        maximum = distant
        Ans = S
print("Наиболее удаленная точка c координатами: {} находится на расстоянии {}".format([*Ans], maximum))