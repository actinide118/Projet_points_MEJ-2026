from classes import *

def baricentre(points : PointCloud):
    CouplePoint = {}
    Baricentre = {}
    point_list = list(points.List_points.keys())
    
    for i in range(0, len(point_list) - 1, 2):
        p = point_list[i]
        p_next = point_list[i + 1]
        
        if p not in CouplePoint:
            points1X = p.position[0]
            points1Y = p.position[1]
            CouplePoint[p] = (points1X, points1Y)

            points2X = p_next.position[0]
            points2Y = p_next.position[1]

            CouplePoint[p_next] = (points2X, points2Y)

            if points1X > points2X:
                MiddlePointX = (points1X - points2X)
            elif points2X > points1X:
                MiddlePointX = (points2X - points1X)
            if points1Y > points2Y:
                MiddlePointY = (points1Y - points2Y)
            elif points2Y > points1Y:
                MiddlePointY = (points2Y - points1Y)
            Baricentre[p] = (MiddlePointX, MiddlePointY)
 

    CouplePoint.clear()

    while len(Baricentre) != 1:
        baricentre_keys = list(Baricentre.keys())
        for i in range(0, len(baricentre_keys) - 1, 2):
            point1 = baricentre_keys[i]
            point2 = baricentre_keys[i + 1]           
            if i not in Baricentre:
                points1X_baricentre = Baricentre[point1][0]
                points1Y_baricentre = Baricentre[point1][1]
                CouplePoint[point1] = (points1X_baricentre, points1Y_baricentre)
                points2X_baricentre = Baricentre[point2][0]
                points2Y_baricentre = Baricentre[point2][1]
                CouplePoint[point2] = (points2X_baricentre, points2Y_baricentre)

                if points1X_baricentre > points2X_baricentre:
                    MiddlePoint_baricentreX = (points1X_baricentre - points2X_baricentre)
                else:
                    MiddlePoint_baricentreX = (points2X_baricentre - points1X_baricentre)

                if points1Y_baricentre > points2Y_baricentre:
                    MiddlePoint_baricentreY = (points1Y_baricentre - points2Y_baricentre)
                else:
                    MiddlePoint_baricentreY = (points2Y_baricentre - points1Y_baricentre)
                MiddlePoint_baricentre = (MiddlePoint_baricentreX, MiddlePoint_baricentreY)

                print(MiddlePoint_baricentre)
                del Baricentre[point1]
                if point2 in Baricentre:
                    del Baricentre[point2]
                Baricentre[-1] = MiddlePoint_baricentre


    final_baricentre_coords = list(Baricentre.values())[0]
    points.drawSinglePoint(final_baricentre_coords[0], final_baricentre_coords[1], "blue")
    print(final_baricentre_coords[0])
    print(final_baricentre_coords[1])
    return
            
                

    
