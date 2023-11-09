from manim import *
from manim_editor import PresentationSectionType

class Compactifications1(ThreeDScene):
    def construct(self):
        
        title = Title(r"How do we deal with a 10D spacetime?", font_size=45)
        
        t1 =  Tex("Answer: make some dimensions compact and small.", font_size=40).to_edge(DOWN, buff=1).to_edge(LEFT, buff=1)
        
        def func(u, v):
            return np.array([0.1*np.cos(v),  u, 0.1*np.sin(v)])

        axes = ThreeDAxes()
        surface1 = Surface(
            lambda u, v: axes.c2p(*func(u, v)),
            u_range=[-15, 0],
            v_range=[0, TAU],
            resolution=15,
            checkerboard_colors=None,
            fill_opacity=0.75,
        )
        surface2 = Surface(
            lambda u, v: axes.c2p(*func(u, v)),
            u_range=[0, 15],
            v_range=[0, TAU],
            resolution=15,
            checkerboard_colors=None,
            fill_opacity=0.75,
        )
        self.add_fixed_in_frame_mobjects(title, t1)
        self.remove(title, t1)
        self.set_camera_orientation(theta=0 * DEGREES, phi=75 * DEGREES, zoom=0.5)
        
        circle = ParametricFunction(lambda t: axes.coords_to_point(*func(0, t)), t_range = np.array([0, TAU]), fill_opacity=0).set_color(PURE_RED)
        dot = Dot3D(point=axes.coords_to_point(*func(0,0)), color=YELLOW, radius=0.01)
        
        self.next_section("Compactifications 1-0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("Compactifications 1-1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("Compactifications 1-2", PresentationSectionType.NORMAL)
        self.play(Create(surface1), run_time=0.5)
        self.play(Create(surface2), run_time=0.5)
        self.next_section("Compactifications 1-3", PresentationSectionType.NORMAL)
        self.play(FadeOut(surface2))
        self.move_camera(theta=80 * DEGREES, phi=89 * DEGREES, zoom=15, run_time=2)
        self.next_section("Compactifications 1-4", PresentationSectionType.SKIP)
        self.play(Create(circle))
        self.play(Create(dot))
        self.next_section("Compactifications 1-5", PresentationSectionType.COMPLETE_LOOP)
        self.play(MoveAlongPath(dot, circle), rate_func=linear, run_time=2)
        self.next_section("Compactifications 1-6", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [dot, circle, surface1]])
        self.play(t1.animate.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1))
        