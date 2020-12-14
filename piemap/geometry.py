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
