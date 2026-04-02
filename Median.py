import classes
from classes import *

def Median(nuage: classes.PointCloud):  
    if not nuage.List_points:
        print("Aucun point dans le nuage.")
        return

    x_coords = sorted(p.position[0] for p in nuage.List_points.keys())
    y_coords = sorted(p.position[1] for p in nuage.List_points.keys())

    n = len(x_coords)
    median_x = (x_coords[n // 2] + x_coords[(n - 1) // 2]) / 2
    median_y = (y_coords[n // 2] + y_coords[(n - 1) // 2]) / 2

    nuage.drawSinglePoint(median_x, median_y, "pink")
