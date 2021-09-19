import numpy as np


def construct_surface(p, q, path_type='row'):
    '''
    CONSTRUCT_SURFACE construct the surface function represented as height_map
       p : measures value of df / dx
       q : measures value of df / dy
       path_type: type of path to construct height_map, either 'column',
       'row', or 'average'
       height_map: the reconstructed surface
    '''

    h, w = p.shape
    height_map = []
    if path_type == 'column':
        height_map = height_column(h, p, q, w)
        """
        ================
        Your code here
        ================
        % top left corner of height_map is zero
        % for each pixel in the left column of height_map
        %   height_value = previous_height_value + corresponding_q_value
        
        % for each row
        %   for each element of the row except for leftmost
        %       height_value = previous_height_value + corresponding_p_value
        
        """
    elif path_type == 'row':
        height_map = height_row(h, p, q, w)
        """
        ================
        Your code here
        ================
        """
    elif path_type == 'average':
        cols = height_column(h, p, q, w)
        rows = height_row(h, p, q, w)
        height_map = (rows + cols) / 2

    return height_map


def height_row(h, p, q, w):
    height_map = np.zeros([h, w])
    height_map[0][0] = 0
    for x in range(1, w):
        height_map[0][x] = height_map[0][x - 1] + p[0][x]
    for y in range(1, h):
        for x in range(0, w):
            height_map[y][x] = height_map[y - 1][x] + q[y][x]
    return height_map


def height_column(h, p, q, w):
    height_map = np.zeros([h, w])
    height_map[0][0] = 0
    for y in range(1, h):
        height_map[y][0] = height_map[y - 1][0] + q[y][0]
    for y in range(h):
        for x in range(1, w):
            height_map[y][x] = height_map[y][x - 1] + p[y][x]
    return height_map
