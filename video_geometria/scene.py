from manim import *

config.background_color = WHITE

class SquareArea(Scene):
    """Class that builds a scene to explain the area of square

    Args:
        Scene (_type_): Scene Manim Type
    """
    def construct(self):
        # Title of the scene
        title = Text("Área de un cuadrado", font_size=36,color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Draw the square
        square = Square(side_length=3, color=BLUE)
        square_label = MathTex("l").next_to(square, LEFT).set_color(BLACK)
        square_num_label = Tex(r"$l\ =\ 3$").next_to(square,LEFT).set_color(BLACK)
        self.play(Create(square), Write(square_label))
        self.wait(1)

        # Display the formula for area
        formula = Tex(r"$A = l^2$").next_to(square,2*DOWN).set_color(BLACK)
        formula_num = Tex(r"$A = 3\times 3 = 9$").next_to(square,2*DOWN).set_color(BLACK)
        self.play(Write(formula))
        self.wait(1)

        # Transformations from Algebra to Numeric representation
        self.play(Transform(square_label, square_num_label))
        self.wait(1)

        # Show the inner grid
        grid = VGroup(*[
            Square(side_length=1, color=BLUE, fill_opacity=0.2).move_to(np.array([-2,-2,-2])+square.get_corner(UR)+ RIGHT * i + UP * j)
            for i in range(3) for j in range(3)
        ])
        self.play(FadeIn(grid))
        self.wait(1)

        # Animate the area calculation
        annotations = VGroup(*[
            MathTex(r"\mathbf{1}").scale(0.5).move_to(sq.get_center()).set_color(BLACK) for sq in grid
        ])
        self.play(Write(annotations))
        self.wait(1)

        # Highlight the total area
        #total_area = Tex(r"$A=3 \times 3= 9$").next_to(grid,RIGHT).set_color(BLACK)
        self.play(Transform(formula,formula_num))
        self.wait(2)

        # Fade out and conclude
        self.play(FadeOut(VGroup(square, square_label, square_num_label, formula, formula_num, grid, annotations, title)))
        conclusion = Tex(r"Área de un cuadrado de lado $l$ es $l^2$!", font_size=50).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)

class RectangleArea(Scene):
    """Class that builds a scene to explain the area of a rectangle

    Args:
        Scene (_type_): Scene Manim Type
    """
    def construct(self):
        title = Text("Área de un rectángulo", font_size=36,color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define the rectangle
        length = 4
        width = 3
        rect = Rectangle(width=length, height=width, color=BLUE)
        rect_label = Tex(r"$A = l \times w$").next_to(rect, 2*DOWN).set_color(BLACK)
        
        # Define dimension labels
        length_label = Tex(f"$l = {length}$").next_to(rect, UP).set_color(BLACK)
        length_l = Tex(f"$l$").next_to(rect, UP).set_color(BLACK)
        width_label = Tex(f"$w = {width}$").next_to(rect, LEFT).set_color(BLACK)
        width_w = Tex(f"$w$").next_to(rect, LEFT).set_color(BLACK)
        label_group = VGroup(rect_label,length_label,width_label,length_l,width_w)
        
        # Create a grid within the rectangle
        grid = VGroup()
        for i in range(1, length):
            grid.add(Line(start=rect.get_corner(DL) + RIGHT * i, end=rect.get_corner(UL) + RIGHT * i, color=BLUE))
        for i in range(1, width):
            grid.add(Line(start=rect.get_corner(DL) + UP * i, end=rect.get_corner(DR) + UP * i, color=BLUE))
        
        # Display the rectangle, labels, and grid
        self.play(Create(rect),Write(width_w),Write(length_l))
        self.play(Write(rect_label))
        #self.play(Write(width_w),Write(length_l))
        self.play(Transform(width_w,width_label),Transform(length_l,length_label))
        #self.play(Transform(length_l,length_label))
        self.play(Create(grid))
        
        # Animate filling in the grid cells one by one
        squares = VGroup()
        for i in range(width):
            for j in range(length):
                square = Square(side_length=1,color=BLUE, fill_color=BLUE, fill_opacity=0.5)
                square.move_to(rect.get_corner(DL) + RIGHT * (j + 0.5) + UP * (i + 0.5))
                squares.add(square)
        
        self.play(LaggedStart(*[FadeIn(square) for square in squares], lag_ratio=0.1))

        # Animate the area calculation
        annotations = VGroup(*[
            MathTex(r"\mathbf{1}").scale(0.5).move_to(sq.get_center()).set_color(BLACK) for sq in squares
        ])
        self.play(Write(annotations))
        self.wait(1)
        
        # Show final area calculation
        area_value = Tex(f"$A = {length} \\times {width} = {length * width}$").move_to(rect_label).set_color(BLACK)
        self.play(Transform(rect_label, area_value))
        self.wait(2)

        # Fade out and conclude
        self.play(FadeOut(VGroup(rect, grid, area_value, label_group, squares, annotations, title)))
        conclusion = Tex(r"Área de un rectángulo de largo $l$ y ancho $w$ es $l\times w$!", font_size=50).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)

