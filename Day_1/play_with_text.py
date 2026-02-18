from manim import *

class textplay(Scene):
    def construct(self):
        x = Text("Hello There!", color=GRAY_BROWN, weight=BOLD, font_size=48)
        self.play(Write(x))
        self.wait(2)
        self.play(Unwrite(x))
        self.wait(2)