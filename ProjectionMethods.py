import math
import numpy as np
from classes import PointCloud


def ProjectionMethod(nuage: PointCloud):
    """
    Méthode 2 : Projection de tous les points sur un segment aléatoire
    """
    coords = np.array(list(nuage.List_points.values()), dtype="float")

    
    # Prendre les deux premiers points comme segment de référence
    x1, y1 = coords[0][0], coords[0][1]
    x2, y2 = coords[1][0], coords[1][1]
    
    dx, dy = x2 - x1, y2 - y1
    dist_sq = dx**2 + dy**2

    
    projections = []
    for px, py in coords:
        t = ((px - x1) * dx + (py - y1) * dy) / dist_sq
        t_clamped = max(0, min(1, t))
        proj_x = x1 + t_clamped * dx 
        proj_y = y1 + t_clamped * dy
        projections.append((proj_x, proj_y))
    
    if projections:
        n_p = len(projections)
        center = (
            sum(p[0] for p in projections) / n_p,
            sum(p[1] for p in projections) / n_p
        )
        print(f"Méthode 2 - Centre calculé : {center}")
        nuage.drawSinglePoint(center[0], center[1], "orange")