class ParallelogramToRectangle(Scene):
    """Class that explains the area calculation of a parallelogram

    Args:
        Scene (_type_): Scene Manim Type
    """
    def construct(self):
        title = Text("Área de un paralelogramo", font_size=36,color=BLACK).to_edge(UP).shift(0.5*LEFT)
        self.play(Write(title))
        self.wait(1)

        # Define colors
        parallelogram_color = BLUE
        rectangle_color = BLUE
        triangle_color = RED
        
        # Define vertices of the parallelogram
        A = [-3, -1, 0]  # Bottom-left
        B = [1, -1, 0]   # Bottom-right
        C = [2, 2, 0]    # Top-right
        D = [-2, 2, 0]   # Top-left
        
        
        # Create parallelogram
        parallelogram = Polygon(A, B, C, D, color=parallelogram_color, fill_opacity=0.5)
        parallelogram_label = Tex(r"$A = l \times h$").next_to(parallelogram, 2*DOWN).set_color(BLACK).shift(0.3*LEFT)

        # Define the cutting triangle (right part)
        triangle = Polygon(B, C, [1, 2, 0], color=triangle_color, fill_opacity=0.5)

        # height
        height_line = DashedLine(start= B, end = [1,2,0], color = BLACK)
        height_h = Tex(f"$h$").next_to(height_line, LEFT).set_color(BLACK)

        # Define the final rectangle (after transformation)
        rectangle = Polygon(A, B, [1, 2, 0],[-3,2,0] , color=rectangle_color, fill_opacity=0.5)

        # Label base and height
        length_l = Tex(f"$l$").next_to(parallelogram, UP).set_color(BLACK).shift(RIGHT * 0.3)

        # Show parallelogram
        self.play(Create(parallelogram),Write(length_l))
        self.wait(1)
        self.play(Create(height_line),Write(height_h))
        self.wait(1)
        self.play(Write(parallelogram_label))
        self.wait(1)

        # Slice the triangle from the right side
        self.play(Create(triangle))
        self.wait(1)

        # Move the triangle to the left side to form the rectangle
        self.play(triangle.animate.move_to([-2.5,0.5,0]))
        self.wait(1)
        self.play(height_h.animate.move_to(triangle.get_left()+0.35*LEFT))
        self.wait(1)

        # # Show the final rectangle
        self.play(Transform(parallelogram, rectangle),length_l.animate.move_to(rectangle.get_top()+0.35*UP),FadeOut(height_line))
        self.wait(1)
        self.play(FadeOut(triangle))
        self.wait(2)

        # Display the area formula
        # Fade out and conclude
        labels = VGroup(length_l,height_h)
        self.play(FadeOut(VGroup(parallelogram,parallelogram_label,rectangle, labels, title)))
        self.wait(1)
        conclusion = Tex(r"El área de un paralelogramo se calcula de la misma forma que la de un rectángulo!", font_size=40).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

