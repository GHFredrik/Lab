from math import sqrt

#A
def volume_of_box(w, h, d):
    return (w * h* d)

print (volume_of_box(2, 3, 5))

#B
def distance(x1, y1, x2, y2):
    return (sqrt(abs(x1-x2)**2 + abs(y1-y2)**2))

print(distance(0,0,1,1))

#C
def circles_overlap(x1, y1, r1, x2, y2, r2):
    return (distance(x1, y1, x2, y2) <= r1 + r2)

print(circles_overlap(0, 0, 1, 1, 1, 1))
print(circles_overlap(0, 0, 2, 4, 1, 2))
print(circles_overlap(0, 0, 3, 5, 0, 2))