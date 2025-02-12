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

class GeometryAreas(Scene):
    def construct(self):
        # Run the first scene (Square Area)
        self.play_square_area()
        
        # Add a transition (optional)
        self.wait(1)
        transition = Text("Ahora veamos el área de un rectángulo...", font_size=36, color=BLACK)
        self.play(Write(transition))
        self.wait(2)
        self.play(FadeOut(transition))

        # Run the second scene (Rectangle Area)
        self.play_rectangle_area()

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

        self.play(FadeOut(VGroup(rect, grid, area_value, label_group, squares, annotations, title)))
        conclusion = Tex(r"Área de un rectángulo de largo $l$ y ancho $w$ es $l\times w$!", font_size=50).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
