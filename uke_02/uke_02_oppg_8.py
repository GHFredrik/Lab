def point_in_rectangle(x0, y0, x1, y1, x2, y2):
    top = max(y0, y1)
    bot = min(y0, y1)
    left = min(x0, x1)
    right = max(x0, x1)

    if bot <= y2 <= top and left <= x2 <= right:
        return True
    else:
        return False

def rectangles_overlap(x0, y0, x1, y1, x2, y2, x3, y3):
    top0 = max(y0, y1)
    bot0 = min(y0, y1)
    left0 = min(x0, x1)
    right0 = max(x0, x1)

    top1 = max(y2, y3)
    bot1 = min(y2, y3)
    left1 = min(x2, x3)
    right1 = max(x2, x3)

    for i in range(bot1, top1):
        for j in range(left1, right1):
            if bot0 <= i <= top0 and left0 <= j <= right0:
                return True
    return False

def circle_overlaps_rectangle(x0, y0, x1, y1, x2, y2, r2):
    top = max(y0, y1)
    bot = min(y0, y1)
    left = min(x0, x1)
    right = max(x0, x1)

    if bot+r2 <= y2 <= top+r2 and left+r2 <= x2 <= right+r2:
        return True
    else:
        return False

print(circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2))
print(circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2))
print(circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5))
print(circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5))
print(circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01))