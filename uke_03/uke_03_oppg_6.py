#A
def g(x):
    return((1/8*x**2)-2*x+10)

#B
def approx_area_under_g(x_lo, x_hi):
    sum = 0
    for x_i in range(x_lo, x_hi):
        sum += g(x_i)
    return sum

#C
def riemann_sum_g(x_lo, x_hi, n):
    sum = 0
    lineSegment = (x_hi - x_lo) / n
    for x_i in range(n):
        sum += g(x_lo + (x_i * lineSegment)) * lineSegment
    return sum

#D
def riemann_sum(f, x_lo, x_hi, n):
    sum = 0
    lineSegment = (x_hi - x_lo) / n
    for x_i in range(n):
        sum += f(x_lo + (x_i * lineSegment)) * lineSegment
    return sum