from manim import *
from manim_editor import PresentationSectionType

class FTExplanation(Scene):
    def construct(self):
        
        title_right = Tex("triangulation", font_size=100).move_to(RIGHT*2)
        title_left = Tex("Fine", font_size=100, color=PURE_GREEN).next_to(title_right, LEFT, buff=2*SMALL_BUFF)
        # the texts have slightly different heights, so we have to align them
        title_left.shift(UP*0.1)
        title = VGroup(title_left, title_right)
        t0 = Tex("A triangulation is fine if all points are vertices of some simplex", font_size=40).to_corner(DL)
        t2 = Tex("Fineness of the triangulation ensures a smooth Calabi-Yau threefold", font_size=40).to_corner(DL)
        
        axes = Axes(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            x_length=6,
            y_length=6,
            tips=False,
        )
        
        vert = [[-2,-1], [1,-1], [1,2]]
        points = [[0,0],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-2,-1],[-1,0],[0,1]]
        
        poly = Polygon(*[axes.coords_to_point(*pt) for pt in vert], color=PURE_RED)
        poly.set_z_index(10)
        
        dots = [Dot(point=axes.coords_to_point(*pt), color=TEAL) for pt in points]
        for d in dots:
            d.set_z_index(20)
        
        simplices = [[9, 8, 0], [6, 8, 7], [2, 9, 1], [3, 5, 0], [3, 5, 4], [6, 5, 0], [6, 8, 0], [2, 3, 0], [2, 9, 0]]
        special_lines = [{0,2},{2,9}]
        lines = []
        for s in simplices:
            for i,j in [[0,1],[0,2],[1,2]]:
                if {s[i],s[j]} in special_lines:
                    continue
                lines.append(Line(start=axes.coords_to_point(*points[s[i]]), end=axes.coords_to_point(*points[s[j]]), color=PURE_RED))
                lines[-1].set_z_index(10)
        for s in special_lines:
            i,j = tuple(sorted(s))
            lines.append(Line(start=axes.coords_to_point(*points[i]), end=axes.coords_to_point(*points[j]), color=PURE_RED))
            lines[-1].set_z_index(10)
        new_line = Line(start=axes.coords_to_point(*points[9]), end=axes.coords_to_point(*points[3]), color=PURE_RED)
        new_line.set_z_index(10)
        
        t1 = Tex("Fine:", font_size=50).shift(UP*2+RIGHT*4)
        yes = Tex("yes", font_size=50, color=PURE_GREEN).next_to(t1, RIGHT).shift(DOWN*0.1)
        yes_cp = yes.copy()
        no = Tex("no", font_size=50, color=PURE_RED).next_to(t1, RIGHT).shift(DOWN*0.05)
        
        self.next_section("FTExplanation 0", PresentationSectionType.NORMAL)
        self.add(title_right)
        self.play(FadeIn(title_left))
        self.next_section("FTExplanation 1", PresentationSectionType.NORMAL)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.play(AnimationGroup(*[FadeIn(pt) for pt in dots], lag_ratio=0.05))
        self.play(Create(poly))
        self.play(AnimationGroup(*[Create(line) for line in lines], lag_ratio=0.05))
        self.next_section("FTExplanation 2", PresentationSectionType.NORMAL)
        self.play(Write(t0))
        self.play(Write(t1), Write(yes_cp))
        self.next_section("FTExplanation 3", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(lines[-2], new_line))
        self.next_section("FTExplanation 4", PresentationSectionType.NORMAL)
        self.play(FadeOut(lines[-1]), dots[2].animate.set_color(PURE_RED), ReplacementTransform(yes_cp, no))
        self.next_section("FTExplanation 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(lines[-1]), dots[2].animate.set_color(TEAL), ReplacementTransform(no, yes))
        self.next_section("FTExplanation 6", PresentationSectionType.NORMAL)
        self.play(FadeOut(t0), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.next_section("FTExplanation 7", PresentationSectionType.SKIP)
        self.play(*[FadeOut(d) for d in dots], *[FadeOut(l_f) for l_f in lines], Unwrite(t2), Unwrite(t1), Unwrite(yes),
                  FadeOut(poly), FadeOut(new_line))
        self.play(FadeOut(title_left), title_right.animate.scale(2).move_to(RIGHT*2))