class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
    
    def get_x(self) -> int:
        return self._x
    
    def set_x(self, x: int) -> None:
        self._x = x
    
    def get_y(self) -> int:
        return self._y
    
    def set_y(self, y: int) -> None:
        self._y = y
    
    def compute_distance(self, other_point: "Point") -> float: 
        x_distance = self._x - other_point.get_x()
        y_distance = self._y - other_point.get_y()
        return (x_distance**2 + y_distance**2)* 0.5
    
class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)
    
    def get_start_point(self) -> Point:
        return self._start_point
    
    def set_start_point(self, start_point: Point) -> None:
        self._start_point = start_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_end_point(self) -> Point:
        return self._end_point
    
    def set_end_point(self, end_point: Point) -> None:
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_length(self) -> float:
        return self._length
  

class Shape:
    def __init__(self, is_regular: bool, vertices: list["Point"], 
                 edges: list["Line"], inner_angles: list[float]) -> None:
        self._is_regular = is_regular         
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
        
    def get_is_regular(self) -> bool:
        return self._is_regular
    
    def set_is_regular(self, is_regular: bool) -> None:
        self._is_regular = is_regular
        
    def get_vertices(self):
        return self._vertices
    
    def set_vertices(self, vertices: list["Point"]):
        self._vertices = vertices

    def get_edges(self):
        return self._edges
    
    def set_edges(self, edges: list["Line"]):
        self._edges = edges

    def get_inner_angles(self):
        return self._inner_angles
    
    def set_inner_angles(self, inner_angles: list[float]):
        self._inner_angles = inner_angles
    

    def compute_area(self): 
        pass #El área se calcula según la figura 

    def compute_perimeter(self):
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.get_length()
        return perimeter

    def compute_inner_angles(self):
        total_angles = 0
        for angle in self._inner_angles: 
            total_angles += angle
        return total_angles

class Rectangle(Shape):
    def __init__(self, vertices: list["Point"], edges: list["Line"]) -> None:
        angles = [90.0, 90.0, 90.0, 90.0]
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=angles)
        self._width = edges[0].get_length()
        self._height = edges[1].get_length()
            
    def get_width(self) -> float:
        return self._width
    
    def set_width(self, width: float) -> None:
        if width <= 0:
            raise ValueError("El ancho debe ser positivo")
        self._width = width
    
    def get_height(self) -> float:
        return self._height
    
    def set_height(self, height: float) -> None:
        if height <= 0:
            raise ValueError("La altura debe ser positiva")
        self._height = height
    
    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)
    
    def compute_angles(self):
        return 360
    
    def diagonal_length(self) -> float:
        return (self._width*2 + self._height*2) **0.5

