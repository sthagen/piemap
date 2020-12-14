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
}


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
    axis_name_space_sep = True if axis_name_space_sep is None else axis_name_space_sep
    return NotImplemented


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
