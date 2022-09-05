def split_line(x_lo, x_hi, n):
    lineSegment = (x_hi - x_lo) / n
    for i in range(n):
        print(str(x_lo + (i * lineSegment)) + " " + str(x_lo + ((i+1) * lineSegment)) + " ")

split_line(1.0, 7.0, 3)
split_line(0.0, 1.0, 4)