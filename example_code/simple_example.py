from cytools import Polytope

p = Polytope([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0],[-1,-1,-1,-1]])
t = p.triangulate()
cy = t.get_cy()