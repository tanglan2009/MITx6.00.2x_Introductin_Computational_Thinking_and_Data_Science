
class Shape(object):
    def __eq__(s1, s2):
        return s1.area() == s2.area()
    def __ge__(s1, s2):
        return s1.area() >= s2.area()

class Square(Shape):
    def __init__(self, h):
        self.side = float(h)
    def area(self):
        return self.side **2
    def __str__(self):
        return 'Square with side ' + str(self.side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

def f(L):
    if len(L) == 0:
        return None
    x = L[0]
    print 'x =', x  # Output Circle with radius 0
    for s in L:
        if s >= x:
            x = s
        print 's = ', s
        print 'x =', x
    return x

s = Square(4)
print s
print s.area()
L = []
shapes = {0: Circle, 1: Square}
for i in range(10):
    L.append(shapes[i%2](i))
    print L[i]
print L[4]
print f(L)


x = '11010'
y = 0
for i in range(len(x)):
    y += int(x[i])*(2**i)
print y
