from classes import *

def baricentre(points: PointCloud):
    CouplePoint = {}
    Baricentre = {}
    point_list = list(points.List_points.keys())

    # --- ROUND 1: pair up the original points ---
    for i in range(0, len(point_list), 2):
        if i + 1 >= len(point_list):  # odd point, carry forward with weight 1
            Baricentre[point_list[i]] = (point_list[i].position[0], point_list[i].position[1], 1)
            continue

        p = point_list[i]
        p_next = point_list[i + 1]

        if p not in CouplePoint:
            points1X = p.position[0]
            points1Y = p.position[1]
            CouplePoint[p] = (points1X, points1Y)

            points2X = p_next.position[0]
            points2Y = p_next.position[1]
            CouplePoint[p_next] = (points2X, points2Y)

            MiddlePointX = (points1X + points2X) / 2
            MiddlePointY = (points1Y + points2Y) / 2
            Baricentre[p] = (MiddlePointX, MiddlePointY, 2)  # weight 2 because 2 points merged

    CouplePoint.clear()

    # --- SUBSEQUENT ROUNDS ---
    while len(Baricentre) != 1:
        baricentre_keys = list(Baricentre.keys())

        for i in range(0, len(baricentre_keys), 2):
            if i + 1 >= len(baricentre_keys):  # odd point, already has its weight, just skip
                continue

            point1 = baricentre_keys[i]
            point2 = baricentre_keys[i + 1]

            if point1 in Baricentre and point2 in Baricentre:
                points1X_baricentre = Baricentre[point1][0]
                points1Y_baricentre = Baricentre[point1][1]
                p1 = Baricentre[point1][2]  # weight of point1

                points2X_baricentre = Baricentre[point2][0]
                points2Y_baricentre = Baricentre[point2][1]
                p2 = Baricentre[point2][2]  # weight of point2

                total_poids = p1 + p2

                MiddlePoint_baricentreX = (points1X_baricentre * p1 + points2X_baricentre * p2) / total_poids
                MiddlePoint_baricentreY = (points1Y_baricentre * p1 + points2Y_baricentre * p2) / total_poids

                del Baricentre[point1]
                if point2 in Baricentre:
                    del Baricentre[point2]
                Baricentre[point1] = (MiddlePoint_baricentreX, MiddlePoint_baricentreY, total_poids)

    # --- DRAW the final barycenter in blue ---
    final_baricentre_coords = list(Baricentre.values())[0]
    points.drawSinglePoint(final_baricentre_coords[0], final_baricentre_coords[1], "blue")
    return final_baricentre_coords[0], final_baricentre_coords[1]