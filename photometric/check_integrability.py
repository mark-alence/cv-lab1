import numpy as np


def check_integrability(normals):
    #  CHECK_INTEGRABILITY check the surface gradient is acceptable
    #   normals: normal image
    #   p : df / dx
    #   q : df / dy
    #   SE : Squared Errors of the 2 second derivatives

    # initalization
    h, w = normals.shape[:2]
    p = np.zeros(normals.shape[:2])
    q = np.zeros(normals.shape[:2])
    SE = np.zeros(normals.shape[:2])

    """
    ================
    Your code here
    ================
    Compute p and q, where
    p measures value of df / dx
    q measures value of df / dy
    
    """

    for y in range(h):
        for x in range(w):
            p[y][x] = normals[y][x][0]/normals[y][x][2]
            q[y][x] = normals[y][x][1]/normals[y][x][2]

    # change nan to 0
    p[p != p] = 0
    q[q != q] = 0

    for y in range(h):
        for x in range(w):
            if x+1 < w:
                diffs_2x = q[y][x+1] - q[y][x]
            else:
                diffs_2x = 0
            if y+1 < h:
                diffs_2y = p[y+1][x] - p[y][x]
            else:
                diffs_2y = 0
            SE[y][x] = ((diffs_2x - diffs_2y) ** 2) / 2

    """
    ================
    Your code here
    ================
    approximate second derivate by neighbor difference
    and compute the Squared Errors SE of the 2 second derivatives SE
    
    """

    return p, q, SE


if __name__ == '__main__':
    normals = np.zeros([10, 10, 3])
    check_integrability(normals)
