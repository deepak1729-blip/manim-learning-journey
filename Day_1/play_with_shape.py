from manim import *

class textplay(Scene):
    def construct(self):
        c = Circle(radius=0.5,
                   color= RED,
                   stroke_width= 10,
                   fill_opacity=0.3)
       
        r=SurroundingRectangle(c,color=BLUE,buff=SMALL_BUFF,corner_radius=0.2)
        t=Text("Animation").next_to(r, UP, buff=0.5)
        
        self.play(DrawBorderThenFill(c),Write(r))
        self.play(Write(t), run_time=2)
        self.wait()

        cr = VGroup(c,r)

        self.play(t.animate.move_to([-4,0,0]),cr.animate.move_to([4,0,0]))

        arrow = always_redraw(lambda: 
                              Line(start= cr.get_left(),
                                   end=t.get_right(),
                                   buff=0.4).add_tip(at_start=True,tip_shape=StealthTip).add_tip(tip_shape=StealthTip))
        self.play(Write(arrow))

        self.play(Indicate(t, 1.5, color= ORANGE))
        self.play(Rotate(r, angle= PI/2), ScaleInPlace(c,2))
        self.play(cr.animate.move_to([0,0,0]))

        self.play(FadeOut(arrow),FadeOut(t),run_time=0.5)
        self.play(ShrinkToCenter(r),ScaleInPlace(c,10),run_time=2)
        self.wait()