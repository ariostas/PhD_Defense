from manim import *
from manim_editor import PresentationSectionType

class CYProperties(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        title = Title(r"Key Properties of Calabi-Yau threefolds", font_size=45)

        torus = Torus(major_radius=2, minor_radius=2/3).shift(UP*4+IN*1)
        torus2 = Torus(major_radius=1, minor_radius=1/3).shift(UP*4+IN*1)
        torus3 = Torus(major_radius=2.5, minor_radius=1/3).shift(UP*4+IN*1)
        
        blist = BulletedList(
            "Complex manifolds.",
            r"Have special holonomy $SU(3)$ and admit a Ricci flat metric.",
            r"Only two relevant Hodge numbers,",
            r"Moduli split into K\"ahler and\\Complex Structure moduli.",
            font_size=40,
        ).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        h_def = Tex(r"$h^{p,q}=\text{dim}H^{p,q}(X)$.", font_size=40).next_to(blist.submobjects[2], RIGHT, buff=0.2)
        h_rel = Tex("$h^{1,1}$ and $h^{2,1}$.", font_size=40).next_to(blist.submobjects[2], RIGHT, buff=0.2).shift(UP*0.1)
        
        mod_split = Tex(r"$\mathcal{M}(X)=\mathcal{M}_K(X)\times\mathcal{M}_{CS}(X)$", font_size=40).next_to(blist.submobjects[3], DOWN, buff=0.2).shift(RIGHT*0.3)
        
        ex1 = Tex(r"{{Torus analogy:}} K\"ahler modulus", font_size=35, color=TEAL).to_edge(DOWN, buff=0.1).to_edge(LEFT, buff=3.5)
        ex2 = Tex(r"{{Torus analogy:}} complex structure modulus", font_size=35, color=TEAL).to_edge(DOWN, buff=0.1).to_edge(LEFT, buff=3.5)
        
        with open("latex/hodge_diamond.txt", "r") as f:
            hodge_diamond_str = f.read()
        hodge_diamond = Tex(hodge_diamond_str).scale_to_fit_height(3).next_to(blist.submobjects[2], DOWN)
        hodge_diamond.shift(LEFT*hodge_diamond.get_center()[0])
        with open("latex/hodge_diamond_full.txt", "r") as f:
            hodge_diamond_full_str = f.read()
        hodge_diamond_full = Tex(hodge_diamond_full_str).scale_to_fit_height(3).next_to(blist.submobjects[2], DOWN)
        hodge_diamond_full.shift(LEFT*hodge_diamond_full.get_center()[0])
        
        m_dims = Tex(r"\begin{align*}\text{dim}(\mathcal{M}_K)&=h^{1,1}\\\text{dim}(\mathcal{M}_{CS})&=h^{2,1}\end{align*}", font_size=40).next_to(blist.submobjects[3], RIGHT)
        m_dims.to_edge(RIGHT, buff=2).shift(DOWN*0.5)
        
        tt = Tex(r"The Hodge numbers determine the number of fields in the EFT\\and the complexity of the computations.", font_size=40).to_edge(DOWN, buff=1)
        box = Rectangle(
            height=tt.height+0.2, width=tt.width+0.2,
            fill_opacity=0, stroke_color=PURE_RED,
        ).move_to(tt.get_center())
        
        self.add_fixed_in_frame_mobjects(title, blist, hodge_diamond, hodge_diamond_full, h_def, h_rel, mod_split, ex1, ex2, tt, box, m_dims)
        self.remove(title, blist, hodge_diamond, hodge_diamond_full, h_def, h_rel, mod_split, ex1, ex2, tt, box, m_dims)
        
        self.next_section("CYProperties 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("CYProperties 1", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[0]))
        self.next_section("CYProperties 2", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[1]))
        self.next_section("CYProperties 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist.submobjects[2]), FadeIn(h_def))
        self.play(Write(hodge_diamond_full, run_time=0.5))
        self.next_section("CYProperties 4", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(hodge_diamond_full, hodge_diamond), ReplacementTransform(h_def, h_rel))
        self.next_section("CYProperties 5", PresentationSectionType.NORMAL)
        self.play(FadeOut(hodge_diamond))
        self.play(FadeIn(blist.submobjects[3]))
        self.play(Write(mod_split))
        self.next_section("CYProperties 6", PresentationSectionType.SKIP)
        self.play(FadeIn(ex1))
        t1 = torus.copy()
        self.play(Create(t1))
        self.next_section("CYProperties 7", PresentationSectionType.COMPLETE_LOOP)
        t2 = torus2.copy()
        self.play(ReplacementTransform(t1, t2))
        t1 = torus.copy()
        self.play(ReplacementTransform(t2, t1))
        self.next_section("CYProperties 8", PresentationSectionType.SKIP)
        self.play(FadeOut(ex1), run_time=0.5)
        self.play(FadeIn(ex2), run_time=0.5)
        self.next_section("CYProperties 9", PresentationSectionType.COMPLETE_LOOP)
        self.play(ReplacementTransform(t1, torus3))
        self.play(ReplacementTransform(torus3, torus))
        self.next_section("CYProperties 10", PresentationSectionType.NORMAL)
        self.play(Uncreate(torus), FadeOut(ex2))
        self.play(FadeIn(m_dims))
        self.next_section("CYProperties 11", PresentationSectionType.NORMAL)
        self.play(FadeIn(tt), Create(box))
        self.next_section("CYProperties 12", PresentationSectionType.SKIP)
        self.play(*[FadeOut(o) for o in [title, blist, h_rel, mod_split, tt, box, m_dims]])