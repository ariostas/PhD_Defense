from manim import *
from manim_editor import PresentationSectionType

import random
random.seed(42)

class AdSVacua(Scene):
    def construct(self):
        
        title = Title(r"Constructing AdS Vacua with exponentially small c.c.s", font_size=45)
        
        t0 = Tex(r"We used CYTools to search for suitable CYs, which required computing\\various kinds of data for $\mathcal{O}(100,000)$ CYs.", tex_environment="flushleft", font_size=35).next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t1 = Tex(r"We tuned parameters, so that the perturbative part of the flux superpotential vanishes, so the only contributions come from instanton corrections.", tex_environment="flushleft", font_size=35).next_to(t0, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t_w = MathTex(r"W_{\text{flux}}\propto -{{2}} e^{2\pi i\tau\frac{7}{29}}+{{252}}e^{2\pi i\tau\frac{7}{28}}+\mathcal{O}(e^{2\pi i\tau\frac{43}{116}})", font_size=35).next_to(t1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t_lambda = MathTex(r"\Lambda\propto -\left( \frac{ \ \ \ \ \ }{ \ \ \ \ \ }\right)^{58}\approx -10^{-122}", font_size=35).next_to(t1, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        t_2 = MathTex("2", color=PURE_RED, font_size=35).move_to(t_lambda.get_center()+LEFT*0.53+UP*0.18)
        t_252 = MathTex("252", color=PURE_RED, font_size=35).move_to(t_lambda.get_center()+LEFT*0.53+DOWN*0.22)
        t_gv = Tex(r"GV invariants", font_size=35).next_to(t_w, DOWN, buff=1.2).shift(LEFT)
        t_w_2 = t_w.split()[1]
        t_w_252 = t_w.split()[3]
        a1 = Arrow(start=t_gv.get_center(), end=t_w_2.get_center())
        a2 = Arrow(start=t_gv.get_center(), end=t_w_252.get_center())
        t2 = Tex(r"We also checked for control of the main corrections that could spoil the constructions. They scale as", tex_environment="flushleft", font_size=35).next_to(t_w, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        t_corr = MathTex(r"\xi=GV_{n\mathcal{C}}\exp(-2\pi n\ \text{vol}(\mathcal{C}))", font_size=35).next_to(t2, DOWN, buff=0.5)
        t3 = Tex(r"We needed to compute GV invariants along potent rays at large $h^{1,1}$.", font_size=35).next_to(t_corr, DOWN, buff=0.3)
        box = Rectangle(
            height=t3.height+0.2, width=t3.width+0.2,
            fill_opacity=0, stroke_color=PURE_RED,
        ).move_to(t3.get_center())
        
        axes = Axes(
            x_range=[1, 10, 1],
            y_range=[-500, 0, 100],
            x_length=10,
            y_length=5.5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": UP},
            tips=False,
        ).shift(RIGHT*0.5+DOWN*0.5)
        y_label = axes.get_y_axis_label(Tex(r"$\log(\xi_n)$").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.4)
        x_label = axes.get_x_axis_label("n", edge=UP, direction=UP, buff=0.4)
        plot_labels = VGroup(x_label, y_label)
        with open("./data/decay_plot.txt", "r") as f:
            plot_data = [[eval(c) for c in l.split(",")] for l in f.readlines()]
        random.shuffle(plot_data)
        dots = [Dot(point=axes.coords_to_point(i,v), color=TEAL).set_z_index(10) for i,v in enumerate(plot_data[0], 1)]
        x_vals = list(range(1,11))
        plot1 = axes.plot_line_graph(x_values=x_vals, y_values=plot_data[0], line_color=PURE_RED, add_vertex_dots=False)
        colors = [PURE_RED, RED, RED_A, RED_E, PURE_BLUE, BLUE, BLUE_A, BLUE_E, PURE_GREEN, GREEN, GREEN_A, GREEN_E, YELLOW, YELLOW_A, YELLOW_E, TEAL, TEAL_A, TEAL_E,
                 PURPLE, PURPLE_A, PURPLE_E, MAROON, MAROON_A, MAROON_E, PINK, ORANGE, LIGHT_GRAY, LIGHT_BROWN, LIGHT_PINK]
        plots = [axes.plot_line_graph(x_values=x_vals, y_values=y_vals, line_color=random.choice(colors), add_vertex_dots=False).set_stroke(width=2)
                for y_vals in plot_data[1:]]
        rectangle = Polygon(axes.c2p(1,-501), axes.c2p(11,-501), axes.c2p(11,-800), axes.c2p(1,-800), stroke_opacity=0, fill_opacity=1, fill_color=BLACK).set_z_index(10000)
        
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
        blist_out.fade_all_but(5, opacity=0.25)
    
        self.next_section("AdSVacua 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("AdSVacua 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("AdSVacua 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.play(Write(t_w))
        self.next_section("AdSVacua 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_gv), Create(a1), Create(a2))
        self.play(t_w_2.animate.set_color(PURE_RED), t_w_252.animate.set_color(PURE_RED))
        self.next_section("AdSVacua 4", PresentationSectionType.NORMAL)
        self.play(Write(t_lambda), ReplacementTransform(t_w_2.copy(), t_2), ReplacementTransform(t_w_252.copy(), t_252))
        self.next_section("AdSVacua 5", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [a1,a2,t_gv]])
        self.play(FadeIn(t_corr), FadeIn(t2))
        self.next_section("AdSVacua 6", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3), Create(box))
        self.next_section("AdSVacua 7", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [title,t0,t1,t_w,t_2,t_252,t_lambda,t2,t_corr,t3,box]])
        self.play(Create(axes), Write(plot_labels), FadeIn(rectangle))
        self.wait(0.1)
        self.next_section("AdSVacua 8", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[FadeIn(d) for d in dots], lag_ratio=0.05))
        self.play(Create(plot1))
        self.next_section("AdSVacua 9", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[FadeOut(d) for d in dots], lag_ratio=0.05))
        self.play(plot1.animate.set_stroke(width=2))
        self.next_section("AdSVacua 10", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(p) for p in plots[:200]], lag_ratio=0.05))
        self.next_section("AdSVacua 11", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(p) for p in plots[200:]], lag_ratio=0.05, run_time=5))
        self.next_section("AdSVacua 12", PresentationSectionType.NORMAL)
        self.play(Uncreate(axes), Unwrite(plot_labels), *[FadeOut(p) for p in plots], FadeOut(plot1))
        self.remove(rectangle)
        self.play(FadeIn(title_out), FadeIn(blist_out))
        self.next_section("AdSVacua 13", PresentationSectionType.SKIP)
        self.play(FadeOut(title_out), FadeOut(blist_out))