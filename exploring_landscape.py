from manim import *
from manim_editor import PresentationSectionType

class ExploringLandscape(Scene):
    def construct(self):
        
        title = Title(r"The secondary fan allows us to explore the landscape", font_size=50)
        
        t0 = Tex(r"This is a 2D cross-section of a\\491-dimensional secondary fan.", tex_environment="flushleft", font_size=40).next_to(title, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        t1 = Tex(r"Each colored region is a\\different triangulation!", tex_environment="flushleft", font_size=40).next_to(t0, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        t2 = Tex(r"We can explore the landscape\\by moving around in the\\secondary fan.", tex_environment="flushleft", font_size=40).next_to(t1, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        t3 = Tex(r"Side note: height vectors are very good\\representations for machine learning.", tex_environment="flushleft", font_size=35).next_to(t2, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        
        xsec = ImageMobject("images/491_xsec_frst.png")
        xsec.scale_to_fit_height(7).to_edge(LEFT, buff=0.5).to_edge(DOWN, buff=0)
        
        d = Dot(point=xsec.get_center()+RIGHT+UP, color=BLACK)
        
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
        blist_out.fade_all_but(3, opacity=0.25)
        
        self.next_section("ExploringLandscape 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("ExploringLandscape 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(xsec))
        self.play(FadeIn(t0))
        self.next_section("ExploringLandscape 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("ExploringLandscape 3", PresentationSectionType.SKIP)
        self.play(FadeIn(t2), FadeIn(d))
        self.next_section("ExploringLandscape 4", PresentationSectionType.COMPLETE_LOOP)
        self.play(d.animate.shift(UP+LEFT*3))
        self.play(d.animate.shift(DOWN*5+RIGHT*2))
        self.play(d.animate.shift(UP*2+LEFT*1))
        self.play(d.animate.shift(UP*2+RIGHT*3.5))
        self.play(d.animate.move_to(xsec.get_center()+RIGHT+UP))
        self.next_section("ExploringLandscape 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(t3), FadeOut(d))
        self.next_section("ExploringLandscape 6", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(title, title_out), *[FadeOut(o) for o in [xsec, t0,t1,t2,t3]])
        self.play(FadeIn(blist_out))
        self.next_section("ExploringLandscape 7", PresentationSectionType.SKIP)
        self.play(FadeOut(blist_out), FadeOut(title_out))