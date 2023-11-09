from cytools import Polytope

p = Polytope([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0],[-1,-1,-1,-1]])
t = p.triangulate()
cy = t.get_cy()

int_nums = cy.intersection_numbers()
kahler_cone = cy.toric_kahler_cone()

cy_vol = cy.compute_cy_volume(kahler_cone.tip_of_stretched_cone(1))