class TriangleToParallelogram(Scene):
    """Class that relates the triangle's area calculation with a parallelogram

    Args:
        Scene (_type_): Scene Manim Type
    """
    def construct(self):
        title = Text("Área de un triángulo", font_size=36,color=BLACK).shift(LEFT).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define points for the triangle
        A = np.array([-3, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([1, 2, 0])
        D = A+C-B        

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)

        # Create duplicate triangle to form parallelogram
        first_line = DashedLine(start= A, end = D, color = BLUE)
        second_line = DashedLine(start= C, end = D, color = BLUE)
        height_line = DashedLine(start= [1,-1,0], end = C, color = BLACK)

        # Create parallelogram outline
        parallelogram = Polygon(A, B, C, D, color=RED,fill_opacity=0.5)
        
        # Labels
        base_label = Tex(f"$l$").next_to(Line(A, B), DOWN).set_color(BLACK)
        height_label =  Tex(f"$h$").next_to(height_line, LEFT).set_color(BLACK)
        
        # Points to indicate the reflection
        point_B = Dot(B, color=BLACK)
        point_B_label = Tex("B",font_size=30).next_to(point_B, RIGHT).set_color(BLACK)
        point_D = Dot(D, color=BLACK)
        point_D_label = Tex("B'",font_size=30).next_to(point_D, UP).set_color(BLACK)
        diagonal_BD = Line(start=B, end=D,color=BLACK)
                
        # Area explanation
        triangle_label = Tex(r"$A = \frac{l \times h}{2}$").next_to(triangle, 4*DOWN).set_color(BLACK).shift(0.3*LEFT)
        
        # Reflection
        reflected_triangle = Polygon(A,D,C, color=BLUE, fill_opacity=0.5)

        # Display animations
        self.play(Create(triangle),Write(base_label))
        self.wait(1)
        self.play(Create(height_line),Write(height_label))
        self.wait(1)
        self.play(Write(triangle_label))
        self.wait(2)
        self.play(Create(point_B),Write(point_B_label))
        self.play(Create(diagonal_BD),Create(point_D),Write(point_D_label))
        self.wait(1)
        self.play(Create(first_line), Create(second_line))
        self.wait(1)
        triangle_copy = triangle.copy()
        self.play(Transform(triangle_copy,reflected_triangle))
        self.wait(1)
        self.play(Create(parallelogram))
        self.wait(1)

        # Fadeout and conclusion
        labels = VGroup(title,base_label,height_label,triangle_label,point_B_label,point_D_label)
        lines_points  = VGroup(height_line,diagonal_BD,point_B,point_D,first_line,second_line)
        polygons = VGroup(triangle,reflected_triangle,parallelogram,triangle_copy) 
        self.play(FadeOut(labels,lines_points,polygons))
        self.wait(1)
        conclusion = Tex(r"El área de un triángulo es $A = \frac{l \times h}{2}$, la mitad de un paralelogramo!", font_size=40).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))


