# Projet pour Math en Jeans 2026
# 2 Objectif
#
# n°1 : Lire coordonnées prédifinie dans un tableau excele et l'afficher dans une fenêtre graphique 
# puis placer le centre à l'aide des méthodes
# n°2 : Placement aléatoire de points selon les paramètres donnéss
#
#
# utilisation de libary : 
# simplegraphics-python et openpyxl
#

import openpyxl
import SimpleGraphics





# initialisation #

tableau_excel = "Coordonnées_points.xlsx"


wb = openpyxl.Workbook()
File = openpyxl.load_workbook(tableau_excel)
Sheet = File.active



List_points = {} 


class Point:
    def __init__(self, x, y):
        self.x = x # Position en x
        self.y = y # Position en y

    def draw(self):     
        for row in Sheet.iter_rows(min_row=2, values_only=True):
            x_coord = row[0]
            y_coord = row[1]
            SimpleGraphics.draw_circle(x_coord, y_coord, 5, fill='red')



SimpleGraphics.resize(1200, 900)

point = Point(400, 400)
point.draw()