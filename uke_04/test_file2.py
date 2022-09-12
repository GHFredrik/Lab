def point_in_rectangle(x0, y0, x1, y1, x2, y2):
    return (min(x0, x1) <= x2 <= max(x0, x1)) and (min(y0, y1) <= y2 <= max(y0, y1))
