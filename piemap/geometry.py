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
