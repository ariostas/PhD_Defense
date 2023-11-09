from manim import *
from manim_editor import PresentationSectionType

class MirrorSymmetry(Scene):
    def construct(self):
        
        title = Title(r"Mirror Symmetry is a profound duality", font_size=50)
        
        t2a = Tex(r"IIA", font_size=40).next_to(title, DOWN, buff=0.3).shift(LEFT*3)
        t2b = Tex(r"IIB", font_size=40).next_to(title, DOWN, buff=0.3).shift(RIGHT*3)
        t_compactify = Tex("compactify", font_size=40).next_to(title, DOWN, buff=1.3)
        t_mirror = Tex("mirror CYs", font_size=40).next_to(title, DOWN, buff=3)
        t_physics = Tex("same physics", font_size=40).to_edge(DOWN, buff=1.5)
        
        t_moduli = Tex(r"\begin{align*}\text{K\"ahler moduli space} &\leftrightarrow \text{Complex structure moduli space}\\\text{Complex structure moduli space} &\leftrightarrow \text{K\"ahler moduli space}\end{align*}", font_size=40)
        t_moduli.to_edge(DOWN, buff=0.2)
        
        cy1 = ImageMobject("images/CY_image.png")
        cy1.scale_to_fit_height(2.5)
        cy1.next_to(t2a, DOWN, buff=1.5)
        
        cy2 = ImageMobject("images/CY_image2.png")
        cy2.scale_to_fit_height(2.5)
        cy2.next_to(t2b, DOWN, buff=1.5)
        
        a1 = Arrow(start=t2a.get_center()+DOWN*t2a.height/2, end=cy1.get_center()+UP*cy1.height/2)
        a2 = Arrow(start=t2b.get_center()+DOWN*t2b.height/2, end=cy2.get_center()+UP*cy2.height/2)
        
        a3 = Arrow(start=cy1.get_center()+RIGHT*cy1.width/2, end=t_physics.get_center()+UP*t_physics.height/2)
        a4 = Arrow(start=cy2.get_center()+LEFT*cy2.width/2, end=t_physics.get_center()+UP*t_physics.height/2)
        
        blist1 = BulletedList(
            "It's an exceptionally suprising and useful duality.",
            r"Allows us to compute quantum effects by doing classical\\computations on the mirror side.",
            r"In this talk, we will only focus on using it to compute\\Gopakumar-Vafa (GV) invariants.",
            r"GV invariants are associated with effective curve classes of the CY.",
            r"They convey deep information about the geometry, about the\\number of certain BPS states, and about non-perturbative\\contributions to the EFT.",
            font_size=40,
        ).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        title2 = Title(r"Advancements in computing GV invariants", font_size=50)
        
        blist2 = BulletedList(
            r"Hosono, Klemm, Theisen, Yau (HKTY) '93 proposed a procedure\\to compute GV invariants for this kind of CYs.",
            r"Klemm and Kreuzer wrote an implementation in Mathematica,\\but it is very limited.",
            r"We have made improvements in the following aspects:",
            font_size=40,
        ).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        blist3 = BulletedList(
            r"Generalized to be applicable at large $h^{1,1}$.",
            r"Wrote a much faster implementation in C++.",
            r"Devised tricks to compute GV invariants at large $h^{1,1}$.",
            font_size=40,
            dot_scale_factor=1.5,
        ).next_to(blist2, DOWN, buff=0.4).to_edge(LEFT, buff=2)
        
        # This is for the image showing the Mori cone and GVs
        title3 = Title(r"How are GV invariants arranged?", font_size=50)
        mori_pts = []
        for x in range(11):
            for y in range(11):
                if y <= 3*x:
                    mori_pts.append((x,y))
        mori_pts.sort(key=lambda p: (p[0]+p[1],p[1],p[0]))
        nz_pts = [(1,3),(1,2)]
        for x in range(11):
            for y in range(11):
                if y <= 1*x and x:
                    nz_pts.append((x,y))
        axes0 = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5,
            y_length=5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            tips=False,
        ).shift(DOWN*0.2).to_edge(LEFT, buff=3).set_z_index(5)
        y_label0 = axes0.get_y_axis_label(Tex(r"$\mathcal{C}_2$").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.4)
        x_label0 = axes0.get_x_axis_label(Tex(r"$\mathcal{C}_1$"), edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels0 = VGroup(x_label0, y_label0).set_z_index(5)
        dots_eff = [Dot(point=axes0.c2p(*pt)).set_z_index(10) for pt in mori_pts]
        anims_nz = [dots_eff[mori_pts.index(pt)].animate.set_color(PURE_RED) for pt in nz_pts]
        gen1 = Line(start=axes0.c2p(0,0), end=axes0.c2p(10/3, 10), color=BLUE).set_z_index(6)
        gen2 = Line(start=axes0.c2p(0,0), end=axes0.c2p(10,0), color=BLUE).set_z_index(6)
        m_cone = Polygon(axes0.c2p(0,0), axes0.c2p(10,0), axes0.c2p(10,10), axes0.c2p(10/3, 10), stroke_opacity=0, fill_opacity=0.5, fill_color=BLUE)
        t_m_cone = Tex(r"$\mathcal{M}_X$", font_size=35).move_to(axes0.c2p(1.5,9))
        t_eff = Tex("Effective curves", font_size=40).to_edge(RIGHT, buff=1).to_edge(UP, buff=2)
        dot_eff = Dot().next_to(t_eff, LEFT, buff=0.2)
        dot_nz = Dot(color=PURE_RED).next_to(dot_eff, DOWN, buff=0.5)
        t_nz = Tex("Non-zero GVs", font_size=40).next_to(dot_nz, RIGHT, buff=0.2)
        t_potent = Tex(r"Potent rays:\\$\infty$ non-zero GVs", font_size=40).to_edge(RIGHT, buff=1)
        t_nilpotent = Tex(r"Nilpotent rays:\\finite non-zero GVs", font_size=40).next_to(t_potent, DOWN, buff=0.5)
        t_trick = Tex(r"Computing a particular\\GV invariant only require\\information in its\\``past light cone''", font_size=30)
        t_trick.next_to(t_nilpotent, DOWN, buff=0.6).to_edge(RIGHT, buff=1)
        m_cone_past = Polygon(axes0.c2p(0,0), axes0.c2p(-10,0), axes0.c2p(-10,-10), axes0.c2p(-10/3, -10), stroke_opacity=0, fill_opacity=0.5, fill_color=RED)
        
        # This is for the timing plots
        title4 = Title(r"Performance comparison at $h^{1,1}=2$", font_size=50)
        axes1 = Axes(
            x_range=[0, 200, 50],
            y_range=[-3, 5, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN, "numbers_to_include": range(0, 201, 50)},
            y_axis_config={"numbers_to_include": range(-6, 11, 2), "numbers_to_exclude": [], "exclude_origin_tick": False, "scaling": LogBase()},
            tips=False,
        ).shift(DOWN*0.2)
        y_label1 = axes1.get_y_axis_label(Tex("Time (s)").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.4)
        x_label1 = axes1.get_x_axis_label(Tex("Degree"), edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels1 = VGroup(x_label1, y_label1)
        with open("data/timings_GVcode.txt", "r") as f:
            gv_timings_ours = np.array([eval(l) for l in f.readlines()])
        with open("data/timings_inst_klemm.txt", "r") as f:
            gv_timings_k = np.array([eval(l) for l in f.readlines()])
        with open("data/timings_inst_klemm_kreuzer.txt", "r") as f:
            gv_timings_kk = np.array([eval(l) for l in f.readlines()])
        plot1 = axes1.plot_line_graph(x_values=gv_timings_k[:,0], y_values=gv_timings_k[:,1], line_color=BLUE, add_vertex_dots=False)
        plot2 = axes1.plot_line_graph(x_values=gv_timings_kk[:,0], y_values=gv_timings_kk[:,1], line_color=ORANGE, add_vertex_dots=False)
        plot3 = axes1.plot_line_graph(x_values=gv_timings_ours[:,0], y_values=gv_timings_ours[:,1], line_color=PURE_GREEN, add_vertex_dots=False)
        t_plot1 = Tex(r"Klemm", color=BLUE, font_size=40).move_to(axes1.c2p(25, 1e5))
        t_plot2 = Tex(r"Klemm+Kreuzer", color=ORANGE, font_size=40).move_to(axes1.c2p(70, 1e4))
        t_plot3 = Tex(r"Our code", color=PURE_GREEN, font_size=40).move_to(axes1.c2p(200, 1e3))
        
        # this is for the cone comparison
        axes2 = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 200, 50],
            x_length=5.5,
            y_length=5.5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            tips=False,
        ).shift(DOWN*0.3).to_edge(LEFT, buff=1.5).set_z_index(5)
        y_label2 = axes2.get_y_axis_label(Tex(r"$\mathcal{C}_2$").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.2)
        x_label2 = axes2.get_x_axis_label(Tex(r"$\mathcal{C}_1$"), edge=RIGHT, direction=DOWN, buff=0.2).shift(RIGHT*0.5)
        plot_labels2 = VGroup(x_label2, y_label2)
        pts_comp = []
        with open("data/11169_output_200.txt", "r") as f:
            for l in f.readlines():
                dd = eval(l)
                pts_comp.append(list(dd[0]))
        pts_comp.sort(key=lambda p: (p[0]+p[1],p[1],p[0]))
        pts_new = [pt for pt in pts_comp if pt[0]+pt[1]>30]
        pts_klemm = [pt for pt in pts_comp if pt[0]+pt[1]<=24]
        pts_klemmkreuzer = [pt for pt in pts_comp if 24<pt[0]+pt[1]<=30]
        dots_new = [Dot(point=axes2.c2p(*pt), color=PURE_GREEN, radius=0.01) for pt in pts_new]
        dots_kk = [Dot(point=axes2.c2p(*pt), color=ORANGE, radius=0.01) for pt in pts_klemmkreuzer]
        dots_k = [Dot(point=axes2.c2p(*pt), color=BLUE, radius=0.01) for pt in pts_klemm]
        with open("latex/large_gv.txt", "r") as f:
            large_gv_str = f.read()
        large_gv = Tex(large_gv_str, font_size=20).to_edge(RIGHT, buff=1).shift(UP*1.2)
        gv_arrow = Arrow(start=large_gv.get_center()+UP*(large_gv.height/2-0.2)+LEFT*large_gv.width/2, end=axes2.c2p(43,157))
        t_k = Tex(r"Klemm", color=BLUE, font_size=40).to_edge(RIGHT, buff=2.5).to_edge(DOWN, buff=1)
        t_kk = Tex(r"Klemm+Kreuzer", color=ORANGE, font_size=40).next_to(t_k, UP, buff=0.7)
        t_new = Tex(r"Our code", color=PURE_GREEN, font_size=40).next_to(t_kk, UP, buff=0.7)
        
        # This is for the info at large h11
        title5 = Title(r"Computing GVs at large $h^{1,1}$", font_size=50)
        blist4 = BulletedList(
            r"We are able to compute GV invariants at much higher $h^{1,1}$ than\\anyone before.",
            r"As an example, for the mirror quintic ($h^{1,1}=101$) we did the\\computation with 360,378,676 curves, and found 2,500 non-zero\\GV invariants.",
            r"Our algorithm works even at $h^{1,1}=491$.",
            r"With the techniques we developed we can compute GVs far along\\some potent rays at large $h^{1,1}$.",
            font_size=40,
        ).next_to(title5, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        
        # Finally, the ourline part
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
        blist_out.fade_all_but(4, opacity=0.25)
        
        self.next_section("MirrorSymmetry 0", PresentationSectionType.NORMAL)
        self.play(Write(title))
        self.next_section("MirrorSymmetry 1", PresentationSectionType.NORMAL)
        self.play(Write(t2a), Write(t2b))
        self.next_section("MirrorSymmetry 2", PresentationSectionType.NORMAL)
        self.play(Create(a1), Create(a2), FadeIn(t_compactify))
        self.play(FadeIn(cy1), FadeIn(cy2))
        self.next_section("MirrorSymmetry 3", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_physics), Create(a3), Create(a4))
        self.next_section("MirrorSymmetry 4", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_mirror))
        self.next_section("MirrorSymmetry 5", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_moduli))
        self.next_section("MirrorSymmetry 6", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [t2a,t2b,a1,a2,a3,a4,cy1,cy2,t_physics,t_mirror,t_moduli,t_compactify]])
        self.play(FadeIn(blist1.submobjects[0]))
        self.next_section("MirrorSymmetry 7", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[1]))
        self.next_section("MirrorSymmetry 8", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[2]))
        self.next_section("MirrorSymmetry 9", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[3]))
        self.next_section("MirrorSymmetry 10", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist1.submobjects[4]))
        self.next_section("MirrorSymmetry 11", PresentationSectionType.NORMAL)
        self.play(FadeOut(blist1), ReplacementTransform(title, title2))
        self.play(FadeIn(blist2.submobjects[0]))
        self.next_section("MirrorSymmetry 12", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[1]))
        self.next_section("MirrorSymmetry 13", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist2.submobjects[2]))
        self.next_section("MirrorSymmetry 14", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist3))
        self.next_section("MirrorSymmetry 15", PresentationSectionType.NORMAL)
        self.play(FadeOut(blist2), FadeOut(blist3))
        self.play(Create(axes0), Write(plot_labels0), Write(t_m_cone), Create(gen1), Create(gen2), FadeIn(m_cone), Create(dot_eff), Write(t_eff),
                 AnimationGroup(*[Create(d) for d in dots_eff], lag_ratio=0.05, run_time=1), ReplacementTransform(title2, title3))
        self.next_section("MirrorSymmetry 16", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*anims_nz, lag_ratio=0.05, run_time=1), Create(dot_nz), Write(t_nz))
        self.next_section("MirrorSymmetry 17", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_potent), FadeIn(t_nilpotent))
        self.next_section("MirrorSymmetry 18", PresentationSectionType.NORMAL)
        self.play(FadeIn(t_trick))
        self.next_section("MirrorSymmetry 19", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(m_cone.copy(), m_cone_past))
        self.next_section("MirrorSymmetry 20", PresentationSectionType.NORMAL)
        self.play(m_cone_past.animate.shift(axes0.c2p(5,5)-axes0.c2p(0,0)))
        self.next_section("MirrorSymmetry 21", PresentationSectionType.NORMAL)
        self.play(m_cone_past.animate.shift(axes0.c2p(0,-5)-axes0.c2p(0,0)))
        self.next_section("MirrorSymmetry 22", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [axes0, plot_labels0, t_m_cone, gen1, gen2, m_cone, dot_eff, t_eff, dot_nz, t_nz, t_potent, t_nilpotent, t_trick, m_cone_past]+dots_eff])
        self.play(ReplacementTransform(title3, title4), Create(axes1), Write(plot_labels1))
        self.next_section("MirrorSymmetry 23", PresentationSectionType.NORMAL)
        self.play(Create(plot1), Write(t_plot1))
        self.next_section("MirrorSymmetry 24", PresentationSectionType.NORMAL)
        self.play(Create(plot2), Write(t_plot2))
        self.next_section("MirrorSymmetry 25", PresentationSectionType.NORMAL)
        self.play(Create(plot3), Write(t_plot3))
        self.next_section("MirrorSymmetry 26", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [plot1, plot2, plot3, t_plot1, t_plot2, t_plot3]])
        self.play(ReplacementTransform(axes1, axes2), ReplacementTransform(plot_labels1, plot_labels2))
        self.next_section("MirrorSymmetry 27", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(d) for d in dots_k], lag_ratio=0.05, run_time=1), Write(t_k))
        self.next_section("MirrorSymmetry 28", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(d) for d in dots_kk], lag_ratio=0.05, run_time=1), Write(t_kk))
        self.next_section("MirrorSymmetry 29", PresentationSectionType.NORMAL)
        self.play(AnimationGroup(*[Create(d) for d in dots_new], lag_ratio=0.05, run_time=1), Write(t_new))
        self.wait(0.1)
        self.next_section("MirrorSymmetry 30", PresentationSectionType.NORMAL)
        self.play(Write(large_gv), Create(gv_arrow))
        self.next_section("MirrorSymmetry 31", PresentationSectionType.NORMAL)
        self.play(*[FadeOut(o) for o in [axes2,plot_labels2, t_k, t_kk, t_new,large_gv,gv_arrow]+dots_k+dots_kk+dots_new])
        self.play(ReplacementTransform(title4, title5), FadeIn(blist4.submobjects[0]))
        self.next_section("MirrorSymmetry 32", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist4.submobjects[1]))
        self.next_section("MirrorSymmetry 33", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist4.submobjects[2]))
        self.next_section("MirrorSymmetry 34", PresentationSectionType.NORMAL)
        self.play(FadeIn(blist4.submobjects[3]))
        self.next_section("MirrorSymmetry 35", PresentationSectionType.NORMAL)
        self.play(ReplacementTransform(blist4, blist_out), ReplacementTransform(title5, title_out))
        self.next_section("MirrorSymmetry 36", PresentationSectionType.SKIP)
        self.play(FadeOut(title_out), FadeOut(blist_out))