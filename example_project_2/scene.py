from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class CircleSquare(Scene):
    def construct(self):
        self.next_section("Circulo")
        circle = Circle().set_fill(PINK, opacity=0.5)
        self.add(circle)
        self.play(FadeOut(circle))  # fade out animation


        # now we wait 1sec and have an animation to satisfy the section
        self.wait(2)
        self.next_section("Cuadrado")
        square = Square().set_fill(BLUE, opacity=0.5)
        self.add(square)
        self.play(FadeOut(square))  # fade out animation