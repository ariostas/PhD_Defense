from manim import *
from manim_editor import PresentationSectionType

class IntroSummary(Scene):
    def construct(self):
        
        title = Title("These toric varieties contain Calabi-Yau anticanonical divisors", font_size=40, include_underline=False)
        
        cy_img = ImageMobject("images/CY_image.png")
        cy_img.scale_to_fit_height(5.5)
        cy_img.next_to(title, DOWN, buff=0.5)
        cy_img_credit = Tex("Image by Geoffrey Fatin", font_size=25).next_to(cy_img, RIGHT, buff=0.5)
        
        t0 = Tex("Let's now talk about the work I've done with these manifolds", font_size=40).to_edge(DOWN)
        
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
        blist_out.fade_all_but(1, opacity=0.25)

        self.next_section("IntroSummary 0", PresentationSectionType.NORMAL)
        self.play(FadeIn(title))
        self.next_section("IntroSummary 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(cy_img), FadeIn(cy_img_credit))
        self.next_section("IntroSummary 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(t0))
        self.next_section("IntroSummary 3", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [title, t0, cy_img, cy_img_credit]])
        self.next_section("IntroSummary 4", PresentationSectionType.NORMAL)
        self.play(FadeIn(title_out), FadeIn(blist_out))
        self.next_section("IntroSummary 5", PresentationSectionType.SKIP)
        self.play(FadeOut(title_out), FadeOut(blist_out))