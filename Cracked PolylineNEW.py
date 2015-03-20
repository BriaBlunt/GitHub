import rhinoscriptsyntax as rs
import Rhino

## "import Rhino" imports lower level Rhino Common. It consist of a whole namespace of classes.
## Google Rhino Common SDK for more info

###CRACK Polygon

def crackpolygon(polylines, count, maxGen):
    newPolylines = []
    if count > maxGen:
        return 

    for polyline in polylines:
       if rs.CloseCurve (polyline) == False:
            print "Not a closed curve"
       else:
           centroid = rs.CurveAreaCentroid(polyline)
           centpt = rs.AddPoint(centroid[0])
           curves = rs.ExplodeCurves(polyline)
           for crv in curves:
                    #print crv
                ptl = rs.CurveStartPoint(crv)
                pt2 = rs.CurveEndPoint(crv)
                pts = []
                pts.append(rs.CurveStartPoint(crv))
                pts.append(rs.CurveEndPoint(crv))
                pts.append(centroid[0])
                pts.append(rs.CurveStartPoint(crv))
                p = rs.AddPolyline(pts)
                newPolylines.append(p)
                rs.DeleteObject(crv)
                rs.DeleteObjects(centpt)
    return crackpolygon(newPolylines, count + 1, maxGen)

def main():
    maxGen = rs.GetInteger("How many iterations would you like to do?", 3)
    polyline = rs.GetCurveObject("pick a closed curve to crack")
    polylineGuid = polyline[0]
    polygons = []
    polygons.append(polylineGuid)
    crackpolygon(polygons, 0, maxGen)

if __name__ == "__main__" :
    main()