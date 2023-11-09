from manim import *
from manim_editor import PresentationSectionType

class ComputationalAdvancements(Scene):
    def construct(self):
        
        title = Title(r"Computational advancements", font_size=50)
        
        t0 = Tex("There are too many advancements to list.", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t1 = Tex(r"Let's discuss the extent to which our ability to study and use\\intricate CYs has increased.", tex_environment="flushleft", font_size=40).next_to(t0, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        t2 = Tex("Some concrete examples of improvements", font_size=40).next_to(title, DOWN, buff=0.5)
        t3 = Tex(r"We can compute all essential topological data in $\mathcal{O}(1)$ seconds,\\even in the most difficult cases.", tex_environment="flushleft", font_size=40).next_to(title, DOWN, buff=0.5)
        t3.to_edge(DOWN, buff=1.5).to_edge(LEFT, buff=1)
        t4 = Tex(r"We now have access to a virtually unlimited set of CYs.", tex_environment="flushleft", font_size=40).next_to(title, DOWN, buff=0.5)
        t4.to_edge(DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        table1 = Tex(r"Obtaining one triangulation\\ \begin{tabular}{|c|c|c|}\hline year & $h^{1,1}$ & CPU time \\ \hline 2014 & 25 & a few hours \\ 2017 & 491 & 2 s \\ 2023 & 491 & 20 ms \\ \hline\end{tabular}", font_size=40)
        table1.to_edge(LEFT, buff=1)
        table2 = Tex(r"Computing intersection numbers\\ \begin{tabular}{|c|c|c|}\hline year & $h^{1,1}$ & CPU time \\ \hline 2017 & 100 & 30 m \\ 2018 & 491 & 30 s \\ 2023 & 491 & 2 s \\ \hline\end{tabular}", font_size=40)
        table2.to_edge(RIGHT, buff=1)
        
        ks_title = Tex(r"KS Database", font_size=40).next_to(title, DOWN, buff=0.8).to_edge(RIGHT, buff=2)
        
        axes = Axes(
            x_range=[0, 500, 100],
            y_range=[0, 500, 100],
            x_length=5.5,
            y_length=5.5,
            axis_config={"include_numbers": True},
            tips=False,
        )
        
        y_label = axes.get_y_axis_label(r"h^{1,1}", edge=LEFT, direction=LEFT)
        x_label = axes.get_x_axis_label(r"h^{2,1}", edge=RIGHT, direction=UP, buff=0).shift(RIGHT*0.5)
        plot = VGroup(x_label, y_label, axes).to_edge(DOWN).to_edge(LEFT)
        
        arrow1 = Arrow(start=DOWN*3+RIGHT*2, end=UP*3+RIGHT*2)
        arrow1_txt = Tex(r"Complexity and $N_{\text{triangs}}$\\grows exponentially", font_size=30).next_to(arrow1, RIGHT, buff=0)
        
        arrow2_txt = Tex(r"Most of the complexity is here\\at $h^{1,1}=491$", font_size=30).move_to(arrow1_txt.get_center())
        arrow2 = Arrow(start=arrow2_txt.get_center()+LEFT*arrow2_txt.width/2, end=axes.c2p(11,491))
        
        easy = Tex(r"$h^{1,1}\lesssim 7$\\Many systematic studies\\Easy to study with SageMath", font_size=30, color=PURE_GREEN).to_edge(RIGHT, buff=0.6).to_edge(DOWN, buff=1)
        medium = Tex(r"$h^{1,1}\lesssim 20$\\Few limited studies\\Difficult to study with SageMath", font_size=30, color=YELLOW).next_to(easy, UP, buff=1)
        hard = Tex(r"Unreachable with SageMath\\Easy for us!", font_size=30, color=PURE_RED).next_to(medium, UP, buff=1)
        
        with open("data/hodge_pairs.txt", "r") as f:
            hodge_data = [eval(l) for l in f.readlines()]
        hodge_pairs = sorted([pt[:2] for pt in hodge_data], key=lambda p: p[1])
        # for testing
        #hodge_pairs = [pt for i,pt in enumerate(hodge_pairs) if i%50==0 or pt[1]==491]
            
        dots1 = [Dot(point=axes.c2p(*pt), radius=0.01, color=WHITE) for pt in hodge_pairs if pt[1]<=6]
        dots2 = [Dot(point=axes.c2p(*pt), radius=0.01, color=WHITE) for pt in hodge_pairs if 6<pt[1]<=20]
        dots3 = [Dot(point=axes.c2p(*pt), radius=0.01, color=WHITE) for pt in hodge_pairs if 20<pt[1]]
        
        new_title = Title(r"These advancements are now available as an open-source package", font_size=40)
        cytools_logo = ImageMobject("images/cytools-circle.png")
        cytools_logo.scale_to_fit_height(6).next_to(new_title, DOWN, buff=0.5)
        
        code = Code(
            "example_code/longer_example.py",
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
        ).scale_to_fit_width(new_title.width).next_to(new_title, DOWN, buff=0.5)
        
        features = Tex(r"Intuitive to use and includes algorithms to do a variety of computations, including intersection numbers, Mori and K\"ahler cones, SR ideals, GLSM charge matrices, and many other things.", tex_environment="flushleft", font_size=35)
        features.scale_to_fit_width(new_title.width).next_to(code, DOWN, buff=0.5)
        
        title_out = Title("Outline", font_size=50)
        
        blist_out = BulletedList(
            "Background and Motivation",
            "Computational Improvements and CYTools",
            "Exploring the KS Landscape",
            "Computational Mirror Symmetry",
            "Exponentially Small Cosmological Constants",
            "Conclusions",
            height=6, width=9,
        ).to_edge(LEFT, buff=1)
        blist_out.fade_all_but(2, opacity=0.25)
        
        self.next_section("ComputationalAdvancements 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("ComputationalAdvancements 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("ComputationalAdvancements 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("ComputationalAdvancements 3", PresentationSectionType.NORMAL)
        self.play(FadeOut(t0), FadeOut(t1))
        self.play(FadeIn(ks_title), Create(plot))
        self.play(*[FadeIn(d) for d in dots1+dots2+dots3])
        self.next_section("ComputationalAdvancements 4", PresentationSectionType.NORMAL)
        self.play(Create(arrow1), FadeIn(arrow1_txt))
        self.next_section("ComputationalAdvancements 5", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(arrow1_txt, arrow2_txt), ReplacementTransform(arrow1, arrow2))
        self.wait(0.1)
        self.next_section("ComputationalAdvancements 6", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [arrow2, arrow2_txt, ks_title]+dots1+dots2+dots3])
        for d in dots1:
            d.set_color(PURE_GREEN)
        for d in dots2:
            d.set_color(YELLOW)
        for d in dots3:
            d.set_color(PURE_RED)
        self.play(AnimationGroup(*[Create(d) for d in dots1], lag_ratio=0.05, run_time=1, rate_func=rate_functions.linear), FadeIn(easy))
        self.next_section("ComputationalAdvancements 7", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(d) for d in dots2], lag_ratio=0.05, run_time=2, rate_func=rate_functions.linear), FadeIn(medium))
        self.next_section("ComputationalAdvancements 8", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(d) for d in dots3], lag_ratio=0.05, run_time=2, rate_func=rate_functions.linear), FadeIn(hard))
        self.wait(0.1)
        self.next_section("ComputationalAdvancements 9", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [easy, medium, hard, plot]+dots1+dots2+dots3])
        self.play(FadeIn(t2))
        self.next_section("ComputationalAdvancements 10", PresentationSectionType.NORMAL)
        self.play(FadeIn(table1))
        self.next_section("ComputationalAdvancements 11", PresentationSectionType.NORMAL)
        self.play(FadeIn(table2))
        self.next_section("ComputationalAdvancements 12", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3))
        self.next_section("ComputationalAdvancements 13", PresentationSectionType.NORMAL)
        self.play(FadeIn(t4))
        self.next_section("ComputationalAdvancements 14", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [t2,t3,t4,table1,table2]], ReplacementTransform(title, new_title))
        self.play(FadeIn(cytools_logo))
        self.next_section("ComputationalAdvancements 15", PresentationSectionType.NORMAL)
        self.play(FadeOut(cytools_logo))
        self.play(FadeIn(code), FadeIn(features))
        self.next_section("ComputationalAdvancements 16", PresentationSectionType.NORMAL)
        self.play(FadeOut(code), FadeOut(features), ReplacementTransform(new_title, title_out))
        self.play(FadeIn(blist_out))
        self.next_section("ComputationalAdvancements 17", PresentationSectionType.SKIP)
        self.play(FadeOut(title_out), FadeOut(blist_out))