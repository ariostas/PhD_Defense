from manim import *
from manim_editor import PresentationSectionType

class Conclusions(Scene):
    def construct(self):
        
        title = Title(r"Conclusions and Outlook", font_size=50)
        
        blist = BulletedList(
            r"We developed a powerful collection of tools to study and use the enormous\\set of CYs obtainable from the KS database.",
            r"We devised new techniques to explore the KS landscape, allowing for future\\systematic studies and AI-guided explorations.",
            r"Our improvements in computational mirror symmetry provide us with\\powerful topological information even in the most intricate cases.",
            r"Using all these computational advancements, we constructed the first\\explicit examples of vacua with exponentially small cosmological constants.",
            r"We hope that these tools will continue to help with the construction\\of increasingly realistic models.",
            font_size=35,
        ).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        title2 = Title(r"Acknowledgements", font_size=50)
        
        blist2 = BulletedList(
            r"Advisor: Liam McAllister",
            r"Other committee members: Tom Hartman and Jared Maxson",
            r"Group members and affiliates: Arjun Chaturvedi, Gauri Batra,\\Mehmet Demirtas, Geoffrey Fatin, Naomi Gendler, Manki Kim,\\Dnyanesh Kulkarni, Jonathan Letai, Daniel Longenecker, Nate MacFadden,\\Jakob Moritz, Richard Nally, Murali Saravanan, Andreas Schachner,\\Elijah Sheridan, Michael Stepniczka, Mike Stillman, Sam Weiss.",
            r"The physics department",
            r"My family",
            r"My girlfriend, Julia",
            r"My friends",
            font_size=30,
            buff=0.3,
            width=12,
            height=10,
        ).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        t_thanks = Tex(r"Thank you!", font_size=60)
        
        self.next_section("Conclusions 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("Conclusions 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[0]))
        self.next_section("Conclusions 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[1]))
        self.next_section("Conclusions 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[2]))
        self.next_section("Conclusions 4", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[3]))
        self.next_section("Conclusions 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[4]))
        self.next_section("Conclusions 6", PresentationSectionType.NORMAL)
        self.play(FadeOut(blist), ReplacementTransform(title, title2))
        self.next_section("Conclusions 7", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[0]))
        self.next_section("Conclusions 8", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[1]))
        self.next_section("Conclusions 9", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[2]))
        self.next_section("Conclusions 10", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[3]))
        self.next_section("Conclusions 11", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[4]))
        self.next_section("Conclusions 12", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[5]))
        self.next_section("Conclusions 13", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[6]))
        self.next_section("Conclusions 14", PresentationSectionType.NORMAL)
        self.play(FadeOut(title2), ReplacementTransform(blist2, t_thanks))
        self.wait(0.1)