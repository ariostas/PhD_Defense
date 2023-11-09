from manim import *
from manim_editor import PresentationSectionType

class STExplanation(Scene):
    def construct(self):
        
        title_right = Tex("triangulation", font_size=100).move_to(RIGHT*2)
        title_left = Tex("Star", font_size=100, color=TEAL).next_to(title_right, LEFT, buff=2*SMALL_BUFF)
        # the texts have slightly different heights, so we have to align them
        title_left.shift(UP*0.1)
        title = VGroup(title_left, title_right)
        t0 = Tex("A triangulation is star if the origin is a vertex of all simplices", font_size=40).to_corner(DL)
        t2 = Tex("Fineness of a triangulation allows us to interpret it as a toric fan", font_size=40).to_corner(DL)
        
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
        
        dots = [Dot(point=axes.coords_to_point(*pt), color=TEAL).set_z_index(20) for pt in points]
        
        s_lines = [[0,2],[0,3],[0,5],[0,6],[0,8],[0,9]]
        special_lines = [{2,9},{3,5},{8,6}]
        lines = []
        for i,j in s_lines:
            lines.append(Line(start=axes.coords_to_point(*points[i]), end=axes.coords_to_point(*points[j]), color=PURE_RED).set_z_index(10))
        for s in special_lines:
            i,j = tuple(sorted(s))
            lines.append(Line(start=axes.coords_to_point(*points[i]), end=axes.coords_to_point(*points[j]), color=PURE_RED).set_z_index(10))
        new_lines = [[0,1],[0,4],[0,7]]
        new_lines = [Line(start=axes.coords_to_point(*points[l[0]]), end=axes.coords_to_point(*points[l[1]]), color=PURE_RED).set_z_index(10) for l in new_lines]
            
        simplices = [[0,3,2],[0,2,1],[0,1,9],[0,9,8],[0,8,7],[0,7,6],[0,6,5],[0,5,4],[0,4,3]]
        triangs = [Polygon(*[axes.coords_to_point(*points[i]) for i in s], stroke_opacity=0, fill_opacity=1, fill_color=GOLD).set_z_index(5) for s in simplices]
        
        t1 = Tex("Star:", font_size=50).shift(UP*2+RIGHT*4)
        yes = Tex("yes", font_size=50, color=PURE_GREEN).next_to(t1, RIGHT).shift(DOWN*0.1)
        no = Tex("no", font_size=50, color=PURE_RED).next_to(t1, RIGHT).shift(DOWN*0.05)
        
        self.next_section("STExplanation 0", PresentationSectionType.NORMAL)
        self.add(title_right)
        self.play(FadeIn(title_left))
        self.next_section("STExplanation 1", PresentationSectionType.NORMAL)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.play(AnimationGroup(*[FadeIn(pt) for pt in dots], lag_ratio=0.05), Create(poly), AnimationGroup(*[Create(line) for line in lines], lag_ratio=0.05))
        self.next_section("STExplanation 2", PresentationSectionType.NORMAL)
        self.play(Write(t0))
        self.play(Write(t1), Write(no))
        self.next_section("STExplanation 3", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(lines[-3], new_lines[0]))
        self.next_section("STExplanation 4", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(lines[-2], new_lines[1]))
        self.next_section("STExplanation 4", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(lines[-1], new_lines[2]), ReplacementTransform(no, yes))
        self.next_section("STExplanation 5", PresentationSectionType.NORMAL)
        self.play(FadeOut(t0),FadeOut(t1),FadeOut(yes))
        self.play(FadeIn(t2), AnimationGroup(*[FadeIn(t) for t in triangs], lag_ratio=0.05), FadeOut(poly), *[FadeOut(d) for d in dots[1:]])
        self.next_section("STExplanation 6", PresentationSectionType.SKIP)
        self.play(*[FadeOut(l) for l in lines], Unwrite(t2), Unwrite(title), FadeOut(dots[0]),
                  *[FadeOut(l) for l in new_lines], *[FadeOut(t) for t in triangs])