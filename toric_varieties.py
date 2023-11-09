from manim import *
from manim_editor import PresentationSectionType

class ToricVarieties(Scene):
    def construct(self):
        
        old_title = Tex(r"Algebraic {{Varieties}}", font_size=45).to_edge(UP).to_edge(LEFT, buff=1)
        title = Tex(r"{{Toric}} {{Varieties}}", font_size=45).to_edge(UP).to_edge(LEFT, buff=1)
        new_title = Tex(r"{{Toric}} {{Varieties}} (a rough explanation)", font_size=45).to_edge(UP).to_edge(LEFT, buff=1)
        
        t0 = Tex("Basic intuition: gluing varieties to an algebraic torus", font_size=40).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        t1 = Tex(r"Algebraic torus $\mathbb{C}^*=\mathbb{C}-\{0\}$", font_size=40).next_to(t0, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        t2 = Tex(r"Information is encoded in toric fan\\(collection of cones in $d$-dim lattice)", font_size=40).next_to(t1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        t3 = Tex(r"$n$-dim cone $\leftrightarrow$ $(d-n)$-dim variety", font_size=40).next_to(t2, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        example = Tex(r"Simple example", font_size=40).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        dim1 = Tex(r"{{$d=$}} $1$", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        dim2 = Tex(r"{{$d=$}} $2$", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        
        pieces = Tex(r"Pieces:", font_size=40).to_edge(LEFT, buff=1).shift(UP*0.5)
        result = Tex(r"Resulting variety:", font_size=40).to_edge(DOWN, buff=1).to_edge(LEFT, buff=1)
        
        # pieces 1
        ex1_cs1 = Tex(r"$\mathbb{C}^*$", font_size=45, color=PURE_RED).next_to(pieces, RIGHT, buff=0.3)
        ex1_cs0_1 = Tex(r"pt", font_size=45, color=PURE_BLUE).next_to(ex1_cs1, DOWN, buff=0.3)
        ex1_cs0_2 = ex1_cs0_1.copy().next_to(ex1_cs0_1, RIGHT, buff=0.3)
        
        # pieces 2
        ex2_cs2 = Tex(r"$(\mathbb{C}^*)^2$", font_size=45, color=PURE_RED).next_to(pieces, RIGHT, buff=0.3)
        ex2_cs1_1 = Tex(r"$\mathbb{C}^*$", font_size=45, color=PURE_BLUE).next_to(ex2_cs2, DOWN, buff=0.3).shift(LEFT*0.2)
        ex2_cs1_2 = ex2_cs1_1.copy().next_to(ex2_cs1_1, RIGHT, buff=0.3)
        ex2_cs1_3 = ex2_cs1_2.copy().next_to(ex2_cs1_2, RIGHT, buff=0.3)
        ex2_cs0_1 = Tex(r"pt", font_size=45, color=GOLD).next_to(ex2_cs1_1, DOWN, buff=0.3)
        ex2_cs0_2 = ex2_cs0_1.copy().next_to(ex2_cs0_1, RIGHT, buff=0.3)
        ex2_cs0_3 = ex2_cs0_2.copy().next_to(ex2_cs0_2, RIGHT, buff=0.3)
        
        # results
        res1_0 = Tex(r"$\mathbb{C}^*$", font_size=45).next_to(result, RIGHT, buff=0.2)
        res1_1 = Tex(r"$\mathbb{C}$", font_size=45).next_to(result, RIGHT, buff=0.2)
        res1_2 = Tex(r"$\mathbb{P}$", font_size=45).next_to(result, RIGHT, buff=0.2)
        res2 = Tex(r"$\mathbb{P}^2$", font_size=45).next_to(result, RIGHT, buff=0.2)
        
        axes = Axes(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            x_length=6,
            y_length=6,
            tips=False,
        ).to_edge(RIGHT, buff=1).shift(DOWN*0.5)
        orig = Dot(point=axes.c2p(0,0), radius=0.05, color=WHITE)
        
        orig_colored = Dot(point=axes.c2p(0,0), color=PURE_RED).set_z_index(5)
        
        cone1_1 = Arrow(start=axes.c2p(-0.2,0), end=axes.c2p(2.3,0), color=PURE_BLUE).set_z_index(3)
        cone1_11 = Arrow(start=axes.c2p(0.2,0), end=axes.c2p(-2.3,0), color=PURE_BLUE).set_z_index(3)
        cone1_2 = Arrow(start=axes.c2p(0,-0.2), end=axes.c2p(0,2.3), color=PURE_BLUE).set_z_index(3)
        cone1_3 = Arrow(start=axes.c2p(0.1,0.1), end=axes.c2p(-2.,-2.), color=PURE_BLUE).set_z_index(3)
        
        cone2_1 = Polygon(*[axes.c2p(*c) for c in [[0,0],[0,2],[2,0]]], fill_color=GOLD, stroke_opacity=0, fill_opacity=1)
        cone2_2 = Polygon(*[axes.c2p(*c) for c in [[0,0],[0,2],[-1.8,-1.8]]], fill_color=GOLD, stroke_opacity=0, fill_opacity=1)
        cone2_3 = Polygon(*[axes.c2p(*c) for c in [[0,0],[-1.8,-1.8],[2,0]]], fill_color=GOLD, stroke_opacity=0, fill_opacity=1)
        
        self.next_section("ToricVarieties 0", PresentationSectionType.NORMAL)
        self.play(TransformMatchingTex(old_title, title))
        self.play(TransformMatchingTex(title, new_title))
        self.next_section("ToricVarieties 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("ToricVarieties 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("ToricVarieties 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(t2))
        self.next_section("ToricVarieties 4", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3))
        self.next_section("ToricVarieties 5", PresentationSectionType.NORMAL)
        self.play(FadeOut(t0), FadeOut(t1), FadeOut(t2), FadeOut(t3))
        self.play(FadeIn(example))
        self.next_section("ToricVarieties 6", PresentationSectionType.NORMAL)
        self.play(FadeIn(dim1))
        self.play(Create(axes.submobjects[0]), Write(result), Create(orig), Write(pieces))
        self.next_section("ToricVarieties 7", PresentationSectionType.NORMAL)
        self.play(Create(orig_colored))
        self.next_section("ToricVarieties 8", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(orig_colored.copy(), ex1_cs1))
        self.next_section("ToricVarieties 9", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(ex1_cs1.copy(), res1_0))
        self.next_section("ToricVarieties 10", PresentationSectionType.NORMAL)
        self.play(FadeOut(res1_0), Create(cone1_1))
        self.next_section("ToricVarieties 11", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(cone1_1.copy(), ex1_cs0_1))
        self.next_section("ToricVarieties 12", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(VGroup(ex1_cs1.copy(), ex1_cs0_1.copy()), res1_1))
        self.next_section("ToricVarieties 13", PresentationSectionType.NORMAL)
        self.play(FadeOut(res1_1), Create(cone1_11))
        self.next_section("ToricVarieties 14", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(cone1_11.copy(), ex1_cs0_2))
        self.next_section("ToricVarieties 15", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(VGroup(ex1_cs1.copy(), ex1_cs0_1.copy(), ex1_cs0_2.copy()), res1_2))
        self.next_section("ToricVarieties 16", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [res1_2, ex1_cs1, ex1_cs0_1, ex1_cs0_2, orig_colored, cone1_1, cone1_11]])
        self.play(TransformMatchingTex(dim1, dim2), Create(axes.submobjects[1]))
        self.play(AnimationGroup(*[Create(c) for c in [orig_colored, cone1_1, cone1_2, cone1_3, cone2_1, cone2_2, cone2_3]], lag_ratio=0.05, run_time=2))
        self.next_section("ToricVarieties 17", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[ReplacementTransform(c.copy(),cc) for c,cc in 
                                   [[orig_colored,ex2_cs2], 
                                    [cone1_1,ex2_cs1_1],
                                    [cone1_2,ex2_cs1_2],
                                    [cone1_3,ex2_cs1_3],
                                    [cone2_1,ex2_cs0_1],
                                    [cone2_2,ex2_cs0_2],
                                    [cone2_3,ex2_cs0_3]]], lag_ratio=0.05))
        self.next_section("ToricVarieties 18", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(VGroup(*[o.copy() for o in [ex2_cs2,ex2_cs1_1,ex2_cs1_2,ex2_cs1_3,ex2_cs0_1,ex2_cs0_2,ex2_cs0_3]]), res2))
        self.next_section("ToricVarieties 19", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [ex2_cs2,ex2_cs1_1,ex2_cs1_2,ex2_cs1_3,ex2_cs0_1,ex2_cs0_2,ex2_cs0_3,new_title,res2,
                                         dim2,example,pieces,result,axes,orig,orig_colored,cone1_1,cone1_2,cone1_3,cone2_1,cone2_2,cone2_3]])