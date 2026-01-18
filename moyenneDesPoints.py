from classes import *
def Moyenne(nuage: PointCloud):
    moyenne_x = 0
    moyenne_y =0
    for i in nuage.List_points:
        moyenne_x += i.position[0]
        moyenne_y += i.position[1]
    moyenne_x = moyenne_x/ len(nuage.List_points)
    moyenne_y = moyenne_y/ len(nuage.List_points)
    nuage.drawSinglePoint(moyenne_x, moyenne_y ,"green")
