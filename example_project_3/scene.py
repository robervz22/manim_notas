from manim import *

# Colors
class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)

# Maths
class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

# Animations with text
class GeometricShapeWithText(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(color=BLUE, fill_opacity=0.5)
        circle.shift(LEFT * 3)

        # Create a square
        square = Square(color=GREEN, fill_opacity=0.5)
        square.shift(RIGHT * 3)

        # Add some text
        text = Text("Circle and Square").scale(0.8)
        text.move_to(DOWN * 3)

        # Create animations
        self.play(FadeIn(circle), FadeIn(square))
        self.play(circle.animate.shift(RIGHT * 3), square.animate.shift(LEFT * 3))
        self.play(Write(text))

        # Add a rotation
        self.play(Rotate(circle, angle=PI), Rotate(square, angle=-PI))
        
        # Change text to another phrase
        new_text = Text("Shapes in Motion!").scale(0.8)
        new_text.move_to(text.get_center())
        self.play(Transform(text, new_text))

        # Fade out everything
        self.play(FadeOut(circle), FadeOut(square), FadeOut(text))
