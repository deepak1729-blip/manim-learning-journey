from manim import *

class firstanimation(Scene):
    def construct(self):
        x1 = Text("Hello there!").shift(UP)
        x2 = Text("Who are you?")
        self.play(Write(x1))
        self.wait(1)
        self.play(Write(x2))