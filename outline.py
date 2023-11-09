from manim import *
from manim_editor import PresentationSectionType

class Outline(Scene):
    def construct(self):
        
        title = Title("Outline", font_size=50)
        
        blist = BulletedList(
            "Background and Motivation",
            "Computational Improvements and CYTools",
            "Exploring the KS Landscape",
            "Computational Mirror Symmetry",
            "Exponentially Small Cosmological Constants",
            "Conclusions",
            height=6, width=9,
        ).to_edge(LEFT, buff=1)

        cytools_logo = ImageMobject("images/cytools-circle.png")
        cytools_logo.scale_to_fit_height(3)
        cytools_logo.next_to(blist.submobjects[1], DOWN)
        cytools_logo.to_edge(LEFT, buff=1)
        cytools_logo.set_z_index(10)
        
        code = Code(
            "example_code/simple_example.py",
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
        )
        code.scale_to_fit_width(8)
        code.next_to(cytools_logo, RIGHT)
        code.to_edge(RIGHT, buff=1)
        code.set_z_index(10)
        
        xsec = ImageMobject("images/491_xsec.png")
        xsec.scale_to_fit_height(4)
        xsec.next_to(blist.submobjects[2], DOWN, buff=SMALL_BUFF)
        xsec.set_x(0)
        xsec.set_z_index(10)
        
        mirror_img = ImageMobject("images/mirror_symmetry.png")
        mirror_img.scale_to_fit_height(2.5)
        mirror_img.next_to(blist.submobjects[3], UP)
        mirror_img.to_edge(LEFT, buff=1.5)
        mirror_img.set_z_index(10)
        
        with open("latex/hodge_diamond.txt", "r") as f:
            hodge_diamond_str = f.read()
        hodge_diamond = Tex(hodge_diamond_str)
        hodge_diamond.scale_to_fit_height(2.5)
        hodge_diamond.next_to(blist.submobjects[3], UP)
        hodge_diamond.to_edge(RIGHT, buff=1.5)
        hodge_diamond.set_z_index(10)
        
        small_cc = MathTex("|\Lambda| \ll 1")
        small_cc.scale_to_fit_height(1)
        small_cc.next_to(blist.submobjects[4], UP)
        small_cc.to_edge(RIGHT, buff=1)
        small_cc.set_z_index(10)
        
        t_coauthors = Tex(r"Based on work with Mehmet Demirtas, Manki Kim, Liam McAllister and Jakob Moritz.", tex_environment="flushleft", font_size=35)
        
        self.next_section("Outline 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.play(Write(blist))
        self.next_section("Outline 1", PresentationSectionType.NORMAL)
        self.play(blist.animate.fade_all_but(0, opacity=0.25))
        self.wait(0.1)
        self.next_section("Outline 2", PresentationSectionType.NORMAL)
        self.play(blist.animate.fade_all_but(1, opacity=0.25), FadeIn(cytools_logo), FadeIn(code))
        self.wait(0.1)
        self.next_section("Outline 3", PresentationSectionType.NORMAL)
        self.play(FadeOut(cytools_logo), FadeOut(code))
        self.play(blist.animate.fade_all_but(2, opacity=0.25), FadeIn(xsec))
        self.wait(0.1)
        self.next_section("Outline 4", PresentationSectionType.NORMAL)
        self.play(FadeOut(xsec))
        self.play(blist.animate.fade_all_but(3, opacity=0.25), FadeIn(mirror_img), Write(hodge_diamond))
        self.wait(0.1)
        self.next_section("Outline 5", PresentationSectionType.NORMAL)
        self.play(FadeOut(mirror_img), FadeOut(hodge_diamond))
        self.play(blist.animate.fade_all_but(4, opacity=0.25), Write(small_cc))
        self.wait(0.1)
        self.next_section("Outline 6", PresentationSectionType.NORMAL)
        self.play(FadeOut(small_cc))
        self.play(blist.animate.fade_all_but(5, opacity=0.25))
        self.wait(0.1)
        self.next_section("Outline 7", PresentationSectionType.NORMAL)
        self.play(blist.animate.fade_all_but(0, opacity=1))
        self.wait(0.1)
        self.next_section("Outline 8", PresentationSectionType.NORMAL)
        self.play(FadeOut(title), FadeOut(blist))
        self.play(FadeIn(t_coauthors))
        self.next_section("Outline 9", PresentationSectionType.SKIP)
        self.play(FadeOut(t_coauthors))