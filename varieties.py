from manim import *
from manim_editor import PresentationSectionType

class Varieties(Scene):
    def construct(self):
        
        question = Tex(r"How can we construct CY threefolds?", font_size=50)
        answer = Tex(r"Answer: Using Toric {{Varieties}}", font_size=50).next_to(question, DOWN, buff=1)
        
        title = Tex(r"Algebraic {{Varieties}}", font_size=45).to_edge(UP).to_edge(LEFT, buff=1)
        
        t0 = Tex("Essential idea: zero-loci of polynomials", font_size=40).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        poly = Tex("$f(x,y)=x^2+y^2-1$", font_size=40).next_to(t0, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        axes = Axes(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            x_length=6,
            y_length=6,
            tips=False,
        ).to_edge(RIGHT, buff=1).shift(DOWN*0.5)
        
        r = Tex(r"{{ $\mathbb{R}^2$ }}", font_size=40).next_to(axes, UP).to_edge(RIGHT, buff=1).shift(DOWN*0.5+LEFT*0.5)
        f_zero = Tex(r"{{ $f(x,y)=0$ }}", font_size=40).next_to(axes, DOWN).shift(UP*1.5+LEFT*2.5)
        v_data = VGroup(r, f_zero)
        
        circ = Circle(radius=axes.height/4, color=PURE_RED).move_to(axes.c2p(0,0))
        
        var = Tex(r"$V=\{(x,y)\in$ {{ $\mathbb{R}^2$ }} $|$ {{ $f(x,y)=0$ }} $\}$", font_size=40).next_to(poly, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        self.next_section("Varieties 0", PresentationSectionType.NORMAL)
        self.play(Write(question))
        self.next_section("Varieties 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(answer))
        self.next_section("Varieties 2", PresentationSectionType.NORMAL)
        self.play(FadeOut(question), TransformMatchingTex(answer, title))
        self.next_section("Varieties 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("Varieties 4", PresentationSectionType.NORMAL)
        self.play(Write(poly))
        self.next_section("Varieties 5", PresentationSectionType.NORMAL)
        self.play(Write(r), Create(axes))
        self.next_section("Varieties 6", PresentationSectionType.NORMAL)
        self.play(Write(f_zero))
        self.play(Create(circ))
        self.next_section("Varieties 7", PresentationSectionType.NORMAL)
        self.play(TransformMatchingTex(v_data, var))
        self.wait(0.1)
        self.next_section("Varieties 8", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [t0, poly, axes, circ, var]])