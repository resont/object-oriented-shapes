import abc, math, colors,numbers
import descriptors as desc

class ConvexPolygon(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self):
        self.fill_colour = colors.WHITE
        self.outline_colour = colors.BLACK

    @abc.abstractclassmethod
    def area(self):
        pass

    @abc.abstractclassmethod
    def perimeter(self):
        pass

    @abc.abstractclassmethod
    def draw(self):
        pass

class Triangle(ConvexPolygon):
    #boki trójkąta
    a = desc.QuantityAndType(numbers.Real)
    b = desc.QuantityAndType(numbers.Real)
    c = desc.QuantityAndType(numbers.Real)

    def __init__(self,a,b,c):
        super().__init__()
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def draw(self):
        pass

class ConvexQuadrilateral(ConvexPolygon):
    #boki czworokąta
    a = desc.QuantityAndType(numbers.Real)
    b = desc.QuantityAndType(numbers.Real)
    c = desc.QuantityAndType(numbers.Real)
    d = desc.QuantityAndType(numbers.Real)

    #przekątne czworokąta
    e = desc.QuantityAndType(numbers.Real)
    f = desc.QuantityAndType(numbers.Real)

    #kąt przecięcia przekątnych
    angle = desc.Range(0,180)

    def __init__(self,a,b,c,d,e,f,angle):
        super().__init__()
        self.a, self.b, self.c, self.d = a, b, c, d
        
        self.e, self.f = e, f

        self.angle = angle

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return (self.e * self.f)/2 * math.asin(self.angle)

    def draw(self):
        pass


class RegularPentagon(ConvexPolygon):
    #bok pięciokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a
        self.angle = 36

    def perimeter(self):
        return self.a * 5

    def area(self):
        return 5/4 * self.a ** 2 * math.atan(1/angle)

    def draw(self):
        pass

class RegularHexagon(ConvexPolygon):
    #bok sześciokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a

    def perimeter(self):
        return self.a * 6

    def area(self):
        return (3 * a ** 2 * math.sqrt(3))/2

    def draw(self):
        pass

class RegularOctagon(ConvexPolygon):
    #bok ośmiokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a

    def perimeter(self):
        return self.a * 8

    def area(self):
        return 2 * (1 + math.sqrt(2)) * self.a ** 2

    def draw(self):
        pass


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a,b,b)

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self,a):
        super().__init__(a,a)

class Parallelogram(ConvexQuadrilateral):
    def __init__(self, a, b, e, f, angle):
        super().__init__(a, b, a, b, e, f, angle)

class Kite(ConvexQuadrilateral):
    def __init__(self, a, b, e, f):
        super().__init__(a, a, b, b, e, f, 90)

class Rhombus(Kite):
    def __init__(self, a, e, f):
        super().__init__(a, a, e, f)

class Square(Rhombus):
    def __init__(self, a):
        d = a * math.sqrt(2)
        super().__init__(a, d, d)

