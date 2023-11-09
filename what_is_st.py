from manim import *
from manim_editor import PresentationSectionType

class WhatIsST(Scene):
    def construct(self):
        
        title = Title(r"What is string theory?", font_size=45)
        
        t1 = Tex(r"Basic idea: the fundamental objects are strings, not point particles.", font_size=35).next_to(title, DOWN, buff=0.5)
        
        particle = Dot(color=PURE_RED).shift(LEFT*4 + UP*0.5)
        
        arrow = Arrow(start=LEFT, end=RIGHT).next_to(particle, RIGHT, buff=1)
        
        w_xshift = -0.7
        w_yshift = 0.4
        def wave_func(t, a):
            return np.array((t*0.4+w_xshift, a*np.sin(3 * t)+w_yshift, 0))
        wave = ParametricFunction(lambda t: wave_func(t, 0.4), t_range = np.array([0, TAU]), fill_opacity=0).set_color(PURE_RED)
        
        radius = 1
        c_xshift = 4
        c_yshift = 0.4
        def wavy_circ_func(t, a):
            return np.array((np.cos(t)*(radius+a*np.sin(3*t))+c_xshift, np.sin(t)*(radius+a*np.sin(3*t))+c_yshift, 0))
        circ = ParametricFunction(lambda t: wavy_circ_func(t, 0.3), t_range = np.array([0, TAU]), fill_opacity=0).set_color(PURE_RED)
        
        blist = BulletedList(
            "It's a simple idea, but with very profound consequences.",
            "Entails the existence of other extended objects, requires supersymmetry, enforces the presence of gravity, and predicts a 10D spacetime.",
            "Extremely rich, but very difficult to study.",
            font_size=35,
        ).next_to(circ, DOWN, buff=0.2).to_edge(LEFT, buff=1)
        
        self.next_section("What is ST 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("What is ST 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(t1))
        self.next_section("What is ST 2", PresentationSectionType.SKIP)
        self.play(Create(particle))
        self.play(Create(arrow))
        part1 = particle.copy()
        part2 = particle.copy()
        self.play(ReplacementTransform(part1, wave), ReplacementTransform(part2, circ))
        self.next_section("What is ST 3", PresentationSectionType.COMPLETE_LOOP)
        for tt in np.arange(0,2, 0.1):
            new_wave = ParametricFunction(lambda t: wave_func(t, 0.4*np.cos(tt*np.pi)), t_range = np.array([0, TAU]), fill_opacity=0).set_color(PURE_RED)
            new_circ = ParametricFunction(lambda t: wavy_circ_func(t, 0.3*np.cos(tt*np.pi)), t_range = np.array([0, TAU]), fill_opacity=0).set_color(PURE_RED)
            self.play(ReplacementTransform(wave, new_wave, rate_func=rate_functions.linear),
                      ReplacementTransform(circ, new_circ, rate_func=rate_functions.linear), run_time=0.1)
            wave = new_wave
            circ = new_circ
        self.next_section("What is ST 4", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[0]))
        self.next_section("What is ST 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[1]))
        self.next_section("What is ST 6", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[2]))
        self.next_section("What is ST 7", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [title, particle, arrow, wave, circ, t1, blist]])
