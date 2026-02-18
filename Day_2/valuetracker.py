from manim import *

class valuetracker(Scene):
    def construct(self):
        t = ValueTracker(10)

        n1 = always_redraw(lambda:  DecimalNumber(t.get_value(), num_decimal_places=1))

        self.play(Write(n1))
        self.play(t.animate.set_value(30), run_time=4)
        self.wait()