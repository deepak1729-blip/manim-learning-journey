from manim import *

class textplay(Scene):
    def construct(self):
        self.add(NumberPlane())
        x = Text("Hello There!", color=GRAY_BROWN, weight=BOLD, font_size=48)
        self.play(Write(x))
        self.wait(2)
        self.play(Unwrite(x))
        self.wait(2)

        s = Square(side_length=2).shift(RIGHT)
        self.play(Write(s))
        self.wait(3)