class GeometryAreas(Scene):
    def construct(self):
        # Run the first scene (Square Area)
        self.play_square_area()
        self.wait(1)

        transition = Tex("Ahora veamos el área de un rectángulo...", font_size=50).set_color(BLACK)
        self.play(Write(transition))
        self.wait(2)
        self.play(FadeOut(transition))

        # Run the second scene (Rectangle Area)
        self.play_rectangle_area()

        self.wait(1)

        transition = Tex("Ahora veamos el área de un paralelogramo...", font_size=50).set_color(BLACK)
        self.play(Write(transition))
        self.wait(2)
        self.play(FadeOut(transition))

        # Run the third scene (Parallelogram Area)
        self.play_parallelogram_area()

        self.wait(1)

        transition = Tex("Y para el área de un triángulo...", font_size=50).set_color(BLACK)
        self.play(Write(transition))
        self.wait(2)
        self.play(FadeOut(transition))

        self.play_triangle_area()

    def play_square_area(self):
        title = Text("Área de un cuadrado", font_size=36, color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        square = Square(side_length=3, color=BLUE)
        square_label = MathTex("l").next_to(square, LEFT).set_color(BLACK)
        square_num_label = Tex(r"$l\ =\ 3$").next_to(square, LEFT).set_color(BLACK)
        self.play(Create(square), Write(square_label))
        self.wait(1)

        formula = Tex(r"$A = l^2$").next_to(square, 2*DOWN).set_color(BLACK)
        formula_num = Tex(r"$A = 3\times 3 = 9$").next_to(square, 2*DOWN).set_color(BLACK)
        self.play(Write(formula))
        self.wait(1)

        self.play(Transform(square_label, square_num_label))
        self.wait(1)

        grid = VGroup(*[
            Square(side_length=1, color=BLUE, fill_opacity=0.2).move_to(np.array([-2, -2, -2]) + square.get_corner(UR) + RIGHT * i + UP * j)
            for i in range(3) for j in range(3)
        ])
        self.play(FadeIn(grid))
        self.wait(1)

        annotations = VGroup(*[
            MathTex(r"\mathbf{1}").scale(0.5).move_to(sq.get_center()).set_color(BLACK) for sq in grid
        ])
        self.play(Write(annotations))
        self.wait(1)

        self.play(Transform(formula, formula_num))
        self.wait(2)

        self.play(FadeOut(VGroup(square, square_label, square_num_label, formula, formula_num, grid, annotations, title)))
        self.wait(1)
        conclusion = Tex(r"Área de un cuadrado de lado $l$ es $l^2$!", font_size=50).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

    def play_rectangle_area(self):
        title = Text("Área de un rectángulo", font_size=36, color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        length = 4
        width = 3
        rect = Rectangle(width=length, height=width, color=BLUE)
        rect_label = Tex(r"$A = l \times w$").next_to(rect, 2*DOWN).set_color(BLACK)
        
        length_label = Tex(f"$l = {length}$").next_to(rect, UP).set_color(BLACK)
        length_l = Tex(f"$l$").next_to(rect, UP).set_color(BLACK)
        width_label = Tex(f"$w = {width}$").next_to(rect, LEFT).set_color(BLACK)
        width_w = Tex(f"$w$").next_to(rect, LEFT).set_color(BLACK)
        label_group = VGroup(rect_label, length_label, width_label, length_l, width_w)
        
        grid = VGroup()
        for i in range(1, length):
            grid.add(Line(start=rect.get_corner(DL) + RIGHT * i, end=rect.get_corner(UL) + RIGHT * i, color=BLUE))
        for i in range(1, width):
            grid.add(Line(start=rect.get_corner(DL) + UP * i, end=rect.get_corner(DR) + UP * i, color=BLUE))

        self.play(Create(rect), Write(width_w), Write(length_l))
        self.play(Write(rect_label))
        self.play(Transform(width_w, width_label), Transform(length_l, length_label))
        self.play(Create(grid))

        squares = VGroup()
        for i in range(width):
            for j in range(length):
                square = Square(side_length=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
                square.move_to(rect.get_corner(DL) + RIGHT * (j + 0.5) + UP * (i + 0.5))
                squares.add(square)
        
        self.play(LaggedStart(*[FadeIn(square) for square in squares], lag_ratio=0.1))

        annotations = VGroup(*[
            MathTex(r"\mathbf{1}").scale(0.5).move_to(sq.get_center()).set_color(BLACK) for sq in squares
        ])
        self.play(Write(annotations))
        self.wait(1)
        
        area_value = Tex(f"$A = {length} \\times {width} = {length * width}$").move_to(rect_label).set_color(BLACK)
        self.play(Transform(rect_label, area_value))
        self.wait(2)

        self.play(FadeOut(VGroup(rect, grid, area_value, label_group, squares, annotations, title, )))
        self.wait(1)
        conclusion = Tex(r"Área de un rectángulo de largo $l$ y ancho $w$ es $l\times w$!", font_size=50).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

    def play_parallelogram_area(self):
        title = Text("Área de un paralelogramo", font_size=36,color=BLACK).to_edge(UP).shift(0.5*LEFT)
        self.play(Write(title))
        self.wait(1)

        # Define colors
        parallelogram_color = BLUE
        rectangle_color = BLUE
        triangle_color = RED
        
        # Define vertices of the parallelogram
        A = [-3, -1, 0]  # Bottom-left
        B = [1, -1, 0]   # Bottom-right
        C = [2, 2, 0]    # Top-right
        D = [-2, 2, 0]   # Top-left
        
        
        # Create parallelogram
        parallelogram = Polygon(A, B, C, D, color=parallelogram_color, fill_opacity=0.5)
        parallelogram_label = Tex(r"$A = l \times h$").next_to(parallelogram, 2*DOWN).set_color(BLACK).shift(0.3*LEFT)

        # Define the cutting triangle (right part)
        triangle = Polygon(B, C, [1, 2, 0], color=triangle_color, fill_opacity=0.5)

        # height
        height_line = DashedLine(start= B, end = [1,2,0], color = BLACK)
        height_h = Tex(f"$h$").next_to(height_line, LEFT).set_color(BLACK)

        # Define the final rectangle (after transformation)
        rectangle = Polygon(A, B, [1, 2, 0],[-3,2,0] , color=rectangle_color, fill_opacity=0.5)

        # Label base and height
        length_l = Tex(f"$l$").next_to(parallelogram, UP).set_color(BLACK).shift(RIGHT * 0.3)

        # Show parallelogram
        self.play(Create(parallelogram),Write(length_l))
        self.wait(1)
        self.play(Create(height_line),Write(height_h))
        self.wait(1)
        self.play(Write(parallelogram_label))
        self.wait(1)

        # Slice the triangle from the right side
        self.play(Create(triangle))
        self.wait(1)

        # Move the triangle to the left side to form the rectangle
        self.play(triangle.animate.move_to([-2.5,0.5,0]))
        self.wait(1)
        self.play(height_h.animate.move_to(triangle.get_left()+0.35*LEFT))
        self.wait(1)

        # # Show the final rectangle
        self.play(Transform(parallelogram, rectangle),length_l.animate.move_to(rectangle.get_top()+0.35*UP),FadeOut(height_line))
        self.wait(1)
        self.play(FadeOut(triangle))
        self.wait(2)

        # Display the area formula
        # Fade out and conclude
        labels = VGroup(length_l,height_h)
        self.play(FadeOut(VGroup(parallelogram,parallelogram_label,rectangle, labels, title)))
        self.wait(1)
        conclusion = Tex(r"El área de un paralelogramo se calcula de la misma forma que la de un rectángulo!", font_size=40).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

    def play_triangle_area(self):
        title = Text("Área de un triángulo", font_size=36,color=BLACK).shift(LEFT).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define points for the triangle
        A = np.array([-3, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([1, 2, 0])
        D = A+C-B        

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)

        # Create duplicate triangle to form parallelogram
        first_line = DashedLine(start= A, end = D, color = BLUE)
        second_line = DashedLine(start= C, end = D, color = BLUE)
        height_line = DashedLine(start= [1,-1,0], end = C, color = BLACK)

        # Create parallelogram outline
        parallelogram = Polygon(A, B, C, D, color=RED,fill_opacity=0.5)
        
        # Labels
        base_label = Tex(f"$l$").next_to(Line(A, B), DOWN).set_color(BLACK)
        height_label =  Tex(f"$h$").next_to(height_line, LEFT).set_color(BLACK)
        
        # Points to indicate the reflection
        point_B = Dot(B, color=BLACK)
        point_B_label = Tex("B",font_size=30).next_to(point_B, RIGHT).set_color(BLACK)
        point_D = Dot(D, color=BLACK)
        point_D_label = Tex("B'",font_size=30).next_to(point_D, UP).set_color(BLACK)
        diagonal_BD = Line(start=B, end=D,color=BLACK)
                
        # Area explanation
        triangle_label = Tex(r"$A = \frac{l \times h}{2}$").next_to(triangle, 4*DOWN).set_color(BLACK).shift(0.3*LEFT)
        
        # Reflection
        reflected_triangle = Polygon(A,D,C, color=BLUE, fill_opacity=0.5)

        # Display animations
        self.play(Create(triangle),Write(base_label))
        self.wait(1)
        self.play(Create(height_line),Write(height_label))
        self.wait(1)
        self.play(Write(triangle_label))
        self.wait(2)
        self.play(Create(point_B),Write(point_B_label))
        self.play(Create(diagonal_BD),Create(point_D),Write(point_D_label))
        self.wait(1)
        self.play(Create(first_line), Create(second_line))
        self.wait(1)
        triangle_copy = triangle.copy()
        self.play(Transform(triangle_copy,reflected_triangle))
        self.wait(1)
        self.play(Create(parallelogram))
        self.wait(2)

        # Fadeout and conclusion
        labels = VGroup(title,base_label,height_label,triangle_label,point_B_label,point_D_label)
        lines_points  = VGroup(height_line,diagonal_BD,point_B,point_D,first_line,second_line)
        polygons = VGroup(triangle,reflected_triangle,parallelogram,triangle_copy) 
        self.play(FadeOut(labels,lines_points,polygons))
        self.wait(1)
        conclusion = Tex(r"El área de un triángulo es $A = \frac{l \times h}{2}$, la mitad de un paralelogramo!", font_size=40).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))