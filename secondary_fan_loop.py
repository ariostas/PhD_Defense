from manim import *
from manim_editor import PresentationSectionType

from scipy.spatial import ConvexHull

def get_real_simp(simp,pts):
    dim = len(pts[0])
    real_simp = []
    tmp_m = np.ones((dim,dim),dtype=int)
    for k,s in enumerate(simp):
        for i in range(len(s)):
            tmp_m[i,0:dim-1] = pts[s[i]][0:dim-1]
        if abs(np.linalg.det(tmp_m)) > 0.1 and len(pts)-1 not in s:
            real_simp.append(s)
    return np.array(sorted(sorted(s) for s in real_simp))

def triangulate(pts, heights):
    pts_ext = [list(pts[i])+[heights[i]] for i in range(len(pts))] + [[0,0,100]]
    hull = ConvexHull(pts_ext)
    simp = get_real_simp(hull.simplices,pts_ext)
    return simp

class SecondaryFanLoop(ThreeDScene):
    def construct(self):
        
        axes2d = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=5,
            y_length=5,
            tips=False,
        ).to_edge(LEFT)
        
        cone1 = AnnularSector(inner_radius=0, outer_radius=1.5, arc_center=axes2d.c2p(0,0), start_angle=0, angle=39.2*PI/180, fill_opacity=1, stroke_opacity=0, fill_color=GOLD)
        cone2 = AnnularSector(inner_radius=0, outer_radius=1.5, arc_center=axes2d.c2p(0,0), start_angle=39.2*PI/180, angle=(180-2*39.2)*PI/180, fill_opacity=1, stroke_opacity=0, fill_color=PURE_RED)
        cone3 = AnnularSector(inner_radius=0, outer_radius=1.5, arc_center=axes2d.c2p(0,0), start_angle=(180-39.2)*PI/180, angle=39.2*PI/180, fill_opacity=1, stroke_opacity=0, fill_color=PURE_GREEN)
        cone4 = AnnularSector(inner_radius=0, outer_radius=1.5, arc_center=axes2d.c2p(0,0), start_angle=PI, angle=PI/2, fill_opacity=1, stroke_opacity=0, fill_color=TEAL)
        cone5 = AnnularSector(inner_radius=0, outer_radius=1.5, arc_center=axes2d.c2p(0,0), start_angle=3*PI/2, angle=PI/2, fill_opacity=1, stroke_opacity=0, fill_color=PURPLE)
        self.add_fixed_in_frame_mobjects(axes2d, cone1, cone2, cone3, cone4, cone5)
        self.remove(axes2d)
        
        axes3d = ThreeDAxes(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            z_range=(-3, 3, 1),
            tips=False,
        ).shift(RIGHT*3 + IN*2)
        self.set_camera_orientation(theta=-100 * DEGREES, phi=75 * DEGREES, zoom=1)
        
        d_fan = Dot(point=axes2d.c2p(0,0), color=BLACK)
        self.lifttime = 1
        self.runtime = 5
        self.t_lift = 0
        self.t_anim = PI/2
        
        self.pts = [[0,0],[1,0],[1,2],[-1,2],[-1,0]]
        self.heights = 0.0004*np.array([0,1,-1,1,-1])
        self.curr_pts = [0,1,2,3,4]
        self.curr_lines = []
        
        def init_lift(mobj, dt):
            self.t_lift += dt/self.lifttime
            pt = [0, self.t_lift]
            mobj.move_to(axes2d.c2p(*pt))
            heights = (2*np.array([1,1,1,1,1])-0.4*np.array([1,-1,0,0,-1]))*self.t_lift
            self.heights = heights.tolist()
            simps = triangulate(self.pts, self.heights)
            self.curr_pts = list(set.union(*[set(s) for s in simps]))
            curr_lines = set()
            for s in simps:
                curr_lines.add((s[0],s[1]))
                curr_lines.add((s[0],s[2]))
                curr_lines.add((s[1],s[2]))
            self.curr_lines = [list(l) for l in curr_lines]
            
        def move_in_circle(mobj, dt):
            self.t_anim += 2*PI*dt/self.runtime
            pt = [np.cos(self.t_anim), np.sin(self.t_anim)]
            mobj.move_to(axes2d.c2p(*pt))
            heights = 2*np.array([1,1,1,1,1])+0.4*np.cos(self.t_anim)*np.array([0,1,-1,1,-1])-0.4*np.sin(self.t_anim)*np.array([1,-1,0,0,-1])
            self.heights = heights.tolist()
            simps = triangulate(self.pts, self.heights)
            self.curr_pts = list(set.union(*[set(s) for s in simps]))
            curr_lines = set()
            for s in simps:
                curr_lines.add((s[0],s[1]))
                curr_lines.add((s[0],s[2]))
                curr_lines.add((s[1],s[2]))
            self.curr_lines = [list(l) for l in curr_lines]
        
        def get_dot(coords):
            return Dot3D(point=axes3d.c2p(*coords), color=TEAL).set_z_index(20)
        
        def get_dots():
            dots = [get_dot(pt+[h]) for pt,h in zip(self.pts,self.heights)]
            if 0 not in self.curr_pts:
                dots[0].set_color(ORANGE)
            return VGroup(*dots).set_z_index(20)
        
        def get_proj_line(start, end):
            return Line3D(start=axes3d.c2p(*start), end=axes3d.c2p(*end), color=WHITE).set_z_index(1)
        
        def get_proj_lines():
            lines = [l for l in self.curr_lines if l not in [[0,1],[0,4],[1,2],[2,3],[3,4],[1,4]]]
            lines = [get_proj_line(self.pts[i]+[0], self.pts[j]+[0]) for i,j in lines]
            vg = VGroup(*lines)
            if self.t_lift < 0.99:
                vg.set_opacity(self.t_lift**4)
            return vg
        
        def get_vert_line(start, end):
            vg = Line3D(start=axes3d.c2p(*start), end=axes3d.c2p(*end), color=PURPLE, thickness=0.01)
            if self.t_lift < 0.99:
                vg.set_opacity(self.t_lift**4)
            return vg
        
        def get_vert_lines():
            lines = [get_vert_line(pt+[0], pt+[h]) for pt,h in zip(self.pts,self.heights)]
            vg = VGroup(*lines)
            if self.t_lift < 0.99:
                vg.set_opacity(self.t_lift**4)
            return vg
        
        def get_lifted_line(start, end):
            return Line3D(start=axes3d.c2p(*start), end=axes3d.c2p(*end), color=PURE_RED).set_z_index(5)
        
        def get_lifted_lines():
            lines = [get_lifted_line(self.pts[i]+[self.heights[i]], self.pts[j]+[self.heights[j]]) for i,j in self.curr_lines]
            vg = VGroup(*lines)
            if self.t_lift < 0.99:
                vg.set_opacity(self.t_lift**4)
            return vg
        
        poly_lines = [get_proj_line(self.pts[i]+[0], self.pts[j]+[0]) for i,j in [[1,2],[2,3],[3,4],[4,1]]]
        
        dots = always_redraw(get_dots)
        proj_lines = always_redraw(get_proj_lines)
        vert_lines = always_redraw(get_vert_lines)
        lifted_lines = always_redraw(get_lifted_lines)
        
        self.add_fixed_in_frame_mobjects(d_fan)
        self.remove(d_fan)
        
        self.t_lift = 1
        self.t_anim = PI/2
        heights = 2*np.array([1,1,1,1,1])+0.4*np.cos(self.t_anim)*np.array([0,1,-1,1,-1])-0.4*np.sin(self.t_anim)*np.array([1,-1,0,0,-1])
        self.heights = heights.tolist()
        simps = triangulate(self.pts, self.heights)
        self.curr_pts = list(set.union(*[set(s) for s in simps]))
        curr_lines = set()
        for s in simps:
            curr_lines.add((s[0],s[1]))
            curr_lines.add((s[0],s[2]))
            curr_lines.add((s[1],s[2]))
        self.curr_lines = [list(l) for l in curr_lines]
        dots = always_redraw(get_dots)
        proj_lines = always_redraw(get_proj_lines)
        vert_lines = always_redraw(get_vert_lines)
        lifted_lines = always_redraw(get_lifted_lines)
        self.add(d_fan, dots,*poly_lines,proj_lines, vert_lines, lifted_lines)
        self.next_section("SecondaryFan 2", PresentationSectionType.COMPLETE_LOOP)
        d_fan.add_updater(move_in_circle)
        self.wait(self.runtime)