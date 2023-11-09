from manim import *
from manim_editor import PresentationSectionType

class TitleSlide(ThreeDScene):
    def worldsheet_func(self, u, v):
        return np.array([u, v, 0.3*np.cos(2*u)*np.sin(3*v)+0.1*np.sin(2*u)*np.cos(3*v)+0.05*np.sin(2*v)*np.sin(2*u)])

    def construct(self):
        
        title = Tex(r"Computational Advancements in\\String Phenomenology", font_size=50).shift(DOWN*0.5)
        author = Tex("Andres Rios-Tascon", font_size=40).next_to(title, DOWN, buff=0.6)
        info = Tex("Doctoral Thesis Defense. March 30th, 2023", font_size=30).next_to(author, DOWN, buff=0.6)
        
        cornell_seal = ImageMobject("./images/cornell_seal.png").scale_to_fit_height(1.5).to_edge(DOWN, buff=1.7).to_edge(RIGHT, buff=1.4)
        self.add_fixed_in_frame_mobjects(title, author, info, cornell_seal)
        
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(*self.worldsheet_func(u, v)),
            u_range=[-5, 8],
            v_range=[2, 8],
            resolution=20,
            fill_opacity=0.3,
            stroke_width=1,
            fill_color=BLUE,
            checkerboard_colors=None,
        ).set_z_index(5)
        self.t_elapsed = 0
        def move_string(mobj, dt):
            self.t_elapsed += dt*13/6
            new_string = ParametricFunction(lambda t: axes.c2p(*(self.worldsheet_func(self.t_elapsed-5, t))), t_range = np.array([2, 8]), fill_opacity=0, shade_in_3d=True).set_color(PURE_RED)
            mobj.become(new_string)
        self.set_camera_orientation(theta=-100 * DEGREES, phi=75 * DEGREES, zoom=2)
        string = ParametricFunction(lambda t: axes.c2p(*(self.worldsheet_func(-5, t))), t_range = np.array([2, 8]), fill_opacity=0, shade_in_3d=True).set_color(PURE_RED)
        string.add_updater(move_string)
        self.add(surface, string)
        self.next_section("Title 0", PresentationSectionType.COMPLETE_LOOP)
        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=-0.01)
        self.t_elapsed = 0
        self.wait(6)
        self.next_section("Title 1", PresentationSectionType.SKIP)
        self.remove(string)
        self.play(FadeOut(title), FadeOut(info), FadeOut(author), FadeOut(cornell_seal), FadeOut(string), Uncreate(surface))