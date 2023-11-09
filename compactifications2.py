from manim import *
from manim_editor import PresentationSectionType

class Compactifications2(Scene):
    def construct(self):
        
        title = Title(r"How do we deal with a 10D spacetime?", font_size=45)
        
        t1 =  Tex("Answer: make some dimensions compact and small.", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        t3 = Tex("What can we use for the compactified space?", font_size=40).next_to(t1, DOWN, buff=0.8).to_edge(LEFT, buff=1)
        
        t2 = Tex(r"spacetime $=$ (spacetime we see) $\times$ (compactified space)", font_size=40)
        t2.to_edge(LEFT, buff=1).shift(RIGHT*2)
        t2_1 = Tex(r"{{spacetime}} {{$=$}} {{(spacetime we see)}} {{$\times$}} {{(compactified space)}}", font_size=40)
        t2_1.to_edge(LEFT, buff=1).shift(RIGHT*2)
        t2_2 = Tex(r"{{spacetime}} {{$=$}} {{$\mathbb{R}^{3,1}$}} {{$\times$}} {{(compactified space)}}", font_size=40)
        t2_2.to_edge(LEFT, buff=1).shift(RIGHT*2)
        t2_3 = Tex(r"{{spacetime}} {{$=$}} {{$\mathbb{R}^{3,1}$}} {{$\times$}} {{(CFT with $c=9$)}}", font_size=40)
        t2_3.to_edge(LEFT, buff=1).shift(RIGHT*2)
        t2_4 = Tex(r"{{spacetime}} {{$=$}} {{$\mathbb{R}^{3,1}$}} {{$\times$}} {{$M_6$}}", font_size=40)
        t2_4.to_edge(LEFT, buff=1).shift(RIGHT*2)
        t2_5 = Tex(r"{{spacetime}} {{$=$}} {{$\mathbb{R}^{3,1}$}} {{$\times$}} {{CY${}_3$}}", font_size=40)
        t2_5.to_edge(LEFT, buff=1).shift(RIGHT*2)
        
        t4 = Tex(r"Too difficult", font_size=45, color=PURE_RED).shift(DOWN)
        t4_2 = Tex(r"Still too difficult", font_size=45, color=PURE_RED).shift(DOWN)
        t4_3 = Tex(r"Difficult, but manageable", font_size=45, color=PURE_GREEN).shift(DOWN)
        
        t5 = Tex(r"Benefits of working with Calabi-Yau compactifications:", font_size=40).to_edge(LEFT, buff=1)
        
        blist = BulletedList(
            "Preserve some supersymmetry, providing more control.",
            "Allow for phenomenologically interesting constructions.",
            "Colossal set of options to choose from.",
            font_size=40,
        ).next_to(t5, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        self.add(title, t1)
        self.next_section("Compactifications 2-0", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3))
        self.next_section("Compactifications 2-1", PresentationSectionType.NORMAL)
        self.play(Write(t2))
        self.add(t2_1)
        self.remove(t2)
        self.next_section("Compactifications 2-2", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(t2_1, t2_2))
        self.next_section("Compactifications 2-3", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(t2_2, t2_3))
        self.next_section("Compactifications 2-4", PresentationSectionType.NORMAL)
        self.play(FadeIn(t4))
        self.next_section("Compactifications 2-5", PresentationSectionType.NORMAL)
        self.play(FadeOut(t4))
        self.play(ReplacementTransform(t2_3, t2_4))
        self.next_section("Compactifications 2-6", PresentationSectionType.NORMAL)
        self.play(FadeIn(t4_2))
        self.next_section("Compactifications 2-7", PresentationSectionType.NORMAL)
        self.play(FadeOut(t4_2))
        self.play(ReplacementTransform(t2_4, t2_5))
        self.next_section("Compactifications 2-8", PresentationSectionType.NORMAL)
        self.play(FadeIn(t4_3))
        self.next_section("Compactifications 2-9", PresentationSectionType.NORMAL)
        self.play(FadeOut(t4_3))
        self.play(FadeOut(t1), FadeOut(t3), t2_5.animate.scale(1.5).next_to(title, DOWN, buff=1))
        self.play(FadeIn(t5))
        self.next_section("Compactifications 2-10", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[0]))
        self.next_section("Compactifications 2-11", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[1]))
        self.next_section("Compactifications 2-12", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[2]))
        self.next_section("Compactifications 2-13", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [title, t2_5, t5, blist]])