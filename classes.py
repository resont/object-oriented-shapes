import abc, math, numbers
import descriptors as desc
import colors
from tkinter import *

class ConvexPolygon(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self):
        self.fill_color = colors.fill_color
        self.outline_color = colors.outline_color

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

        canvas = Canvas(root, width=600, height=600)
        canvas.pack()

        canvas.create_polygon(points, fill=self.fill_color, outline=self.outline_color)        
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

        vector = (200,200)

        alpha = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)/(2 * self.a * self.b)))

        point_a = (0 + vector[0],0 + vector[1])
        point_b = (vector[0] + math.cos(math.radians(alpha/2)) * self.b, vector[1] + math.sin(math.radians(alpha/2)) * self.b)
        point_c = (point_b[0] + math.cos(math.radians(180 - alpha/2)) * self.c, point_b[1] + math.sin(math.radians(180 - alpha/2)) * self.c)

        self.base_drawing([point_a,point_b,point_c])


class ConvexQuadrilateral(ConvexPolygon):
    #przekątne czworokąta
    AC = desc.QuantityAndType(numbers.Real)
    BD = desc.QuantityAndType(numbers.Real)

    #kąt przecięcia przekątnych
    angle = desc.Range(0,180)

    #stosunek przecięcia przekątnych
    AC_custs_BD = desc.Range(0,1)
    BD_cuts_AC = desc.Range(0,1)

    def __init__(self,e,f,angle,AC_ratio,BD_ratio):
        super().__init__()
        self.AC, self.BD = e, f

        self.angle = angle

        self.AC_custs_BD = AC_ratio
        self.BD_cuts_AC = BD_ratio

        self._angles()


    def perimeter(self):
        AB = self.AS ** 2 + self.BS ** 2 - 2 * self.AS * self.BS * math.cos(math.radians(self.ASB_angle))
        AB = math.sqrt(AB)
        BC = self.BS ** 2 + self.CS ** 2 - 2 * self.BS * self.CS * math.cos(math.radians(self.BSC_angle))
        BC = math.sqrt(BC)
        CD = self.CS ** 2 + self.DS ** 2 - 2 * self.CS * self.DS * math.cos(math.radians(self.DSC_angle))
        CD = math.sqrt(CD)
        DA = self.DS ** 2 + self.AS ** 2 - 2 * self.DS * self.AS * math.cos(math.radians(self.ASD_angle))
        DA = math.sqrt(DA)
        perimeter = AB + BC + CD + DA
        return "{:.2f}".format(perimeter)

    def area(self):
        area = (self.AC * self.BD)/2 * math.sin(math.radians(self.angle))
        return "{:.2f}".format(area)

    def draw(self):
        point_a = (200,200)
        point_s = (point_a[0] + math.cos(0) * self.AS, point_a[1] + math.sin(0) * self.AS)
        point_b = (point_s[0] + math.cos(math.radians(180 - self.ASB_angle)) * self.BS, point_s[1] + math.sin(math.radians(180 - self.ASB_angle)) * self.BS)
        point_c = (point_s[0] +  math.cos(0) * self.CS, point_s[1] + math.sin(0) * self.CS)
        point_d = (point_s[0] + math.cos(math.radians(180 + self.ASD_angle)) * self.DS, point_s[1] + math.sin(math.radians(180 + self.ASD_angle)) * self.DS)

        points = [point_a,point_b,point_c,point_d]

        self.base_drawing(points)

    def _angles(self):
        self.ASB_angle = self.angle

        self.AS = self.BD_cuts_AC * self.AC
        self.CS = self.AC = self.AS

        self.BS = self.AC_custs_BD * self.BD
        self.DS = self.BD - self.BS

        self.DSC_angle = self.ASB_angle
        self.ASD_angle = 180 - self.ASB_angle
        self.BSC_angle = self.ASD_angle




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
        vector = (250,250)
        angle = 360/5
        points = []
        for i in range(5):
            points.append((
                vector[0] + self.a * math.cos(math.pi/180 * i * angle),
                vector[1] + self.a * math.sin(math.pi/180 * i * angle)
            ))
        
        self.base_drawing(points)

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
        vector = (250,250)
        angle = 360/6
        points = []
        for i in range(6):
            points.append((
                vector[0] + self.a * math.cos(math.pi/180 * i * angle),
                vector[1] + self.a * math.sin(math.pi/180 * i * angle)
            ))
        
        self.base_drawing(points)

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
        vector = (250,250)
        angle = 360/8
        points = []
        for i in range(8):
            points.append((
                vector[0] + self.a * math.cos(math.pi/180 * i * angle),
                vector[1] + self.a * math.sin(math.pi/180 * i * angle)
            ))
        
        self.base_drawing(points)


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a,a,b)


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self,a):
        super().__init__(a,a)


class Parallelogram(ConvexQuadrilateral):
    def __init__(self, e, f, angle):
        super().__init__(e, f, angle, 0.5, 0.5)


class Kite(ConvexQuadrilateral):
    def __init__(self, e, f):
        super().__init__(e, f, 90, 0.7, 0.5)


class Rhombus(Parallelogram):
    def __init__(self, e, f):
        super().__init__(e, f, 90)


class Square(Rhombus):
    def __init__(self, e):
        super().__init__(e, e)


