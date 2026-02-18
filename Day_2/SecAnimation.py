from manim import *

class SecAnimation(Scene):
    def construct(self):
        
        t = Tex("Hello ", "There ", r"\textbf{Y}", r"\textbf{O}", r"\textbf{U}")
        t[2:].set_color("#BD0000")
        t[0:].scale(1.5)

        self.play(Write(t[0:2]), run_time=1.5)
        self.wait()
        self.play(DrawBorderThenFill(t[2:], stroke_width=2, run_time=2, rate_func=linear))

        self.play(t[0].animate.to_edge(UL), t[1].animate.to_edge(UR), t[2:].animate.move_to([0,0,0]))
        self.wait()

        self.play(t[2].animate.move_to([0,2.5,0]), t[4].animate.move_to([0,-2.5,0]))
        self.wait()

        r = Rectangle(height = 1.25, width=1.25).move_to([0,2.5,0])
        c = Circle(radius=0.75)
        p = RegularPolygon(5).move_to([0,-2.5,0]).scale(0.75)

        self.play(SpinInFromNothing(r),Write(c),SpinInFromNothing(p))
        self.wait()

        rp = VGroup(r,p)
        self.play(Rotate(rp,angle=3*PI))

        self.play(Swap(p,r))

        text = Text("BYE BYE").scale(1.5)
        group = VGroup(t, r, c,p)

        self.play(Transform(group,text), run_time=2)