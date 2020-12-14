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
