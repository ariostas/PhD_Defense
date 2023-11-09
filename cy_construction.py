from manim import *
from manim_editor import PresentationSectionType

class CYConstruction(Scene):
    def construct(self):
        
        title = Title(r"Constructing suitable toric varieties", font_size=45)
        
        t0 =  Tex("Follow the procedure proposed by Batyrev '93.", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        t1 = Tex("1. Start with a 4D reflexive polytope.", font_size=40).next_to(t0, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t1_2 = Tex("Kreuzer-Skarke (KS) database.", font_size=40).next_to(t1, RIGHT, buff=0.2)
        t2_0 = Tex(r"2. Find a \ \ \ \ \ \ ,\ \ \ \ \ \ \ \ \ \ \ , \ \ \ \ \ \ \ triangulation (FRST).", font_size=40).next_to(t1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t2_1 = Tex(r"Fine", font_size=40, color=PURE_GREEN).next_to(t2_0, LEFT, buff=-2.6).shift(UP*0.03)
        t2_2 = Tex(r"Regular", font_size=40, color=PURE_RED).next_to(t2_0, LEFT, buff=-4.3).shift(DOWN*0.01)
        t2_3 = Tex(r"Star", font_size=40, color=TEAL).next_to(t2_0, LEFT, buff=-5.3).shift(UP*0.03)
        t2 = VGroup(t2_0, t2_1, t2_2, t2_3)
        t3 = Tex("3. Anticanonical divisor of the resulting toric variety is CY${}_3$.", font_size=40).next_to(t2, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        dual_eq = Tex(r"$\Delta^\circ = \{y\in \mathbb{R}^n | x\cdot y\geq -1 \text{ for all }x\in\Delta\}$", font_size=40).shift(DOWN*0.8)
        
        poly_count = Tex(r"\begin{tabular}{|c|c|}\hline dim & count \\ \hline 1 & 1 \\ 2 & 16 \\ 3 & 4,319 \\ 4 & 473,800,776 \\ 5 & ? \\ \hline\end{tabular}",
                         font_size=35).to_edge(RIGHT, buff=1).to_edge(UP, buff=1.5)
        
        axes1 = Axes(
            x_range=(-1, 1, 1),
            y_range=(-1, 1, 1),
            x_length=2,
            y_length=2,
            tips=False,
        ).to_edge(DOWN, buff=0.5).to_edge(LEFT, buff=4)
        
        axes2 = Axes(
            x_range=(-1, 1, 1),
            y_range=(-1, 1, 1),
            x_length=2,
            y_length=2,
            tips=False,
        ).to_edge(DOWN, buff=0.5).to_edge(RIGHT, buff=4)
        
        vert1 = [[-1,1],[-1,-1],[1,1],[1,-1]]
        pts1 = [[-1,0],[0,1],[0,0],[0,-1],[1,0]]
        
        vert2 = [[-1,0],[0,1],[0,-1],[1,0]]
        pts2 = [[0,0]]
        
        v_dots1 = [Dot(point=axes1.coords_to_point(*pt), color=PURE_BLUE).set_z_index(3) for pt in vert1]
        p_dots1 = [Dot(point=axes1.coords_to_point(*pt), color=WHITE).set_z_index(3) for pt in pts1]
        
        v_dots2 = [Dot(point=axes2.coords_to_point(*pt), color=PURE_RED).set_z_index(3) for pt in vert2]
        p_dots2 = [Dot(point=axes2.coords_to_point(*pt), color=WHITE).set_z_index(3) for pt in pts2]
        
        edges1 = [[0,1],[0,2],[1,3],[2,3]]
        edges2 = [[0,1],[0,2],[1,3],[2,3]]
        
        e_lines1 = [Line(start=axes1.c2p(*vert1[i]), end=axes1.c2p(*vert1[j]), color=PURE_RED) for i,j in edges1]
        i_lines1 = [Line(start=axes1.c2p(0,0), end=axes1.c2p(*pt), color=WHITE) for pt in pts1+vert1 if any(pt)]
        
        e_lines2 = [Line(start=axes2.c2p(*vert2[i]), end=axes2.c2p(*vert2[j]), color=PURE_BLUE) for i,j in edges2]
        i_lines2 = [Line(start=axes2.c2p(0,0), end=axes2.c2p(*pt), color=WHITE) for pt in vert2 if any(pt)]
        
        self.next_section("CYConstruction 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("CYConstruction 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("CYConstruction 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("CYConstruction 3", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(pt) for pt in v_dots1], lag_ratio=0.05),
                  AnimationGroup(*[Create(pt) for pt in p_dots1], lag_ratio=0.05),
                  AnimationGroup(*[Create(l) for l in e_lines1], lag_ratio=0.05),
                 )
        self.play(Write(dual_eq))
        self.next_section("CYConstruction 4", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[ReplacementTransform(pt.copy(), l) for pt,l in zip(v_dots1, e_lines2)], lag_ratio=0.05),
                  AnimationGroup(*[ReplacementTransform(l.copy(), pt) for l,pt in zip(e_lines1, v_dots2)], lag_ratio=0.05),
                  run_time=1.5,
                 )
        self.play(FadeIn(p_dots2[0]))
        self.next_section("CYConstruction 5", PresentationSectionType.NORMAL)
        self.play(Create(poly_count))
        self.wait(0.1)
        self.next_section("CYConstruction 6", PresentationSectionType.NORMAL)
        self.play(FadeOut(poly_count), FadeOut(dual_eq))
        self.play(FadeIn(t1_2))
        self.next_section("CYConstruction 7", PresentationSectionType.NORMAL)
        self.play(FadeIn(t2))
        self.next_section("CYConstruction 8", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(l) for l in i_lines1], lag_ratio=0.05),
                  AnimationGroup(*[Create(l) for l in i_lines2], lag_ratio=0.05),
                 )
        self.next_section("CYConstruction 9", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3))
        self.next_section("CYConstruction 10", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [title,t0,t1,t1_2,t2,t3]+e_lines1+e_lines2+i_lines1+i_lines2+v_dots1+p_dots1+v_dots2+p_dots2])