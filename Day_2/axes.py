from manim import *

class axesfunc(Scene):
    def construct(self):
        axes = Axes(x_range=(-8,8),
                    y_range=(0,16),
                    x_length=12,
                    y_length=6,
                    tips=False).add_coordinates()
        
        x_lab = axes.get_x_axis_label("x")
        y_lab = axes.get_y_axis_label("y")

        n = ValueTracker(1)

        self.play(Write(axes),Write(x_lab),Write(y_lab))
        
        curve = always_redraw(lambda: axes.plot(lambda x: n.get_value()*x*x,color=BLUE))
        
        self.add(curve)
        
        # Overlay rectangles to hide parts outside axes
        cover_top = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=config.background_color,
            fill_opacity=1,
            stroke_width=0).next_to(axes, UP, buff=0)
        
        cover_left = Rectangle(
            width=config.frame_width/2,
            height=config.frame_height,
            fill_color=config.background_color,
            fill_opacity=1,
            stroke_width=0).next_to(axes, LEFT, buff=0)
        
        cover_right = Rectangle(
            width=config.frame_width/2,
            height=config.frame_height,
            fill_color=config.background_color,
            fill_opacity=1,
            stroke_width=0).next_to(axes, RIGHT, buff=0)
        
        cover_bottom = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=config.background_color,
            fill_opacity=1,
            stroke_width=0).next_to(axes, DOWN, buff=0)
        
        self.add(cover_top, cover_left, cover_right, cover_bottom)
        
        # Bring axes and labels to front
        self.bring_to_front(axes, x_lab, y_lab)
        
        self.play(Create(curve), run_time=2)

        self.play(n.animate.set_value(2), run_time=2)
        self.play(n.animate.set_value(0.1), run_time=2)
        
        self.wait()
