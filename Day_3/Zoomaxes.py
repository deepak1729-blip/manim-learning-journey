from manim import *
import numpy as np

class Zoomaxes(Scene):
    def construct(self):

        x=ValueTracker(7)
        y=ValueTracker(3)

        axes = always_redraw(lambda:Axes(x_range=(-8,8),
                    y_range=(-1,1),
                    x_length=x.get_value(),
                    y_length=y.get_value(),
                    tips=False).add_coordinates())
        
        self.play(Write(axes))

        Sinecurve= always_redraw(lambda: axes.plot(lambda x: np.sin(x), color=BLUE))

        self.play(Write(Sinecurve))
        self.play(x.animate.set_value(50))
        self.play(y.animate.set_value(7.5))

        yeqx= axes.plot(lambda x: x, x_range=[-1.5, 1.5], color=RED)

        self.play(Write(yeqx))

        text = Text("Near x=0, sin(x) ≈ x", font_size=24).to_corner(DR, buff=0.5)
        self.play(Write(text))

        self.wait()