class Square(Rectangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"]) -> None:
        super().__init__(vertices, edges)
        self._side = edges[0].get_length()

    def get_side(self) -> float:
        return self._side

    def set_side(self, side: float) -> None:
        if side <= 0:
            raise ValueError("El lado debe ser positivo")
        self._side = side

    def compute_area(self) -> float:
        return self._side**2

    def compute_perimeter(self) -> float:
        return 4 * self._side

    def compute_angles(self) -> float:
        return 360

    

class Triangle(Shape): 
    def __init__(self, is_regular: bool, vertices: list["Point"], 
                 edges: list["Line"], inner_angles: list[float]) -> None:
        super().__init__(is_regular, vertices, edges, inner_angles)    
        self._side1 = edges[0].get_length()
        self._side2 = edges[1].get_length()
        self._side3 = edges[2].get_length()
        self._angle1 = inner_angles[0]
        self._angle2 = inner_angles[1]
        self._angle3 = inner_angles[2]
        
    def get_side1(self) -> float:
        return self._side1
    
    def set_side1(self, _side1: float) -> None:
        if _side1 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side1 = _side1

    def get_side2(self) -> float:
        return self._side2
    
    def set_side2(self, _side2: float) -> None:
        if _side2 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side2 = _side2
        
    def get_side3(self) -> float:
        return self._side3
    
    def set_side3(self, _side3: float) -> None:
        if _side3 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side3 = _side3
    
    def get_angle1(self) -> float:
        return self._angle1

    def set_angle1(self, _angle1: float) -> None:
        if _angle1 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle1 = _angle1
        
    def get_angle2(self) -> float:
        return self._angle2

    def set_angle2(self, _angle2: float) -> None:
        if _angle2 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle2 = _angle2
    
    def get_angle3(self) -> float:
        return self._angle3
    
    def set_angle3(self, _angle3: float) -> None:
        if _angle3 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle3 = _angle3

    """Usamos la fórmula de Herón para calcular el área, ya que es aplicable a 
    cualquier triángulo"""
    def compute_area(self) -> float:
        #sp es el semiperímetro, lo coloqué así para que no ocupase tanto espacio
        sp = (self._side1 + self._side2 + self._side3) / 2
        return (sp * (sp - self._side1) * (sp - self._side2) * 
                (sp - self._side3)) ** 0.5

    def compute_perimeter(self) -> float: 
        return self._side1 + self._side2 + self._side3
    
    def compute_angles(self) -> float:
        return self._angle1 + self._angle2 + self._angle3 


    def is_acute(self) -> bool:
        return self._angle1 < 90 and self._angle2 < 90 and self._angle3 < 90
    
    def is_obtuse(self) -> bool:
        """Un ángulo > 90°"""
        return self._angle1 > 90 or self._angle2 > 90 or self._angle3 > 90
    
    def is_right(self) -> bool:
        return self._angle1 == 90 or self._angle2 == 90 or self._angle3 == 90
    
    #Decimos que tipo de triángulo es según sus ángulos
    def angles_type(self) -> str:
        if self.is_right():
            return "Triangle Rectangle"
        elif self.is_obtuse():
            return "Triangle Obtuse"
        else:
            return "Triangle Acute"




class Isoceles(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"], 
                 inner_angles: list[float]) -> None:
        super().__init__(is_regular=False, vertices=vertices, edges=edges, 
                         inner_angles=inner_angles)
        
    def equal_sides(self) -> float:
        side1 = self.get_side1()
        side2 = self.get_side2()
        side3 = self.get_side3()
        if side1 == side2 or side1 == side3:
            return side1
        else:
            return side2

    def compute_area(self) -> float:
        side1 = self.get_side1()
        side2 = self.get_side2()
        side3 = self.get_side3()

        if side1 == side2:
            equal_side = side1
            base = side3
        elif side1 == side3:
            equal_side = side1
            base = side2
        else:
            equal_side = side2
            base = side1

        return (base / 4) * ((4 * equal_side**2 - base**2) ** 0.5)



class Equilateral(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"]) -> None:
        side = edges[0].get_length()
        angles = [60.0, 60.0, 60.0]
        super().__init__(is_regular = True, vertices = vertices, edges = edges,
                         inner_angles = angles)
        self.set_side1(side)
        self.set_side2(side)
        self.set_side3(side) 
    
    def height(self) -> float:
        #Altura del triángulo equilátero: (√3/2) * lado
        self._height = (((3)**0.5) / 2) * self.get_side1()
        return self._height
        
    def compute_area(self):
        #Usamos la fórmula específica para triángulos equiláteros
        #Base * altura / 2
        return self.height() * self.get_side1() / 2


class Scalene(Triangle): 
    def __init__(self, vertices: list["Point"], edges: list["Line"], inner_angles
                 : list[float]) -> None:
        super().__init__(is_regular = False, vertices = vertices, edges = edges
                         , inner_angles = inner_angles)
        self.set_side1(edges[0].get_length())
        self.set_side2(edges[1].get_length())
        self.set_side3(edges[2].get_length())

    """Usamos la fórmula de Herón para calcular el área, ya que es aplicable a 
    cualquier triángulo"""
    def compute_area(self):
        #sp es el semiperímetro, lo coloqué así para que no ocupase tanto espacio
        sp = (self.get_side1() + self.get_side2() + self.get_side3()) / 2
        return (sp * (sp - self.get_side1()) * (sp - self.get_side2()) * 
                (sp - self.get_side3())) ** 0.5

class TriRectangle(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"], inner_angles: list[float]) -> None:
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=inner_angles)

    def compute_area(self) -> float:
        sides = sorted([self.get_side1(), self.get_side2(), self.get_side3()])
        return (sides[0] * sides[1]) / 2

    def hypotenuse(self) -> float:
        return max(self.get_side1(), self.get_side2(), self.get_side3())






