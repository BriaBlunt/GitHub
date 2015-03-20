import rhinoscriptsyntax as rs
import Rhino

## "import Rhino" imports lower level Rhino Common. It consist of a whole namespace of classes.
## Google Rhino Common SDK for more info


###CRACK Polygon

def crackpolygon(polylines, count, maxGen, attrPts):
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
                newpl = rs.AddPolyline(pts)
                
                addCurve = False
                for pt in attrPts:
                    if isPointInCurve(pt, newpl) :
                        addCurve = True
                    if addCurve :
                        newPolyline.append(newpl)

                p = rs.AddPolyline(pts)
                newPolylines.append(p)
                rs.DeleteObject(crv)
                rs.DeleteObjects(centpt)
    return crackpolygon(newPolylines, count + 1, maxGen)


def isPointInCurve (pt, curve):
    curve = rs.coercecurve(curve)
    rc = curve.Contains(pt)
    
    if rc == Rhino.Geometry.PointContainment
       return False
    else
        return True
        
    return curve.Contains(pts)
    endPt = rs.PointAdd(pt,[10000000, 0, 0])
    tempLine = Rhino.Geometry.Curve(pt, endPt)
    intercesctions = rs.CurveCurveIntersection (curve, tempLine)
    if len(intersections)%2 == 0:
        return false
    else:
        return true
    

def main():
    attrPts = rs.GetPoints("select attractor Pts)
    maxGen = rs.GetInteger("How many iterations would you like to do?", 3)
    polyline = rs.GetCurveObject("pick a closed curve to crack")
    polylineGuid = polyline[0]
    polygons = []
    polygons.append(polylineGuid)
    crackpolygon(polygons, 0, maxGen)

if __name__ == "__main__" :
    main()