def find_min_arrow_shots(points):

    if len(points) == 0:
        return 0

    # sort balloons by Xend
    points = sorted(points, key=lambda x:x[1])

    arrows = 1
    prev_end = points[0][1]

    for i in range(1,len(points)):
        if points[i][0] > prev_end: # if start of next balloon is >, increment arrow
            arrows += 1
            prev_end = points[i][1]

    return arrows