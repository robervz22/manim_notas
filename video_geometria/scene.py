from manim import *

config.background_color = WHITE

class SquareArea(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Área de un cuadrado", font_size=36,color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Draw the square
        square = Square(side_length=3, color=BLUE)
        square_label = MathTex("l").next_to(square, LEFT).set_color(BLACK)
        self.play(Create(square), Write(square_label))
        self.wait(1)

        # Display the formula for area
        formula = Tex(r"$\text{Area}\ =\ l^2$").next_to(square,2*DOWN).set_color(BLACK)
        self.play(Write(formula))
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
        total_area = Tex(r"$\text{Área}=3 \times 3= 9$").next_to(grid,RIGHT).set_color(BLACK)
        self.play(Write(total_area))
        self.wait(2)

        # Fade out and conclude
        self.play(FadeOut(VGroup(square, square_label, formula, grid, annotations, total_area, title)))
        conclusion = Tex(r"Área de un cuadrado de lado $l$ es $l^2$!", font_size=72).move_to(ORIGIN).set_color(BLACK)
        self.play(Write(conclusion))
        self.wait(2)
