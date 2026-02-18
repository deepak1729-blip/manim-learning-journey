from manim import *

class finalanimation(Scene):
    def construct(self):
        c= Circle(radius=0.1,stroke_width=6,color=RED)
        c.set_fill(WHITE, opacity=1)
        r= SurroundingRectangle(c,corner_radius=0.1,color=RED)

        g1=VGroup(c,r)

        t=Tex("Hello ","there")
        t[0].set_color(LIGHT_BROWN)
        t[1].set_color(BLUE)

        g2=VGroup(g1,t)
        g2.arrange()

        width = t[1].width
        
        square = Square(side_length=width+0.1, color=WHITE)
        square.move_to(t[1])

        g3 = VGroup(t[1], square)

        self.play(SpinInFromNothing(c),SpinInFromNothing(r))
        self.play(Write(t[0]))
        self.play(Write(t[1]))
        self.play(Write(square), run_time=1.5)

        self.play(g1.animate.next_to(t[0], UP),g3.animate.next_to(t[0], DOWN))

        self.play(square.animate.scale(3).move_to(ORIGIN),g2.animate.move_to(ORIGIN),t[1].animate.move_to(ORIGIN).shift(DOWN*0.3))

        dot=Dot(color=WHITE).scale(0.5)
        g4=VGroup(c,r,t,square)
        self.play(Transform(g4,dot))
        self.play(dot.animate.scale(300))
        self.play(dot.animate.set_color(BLACK))
        self.wait()
