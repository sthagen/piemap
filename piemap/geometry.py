import math


def exact_top_of_center(angle):
    """
    True, if angle leads to point exactly top of center
    """
    return True if angle == 270 else False


def exact_bottom_of_center(angle):
    """
    True, if angle leads to point exactly bottom of center
    """
    return True if angle == 90 else False


def right_bottom_of_center(angle):
    """
    True, if angle leads to point right bottom of center
    """
    return True if angle < 90 else False


def right_top_of_center(angle):
    """
    True, if angle leads to point right top of center
    """
    return True if angle > 270 else False


def left_bottom_of_center(angle):
    """
    True, if angle leads to point left bottom of center
    """
    return True if angle > 90 and angle < 180 else False


def left_top_of_center(angle):
    """
    True, if angle leads to point left top of center
    """
    return True if angle >= 180 and angle < 270 else False


def octant_of_angle(angle):
    """
    derive octant in (N,NW,W,SW,S,SE,E,NE) counterclockwise from angle
    """
    error_log = print
    if exact_top_of_center(angle):
        return 'N'
    elif exact_bottom_of_center(angle):
        return 'S'
    elif right_bottom_of_center(angle):
        return 'E' if angle == 0 else 'SE'
    elif left_top_of_center(angle):
        return 'W' if angle == 180 else 'NW'
    elif left_bottom_of_center(angle):
        return 'SW'        
    elif right_top_of_center(angle):
        return 'NE'

    error_log(f'geometry.octant_of_angle_X_angle == {angle}')
    return 'X'


def axis_name_circle_adjust(angle, font_size_pts, text_angle, font_name, axis_name, axis_name_space_sep = None):
    """
    calculate axis name placements from bounding box and angle
    """

    def bounding_box_from_font(font_size_pts, text_angle, font_name, axis_name):
        """
        TODO(sthagen): PHP::imagettfbbox(font_size_pts, text_angle, font_name, axis_name)
        6,7	upper left corners X,Y-Pos and 4,5	upper right corners X,Y-Pos
        0,1	lower left corners X,Y-Pos and 2,3	lower right corners X,Y-Pos
        
        Returns tuple with: 
             0,         1,         2,          3,          4,          5,          6,         7
             lo_left_x, lo_left_y, lo_right_x, lo_right_y, hi_right_x, hi_right_y, hi_left_x, hi_left_y
        """
        return (100, 200, 300, None, None, None, None, 400)  # TODO(sthagen) implement real functionality

    axis_name_space_sep = True if axis_name_space_sep is None else axis_name_space_sep
    
    bbox = bounding_box_from_font(font_size_pts, text_angle, font_name, axis_name)
    text_width = abs(bbox[2] - bbox[0])
    text_height = abs(bbox[7] - bbox[1])

    sep_x = 0
    sep_y = 0
    if axis_name_space_sep:
        sep_x = 5
        sep_y = 5

    dx_pixel = 0
    dy_pixel = 0
    octant = octant_of_angle(angle)
    if octant == 'SE':
        dx_pixel = 0 + sep_x
        dy_pixel = +text_height + sep_y
    elif octant == 'NE':
        dx_pixel = 0 + sep_x
        dy_pixel = 0 - sep_y
    elif octant == 'SW':
        dx_pixel = -text_width - sep_x
        dy_pixel = +text_height + sep_y
    elif octant == 'NW':
        dx_pixel = -text_width - sep_x
        dy_pixel = 0 - sep_y
    elif octant == 'S':
        dx_pixel = -text_width / 2
        dy_pixel = +text_height + 2 * sep_y
    elif octant == 'N':
        # exactly on top of center
        dx_pixel = -text_width / 2
        dy_pixel = 0 - 2 * sep_y
    elif octant == 'W':
        dx_pixel = -text_width - sep_x
        dy_pixel = +text_height / 2 + 0
    elif octant == 'E':
        dx_pixel = +text_width + sep_x
        dy_pixel = +text_height / 2 + 0

    # Note: Unmatched octant returns (0,0)
    return (dx_pixel, dy_pixel)


def xy_point_from_radius_angle(radius, angle, c_x = 0, c_y = 0):
    """
    return point as tuple in (x,y) = (radius,angle/[deg]) possibly shifted (c_x, c_y)
    """
    
    def deg2rad(deg):
        """TODO(sthagen) refactor later."""
        return deg * math.pi / 180.0

    angle_in_rad = deg2rad(angle)
    x = c_x + math.cos(angle_in_rad) * radius; 
    y = c_y + math.sin(angle_in_rad) * radius;
    return (x, y)
