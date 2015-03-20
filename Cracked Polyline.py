import rhinoscriptsyntax as rs
import Rhino

## "import Rhino" imports lower level Rhino Common. It consist of a whole namespace of classes.
## Google Rhino Common SDK for more info

###CRACK Polygon

def crackpolygon(polylines, count):
    newPolylines = []
    if count == > maxGen:
        return 

    for polyline in polylines:
       if rs.CloseCurve (pl) == False:
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
                    pts.append(pt1)
                    pts.append(pt2)
                    pts.append(centpt)
                    pts.append(pt1)
                    newpl = rs.AddPolyline(pts)
                    pls.append(newpl)
                    rs.DeleteObject(crv)

                rs.DeleteObjects(cleanup)
        return crackpolygon(pls, count + 1)
 
maxGen = rs.GetInteger("How many iterations would you like to do?", 3)
pl = rs.GetCurveObject("pick a closed curve to crack")
plguid = pl[0]
polygons = []
polygons.append(plguid)
crackpolygon(polygons, 0)
    