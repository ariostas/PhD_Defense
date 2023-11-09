from manim import *
from manim_editor import PresentationSectionType

class RTExplanation(ThreeDScene):
    def construct(self):
        
        title_right = Tex("triangulation", font_size=100).move_to(RIGHT*2)
        title_left = Tex("Regular", font_size=100, color=PURE_RED).next_to(title_right, LEFT, buff=2*SMALL_BUFF)
        title = VGroup(title_left, title_right)
        t0 = Tex("A triangulation is regular if it can be constructed as follows", font_size=40).to_corner(DL)
        t1 = Tex("Embed into $d+1$ dimensions", font_size=40).to_corner(DL)
        t2 = Tex("Lift points by heights $h_i$", font_size=40).to_corner(DL)
        t3 = Tex("Construct convex hull", font_size=40).to_corner(DL)
        t4 = Tex("Project back into starting space", font_size=40).to_corner(DL)
        t5 = Tex(r"Regularity of the triangulation ensures that the toric variety is K\"ahler", font_size=40).to_corner(DL)
        # This is a trick to fix them in frame without having them appear right away
        self.add_fixed_in_frame_mobjects(title, t0, t1, t2, t3, t4, t5)
        self.remove(title, t0, t1, t2, t3, t4, t5)
        
        axes = ThreeDAxes(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            z_range=(-3, 3, 1),
            tips=False,
        )
        
        vert = [[-2,-1], [1,-1], [1,2]]
        points = [[0,0],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-2,-1],[-1,0],[0,1]]
        heights = [0.6, 2.131370849898476, 1.4, 1.0, 1.4, 1.0, 1.4, 2.131370849898476, 1.0, 1.0]
        
        poly = Polygon(*[axes.coords_to_point(*(pt+[0])) for pt in vert], color=PURE_RED, shade_in_3d=True)
        
        dots = [Dot3D(point=axes.coords_to_point(*(pt+[0])), color=TEAL) for pt in points]
        for d in dots:
            d.set_z_index(20)

        self.set_camera_orientation(zoom=0.5)
        
        simplices = [[9, 8, 0], [6, 8, 7], [2, 9, 1], [3, 5, 0], [3, 5, 4], [6, 5, 0], [6, 8, 0], [2, 3, 0], [2, 9, 0]]
        lines_lifted = []
        lines_flat = []
        for s in simplices:
            lines_lifted.extend([
                Line3D(start=axes.coords_to_point(*points[s[0]],heights[s[0]]), end=axes.coords_to_point(*points[s[1]],heights[s[1]]), color=PURE_RED),
                Line3D(start=axes.coords_to_point(*points[s[0]],heights[s[0]]), end=axes.coords_to_point(*points[s[2]],heights[s[2]]), color=PURE_RED),
                Line3D(start=axes.coords_to_point(*points[s[1]],heights[s[1]]), end=axes.coords_to_point(*points[s[2]],heights[s[2]]), color=PURE_RED),
            ])
            lines_flat.extend([
                Line3D(start=axes.coords_to_point(*points[s[0]],0), end=axes.coords_to_point(*points[s[1]],0), color=PURE_RED),
                Line3D(start=axes.coords_to_point(*points[s[0]],0), end=axes.coords_to_point(*points[s[2]],0), color=PURE_RED),
                Line3D(start=axes.coords_to_point(*points[s[1]],0), end=axes.coords_to_point(*points[s[2]],0), color=PURE_RED),
            ])
            
        for l in lines_lifted+lines_flat:
            d.set_z_index(10)
        
        self.next_section("RTExplanation 0", PresentationSectionType.NORMAL)
        self.play(Write(title_right))
        self.play(FadeIn(title_left))
        self.next_section("RTExplanation 1", PresentationSectionType.NORMAL)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.play(AnimationGroup(*[FadeIn(pt) for pt in dots], lag_ratio=0.05))
        self.play(Create(poly))
        self.next_section("RTExplanation 2", PresentationSectionType.NORMAL)
        self.play(Write(t0))
        self.next_section("RTExplanation 3", PresentationSectionType.NORMAL)
        self.play(Unwrite(t0), run_time=0.5)
        self.play(Write(t1), run_time=0.5)
        self.wait()
        self.play(Create(axes))
        self.wait()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait()
        self.next_section("RTExplanation 4", PresentationSectionType.NORMAL)
        self.play(Unwrite(t1), run_time=0.5)
        self.play(Write(t2), run_time=0.5)
        self.wait()
        self.play(*[dot.animate.move_to(axes.coords_to_point(*pt,h)) for dot,pt,h in zip(dots, points, heights)])
        self.wait()
        self.next_section("RTExplanation 5", PresentationSectionType.NORMAL)
        self.play(Unwrite(t2), run_time=0.5)
        self.play(Write(t3), run_time=0.5)
        self.wait(0.5)
        self.play(AnimationGroup(*[Create(line) for line in lines_lifted], lag_ratio=0.05), run_time=1.5)
        self.wait()
        self.next_section("RTExplanation 6", PresentationSectionType.NORMAL)
        self.play(Unwrite(t3), run_time=0.5)
        self.play(Write(t4), run_time=0.5)
        self.play(*[dot.animate.move_to(axes.coords_to_point(*pt,0)) for dot,pt in zip(dots, points)],
                  *[ReplacementTransform(l_l, l_f) for l_l,l_f in zip(lines_lifted, lines_flat)])
        self.play(FadeOut(poly))
        self.wait()
        self.next_section("RTExplanation 7", PresentationSectionType.NORMAL)
        self.play(Unwrite(t4))
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0*DEGREES, theta=270*DEGREES, zoom=0.5, run_time=1.5)
        self.play(Uncreate(axes))
        self.wait()
        self.play(FadeIn(t5))
        self.next_section("RTExplanation 8", PresentationSectionType.SKIP)
        self.play(*[FadeOut(d) for d in dots], *[FadeOut(l_f) for l_f in lines_flat], FadeOut(t5))
        self.play(FadeOut(title_left), title_right.animate.scale(2).move_to(RIGHT*2))