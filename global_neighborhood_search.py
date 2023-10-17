from math import sin, sqrt

# f_x Schwefel cost function
def variable_neighborhood_search(hyparam, xj):
    series = 0
    d = hyparam
    for i in range(1,d):
        series += xj*sin(sqrt(xj))

    f_x = 418.982*d - series
