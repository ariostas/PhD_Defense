from manim import *
from manim_editor import PresentationSectionType

class IntroQuestion(Scene):
    def construct(self):
        
        question = Title(r"How can we learn about quantum gravity?", font_size=45)
        
        blist1 = BulletedList(
            "Excluding what CANNOT happen. (Swampland Program)",
            "Constructing explicit models and seeing what CAN happen.",
            font_size=35,
        ).next_to(question, DOWN, buff=0.7).to_edge(LEFT, buff=1)
        
        box1 = Rectangle(
            height=blist1.submobjects[1].height+0.2, width=blist1.submobjects[1].width+0.2,
            fill_opacity=0, stroke_color=PURE_RED,
        ).move_to(blist1.submobjects[1].get_center())
        
        t0 = Tex(r"Looking at constructions we can ask questions such as", font_size=35).to_edge(LEFT, buff=1).shift(UP*1.3)
        blist2 = BulletedList(
            "How many (if any) axions should we expect to find in our universe?",
            "How can small cosmological constants arise?",
            "Are de Sitter vacua possible in string theory?",
            "Is string theory a viable option to describe our universe?",
            font_size=30,
        ).next_to(t0, DOWN, buff=0.2).to_edge(LEFT, buff=1)
        for i in range(1,4):
            blist2.submobjects[i].shift(UP*0.2*i)
        
        t1 = Tex(r"Answering these questions requires computational tools\\to construct and study solutions.", font_size=45).shift(DOWN*1.9)
        t2 = Tex(r"Today I will present new computational advancements\\that help us work towards answering these questions.", font_size=40).next_to(t1, DOWN, buff=0.3)
        box2 = Rectangle(
            height=t2.height+0.2, width=t2.width+0.2,
            fill_opacity=0, stroke_color=PURE_RED,
        ).move_to(t2.get_center())
        
        self.next_section("Intro 0", PresentationSectionType.NORMAL)
        self.play(Write(question))
        self.next_section("Intro 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[0]))
        self.next_section("Intro 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[1]))
        self.next_section("Intro 3", PresentationSectionType.NORMAL)
        self.play(Create(box1))
        self.next_section("Intro 4", PresentationSectionType.NORMAL)
        self.play(FadeOut(blist1.submobjects[0]), blist1.submobjects[1].animate.shift(UP), box1.animate.shift(UP))
        self.play(FadeIn(t0), FadeIn(blist2))
        self.next_section("Intro 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("Intro 6", PresentationSectionType.NORMAL)
        self.play(FadeIn(t2), FadeIn(box2))
        self.next_section("Intro 7", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [question, blist1.submobjects[1], box1, t0, blist2, t1, t2, box2]])