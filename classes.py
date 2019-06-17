import abc, math, numbers
import descriptors as desc
from colors import Colors
from tkinter import *

class ConvexPolygon(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self):
        self.fill_colour = Colors.WHITE
        self.outline_colour = Colors.BLACK

    @abc.abstractclassmethod
    def area(self):
        pass

    @abc.abstractclassmethod
    def perimeter(self):
        pass

    @abc.abstractclassmethod
    def draw(self):
        pass

    def base_drawing(self, points):
        root = Tk()

        canvas = Canvas(root, width=500, height=500)
        canvas.pack()

        canvas.create_polygon(points, fill=self.fill_colour, outline=self.outline_colour)        
        mainloop()

class Triangle(ConvexPolygon):
    #boki trójkąta
    a = desc.QuantityAndType(numbers.Real)
    b = desc.QuantityAndType(numbers.Real)
    c = desc.QuantityAndType(numbers.Real)

    def __init__(self,a,b,c):
        super().__init__()
        self.a, self.b, self.c = a, b, c
        

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return "{:.2f}".format(perimeter)

    def area(self):
        p = float(self.perimeter()) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return "{:.2f}".format(area)

    def draw(self):

        vector = (100,100)

        alpha = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)/(2 * self.a * self.b)))

        point_a = (0 + vector[0],0 + vector[1])
        point_b = (vector[0] + math.cos(math.radians(alpha/2)) * self.b, vector[1] + math.sin(math.radians(alpha/2)) * self.b)
        point_c = (point_b[0] + math.cos(math.radians(180 - alpha/2)) * self.c, point_b[1] + math.sin(math.radians(180 - alpha/2)) * self.c)

        self.base_drawing([point_a,point_b,point_c])


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

        self.angle = math.radians(angle)

    def perimeter(self):
        perimeter = self.a + self.b + self.c + self.d
        return "{:.2f}".format(perimeter)

    def area(self):
        area = (self.e * self.f)/2 * math.sin(self.angle)
        return "{:.2f}".format(area)

    def draw(self):
        pass


class RegularPentagon(ConvexPolygon):
    #bok pięciokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a
        self.angle = math.radians(36)

    def perimeter(self):
        perimeter = self.a * 5
        return "{:.2f}".format(perimeter)

    def area(self):
        area = 5/4 * self.a ** 2 * (1/math.tan(self.angle))
        return "{:.2f}".format(area)

    def draw(self):
        pass

class RegularHexagon(ConvexPolygon):
    #bok sześciokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a

    def perimeter(self):
        perimeter = self.a * 6
        return "{:.2f}".format(perimeter)

    def area(self):
        area = (3 * self.a ** 2 * math.sqrt(3))/2
        return "{:.2f}".format(area)

    def draw(self):
        pass

class RegularOctagon(ConvexPolygon):
    #bok ośmiokąta
    a = desc.QuantityAndType(numbers.Real)

    def __init__(self,a):
        super().__init__()
        self.a = a

    def perimeter(self):
        perimeter = self.a * 8
        return "{:.2f}".format(perimeter)

    def area(self):
        area = 2 * (1 + math.sqrt(2)) * self.a ** 2
        return "{:.2f}".format(area)

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
        d = float(a) * math.sqrt(2)
        super().__init__(a, d, d)


