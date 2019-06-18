from classes import *
import colors

class Menu:
    def __init__(self):
        self.options = {
            "1" : self.triangles,
            "2" : self.quadrilaterals,
            "3" : self.regular_pentagon,
            "4" : self.regular_hexagon,
            "5" : self.regular_octagon,
            "6" : self.set_color,
            "0" : self.exit_program
        }

        self.menu_triangles = {
            "1" : self.triangle,
            "2" : self.isosceles_triangle,
            "3" : self.equilateral_triangle
        }

        self.menu_quadrilaterals = {
            "1" : self.quadrilateral,
            "2" : self.parallelogram,
            "3" : self.kite,
            "4" : self.rhombus,
            "5" : self.square
        }

        self.menu_colors = {
            "1" : self.fill_color,
            "2" : self.outline_color
        }

    def triangles(self):
        print()

        for a,b in self.menu_triangles.items():
            print(f"{a} : {b.__name__}")

        option = input("Choose an option: ")

        if option in self.menu_triangles:
            self.menu_triangles[option]()
        else:
            print("Invalid option.")
            self.trinagles()

    def quadrilaterals(self):
        print()

        for a,b in self.menu_quadrilaterals.items():
            print(f"{a} : {b.__name__}")

        option = input("Choose an option: ")
        
        if option in self.menu_quadrilaterals:
            self.menu_quadrilaterals[option]()
        else:
            print("Invalid option.")
            self.quadrilaterals()

    def regular_pentagon(self):
        print()
        print("Input the required parameters")

        a = float(input("Side: "))

        pentagon = RegularPentagon(a)

        print("Perimeter: "+ str(pentagon.perimeter()))
        print("Area: "+ str(pentagon.area()))
        pentagon.draw()

    def regular_hexagon(self):
        print()
        print("Input the required parameters")

        a = float(input("Side: "))

        hexagon = RegularHexagon(a)

        print("Perimeter: "+ str(hexagon.perimeter()))
        print("Area: "+ str(hexagon.area()))
        hexagon.draw()

    def regular_octagon(self):
        print()
        print("Input the required parameters")

        a = float(input("Side: "))

        octagon = RegularOctagon(a)

        print("Perimeter: "+ str(octagon.perimeter()))
        print("Area: "+ str(octagon.area()))
        octagon.draw()


    def triangle(self):
        print()
        print("Input the required parameters")

        a = float(input("Side a: "))
        b = float(input("Side b: "))
        c = float(input("Side c: "))

        triangle_check = [a,b,c]
        triangle_check.sort()

        if triangle_check[0] + triangle_check[1] > triangle_check[2]:

            triangle = Triangle(a,b,c)
            print("Perimeter: "+ str(triangle.perimeter()))
            print("Area: "+ str(triangle.area()))
            triangle.draw()

        else:
            print("This is not a triangle!")

        

    def isosceles_triangle(self):
        print()
        print("Input the required parameters")

        a = float(input("Side: "))
        b = float(input("Base: "))

        triangle_check = [a,a,b]
        triangle_check.sort()

        if triangle_check[0] + triangle_check[1] > triangle_check[2]:

            triangle = IsoscelesTriangle(a,b)
            print("Perimeter: "+ str(triangle.perimeter()))
            print("Area: "+ str(triangle.area()))
            triangle.draw()

        else:
            print("This is not a triangle!")

    def equilateral_triangle(self):
        print()
        print("Input the required parameters")

        a = float(input("Side: "))

        triangle = EquilateralTriangle(a)
        print("Perimeter: "+ str(triangle.perimeter()))
        print("Area: "+ str(triangle.area()))
        triangle.draw()


    def quadrilateral(self):
        print()
        print("Input the required parameters")

        e = float(input("Diagonal ac: "))
        f = float(input("Diagonal bd: "))
        angle = float(input("Angle of intersection of diagonals: "))
        AC_ratio = float(input("The ratio in which the diagonal bd intersects the diagonal ac: "))
        BD_ratio = float(input("The ratio in which the diagonal ac intersects the diagonal bd: "))

        quadrilateral = ConvexQuadrilateral(e,f,angle,AC_ratio,BD_ratio)
        print("Perimeter: "+ str(quadrilateral.perimeter()))
        print("Area: "+ str(quadrilateral.area()))
        quadrilateral.draw()

    def parallelogram(self):
        print()
        print("Input the required parameters")

        e = float(input("Diagonal ac: "))
        f = float(input("Diagonal bd: "))
        angle = float(input("Angle of intersection of diagonals: "))

        parallelogram = Parallelogram(e,f,angle)
        print("Perimeter: "+ str(parallelogram.perimeter()))
        print("Area: "+ str(parallelogram.area()))
        parallelogram.draw()

    def kite(self):
        print()
        print("Input the required parameters")

        e = float(input("Diagonal ac: "))
        f = float(input("Diagonal bd: "))

        kite = Kite(e,f)
        print("Perimeter: "+ str(kite.perimeter()))
        print("Area: "+ str(kite.area()))
        kite.draw()

    def rhombus(self):
        print()
        print("Input the required parameters")

        e = float(input("Diagonal ac: "))
        f = float(input("Diagonal bd: "))

        rhombus = Rhombus(e,f)
        print("Perimeter: "+ str(rhombus.perimeter()))
        print("Area: "+ str(rhombus.area()))
        rhombus.draw()

    def square(self):
        print()
        print("Input the required parameters")

        e = float(input("Diagonal: "))

        square = Square(e)
        print("Perimeter: "+ str(square.perimeter()))
        print("Area: "+ str(square.area()))
        square.draw()


    def show(self):
        print()
        for a, b in self.options.items():
            print(f"{a} : {b.__name__}")

    def run(self):
        while True:

            self.show()
            option = input("Choose an option: ")

            if option in self.options:
                self.options[option]()
            else:
                print("Invalid option.")

    def set_color(self):
        print()
        for a, b in self.menu_colors.items():
            print(f"{a} : {b.__name__}")

        option = input("Choose an option: ")
        
        if option in self.menu_colors:
            self.menu_colors[option]()
        else:
            print("Invalid option.")
            self.quadrilaterals()

    def fill_color(self):
        print()

        for color in colors.colors:
            print(color)
        
        option = input("Choose a color: ")

        if option in colors.colors:
            colors.fill_color = option
        else:
            print("Invalid color.")
            self.set_color()

    def outline_color(self):
        print()

        for color in colors.colors:
            print(color)
        
        option = input("Choose a color: ")

        if option in colors.colors:
            colors.outline_color = option
        else:
            print("Invalid color.")
            self.set_color()
        

    def exit_program(self):
        exit()