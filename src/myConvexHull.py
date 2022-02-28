import numpy as np

#Fungsi Convex Hull
def ConvexHull(points):
    left = []
    right = []
    det = 0
    detMax = 0
    detMin = 0
    add = []
    result = np.array([[]], dtype=int)

    #Mencari titik teratas dan terbawah
    top = np.append(points[0], [int(0)])
    bottom = np.append(points[0], [0])
    i = 0
    for point in points:
        if point[1] > top[1]:
            add = np.append(point, [int(i)])
            top = add
        if point[1] < bottom[1]:
            add = np.append(point, [i])
            bottom = add
        i += 1

    #Mengumpulkan titik-titik di bagian kiri dan kanan dari garis yang terbentuk dari titik teratas dan terbawah,
    #juga mencari titik terjauh di kiri dan kanan garis tersebut
    i = 0
    for point in points:
        if ((point[0] == top[0] and point[1] == top[1]) or (point[0] == bottom[0] and point[1] == bottom[1])):
            pass
        else:
            det = bottom[0]*top[1]+top[0]*point[1]+point[0]*bottom[1]-bottom[0]*point[1]-point[0]*top[1]-top[0]*bottom[1]
            if det > 0:
                add = np.append(point, [i])
                left.append(add)
                if det > detMax:
                    detMax = det
                    pointMax = add
            if det < 0:
                add = np.append(point, [i])
                right.append(add)
                if det < detMin:
                    detMin = det
                    pointMin = add
        i += 1

    #Mencari Convex Hull bagian kiri dan kanan
    result = ConvexHullLeft(pointMax, top, bottom, left)
    result = np.append(result, ConvexHullRight(pointMin, top, bottom, right), axis=0)
    return result


#Fungsi Convex Hull Bagian Kiri
def ConvexHullLeft(left, top, bottom, points):
    above = []
    below = []
    detMax = 0
    pointMaxAbove = []
    pointMaxBelow = []
    result = np.array([[]], dtype=int)

    #basis, membentuk garis convex hull
    if(len(points)==0):
        return(np.array([[top[2], bottom[2]]], dtype=int))
    if(len(points)==1):
        return(np.array([[top[2], left[2]], [left[2], bottom[2]]], dtype=int))
    else:
        
        #Mengumpulkan titik-titik di atas dari garis yang terbentuk dari titik teratas dan terjauh di kiri,
        #juga mencari titik terjauh yang diatas garis tersebut
        for point in points:
            if (point[0] == left[0] and point[1] == left[1]):
                pass
            else:
                det = left[0]*top[1]+top[0]*point[1]+point[0]*left[1]-left[0]*point[1]-point[0]*top[1]-top[0]*left[1]
                if det > 0:
                    above.append(point)
                    if det > detMax:
                        detMax = det
                        pointMaxAbove = point

        #Mengumpulkan titik-titik di bawah dari garis yang terbentuk dari titik terbawah dan terjauh di kiri,
        #juga mencari titik terjauh yang dibawah garis tersebut
        detMax = 0
        for point in points:
            if (point[0] == left[0] and point[1] == left[1]):
                pass
            else:
                det = bottom[0]*left[1]+left[0]*point[1]+point[0]*bottom[1]-bottom[0]*point[1]-point[0]*left[1]-left[0]*bottom[1]
                if det > 0:
                    below.append(point)
                    if det > detMax:
                        detMax = det
                        pointMaxBelow = point

        #Mencari titik convex hull lain
        result = ConvexHullLeft(pointMaxAbove, top, left, above)
        result = np.append(result, ConvexHullLeft(pointMaxBelow, left, bottom, below), axis=0)
        return result


#Fungsi Convex Hull Bagian Kanan
def ConvexHullRight(right, top, bottom, points):
    above = []
    below = []
    detMin = 0
    pointMinAbove = []
    pointMinBelow = []
    result = np.array([[]], dtype=int)

    #basis, membentuk garis convex hull
    if(len(points)==0):
        return(np.array([[top[2], bottom[2]]], dtype=int))
    if(len(points)==1):
        return(np.array([[top[2], right[2]], [right[2], bottom[2]]], dtype=int))
    else:

        #Mengumpulkan titik-titik di atas dari garis yang terbentuk dari titik teratas dan terjauh di kanan,
        #juga mencari titik terjauh yang diatas garis tersebut
        for point in points:
            if (point[0] == right[0] and point[1] == right[1]):
                pass
            else:
                det = right[0]*top[1]+top[0]*point[1]+point[0]*right[1]-right[0]*point[1]-point[0]*top[1]-top[0]*right[1]
                if det < 0:
                    above.append(point)
                    if det < detMin:
                        detMin = det
                        pointMinAbove = point

        #Mengumpulkan titik-titik di bawah dari garis yang terbentuk dari titik terbawah dan terjauh di kanan,
        #juga mencari titik terjauh yang dibawah garis tersebut
        detMin = 0
        for point in points:
            if (point[0] == right[0] and point[1] == right[1]):
                pass
            else:
                det = bottom[0]*right[1]+right[0]*point[1]+point[0]*bottom[1]-bottom[0]*point[1]-point[0]*right[1]-right[0]*bottom[1]
                if det < 0:
                    below.append(point)
                    if det < detMin:
                        detMin = det
                        pointMinBelow = point

        #Mencari titik convex hull lain
        result = ConvexHullRight(pointMinAbove, top, right, above)
        result = np.append(result, ConvexHullRight(pointMinBelow, right, bottom, below), axis=0)
        return result