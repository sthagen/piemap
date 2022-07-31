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
    return True if 90 < angle < 180 else False


def left_top_of_center(angle):
    """
    True, if angle leads to point left top of center
    """
    return True if 180 <= angle < 270 else False


def octant_of_angle(angle):
    """
    derive octant in (N,NW,W,SW,S,SE,E,NE) counterclockwise from angle
    """
    try:
        angle = int(angle)
    except TypeError:
        return 'X'
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


def axis_name_circle_adjust(angle, font_size_pts, text_angle, font_name, axis_name, axis_name_space_sep=None):
    """
    calculate axis name placements from bounding box and angle
    """

    def bounding_box_from_font(fnt_size_pts, txt_angle, fnt_name, axs_name):
        """
        TODO(sthagen): PHP::imagettfbbox(font_size_pts, text_angle, font_name, axis_name)
        6,7	upper left corners X,Y-Pos and 4,5	upper right corners X,Y-Pos
        0,1	lower left corners X,Y-Pos and 2,3	lower right corners X,Y-Pos

        Returns tuple with:
             0,         1,         2,          3,          4,          5,          6,         7
             lo_left_x, lo_left_y, lo_right_x, lo_right_y, hi_right_x, hi_right_y, hi_left_x, hi_left_y
        """
        return 100, 200, 300, None, None, None, None, 400  # TODO(sthagen) implement real functionality

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
    return dx_pixel, dy_pixel


def xy_point_from_radius_angle(radius, angle, c_x=0, c_y=0):
    """
    return point as tuple in (x,y) = (radius,angle/[deg]) possibly shifted (c_x, c_y)
    """

    def deg2rad(deg):
        """TODO(sthagen) refactor later."""
        return deg * math.pi / 180.0

    if math.isfinite(angle):
        angle_in_rad = deg2rad(math.fmod(angle + 360, 360))
        x = c_x + math.cos(angle_in_rad) * radius
        y = c_y + math.sin(angle_in_rad) * radius
        return x, y
    else:
        return math.nan, math.nan


def segment_angle_map(needed_number_of_axis):
    """
    return map of clockwise allocated angles for the needed axis segments
    from imagefilledarc: 0 degrees is located at the three-oclock position,
    ... and the arc is drawn clockwise.
    but we want one $angleMid allways point to 12 oclock, the rest
    ... determined by $neededNumberOfAxis
    and remember, we want the axis to point at 12 oclock, not start-stop
    so n = 1 gives (0,360,360) in theory 180 full circle to 180
       n = 2 gives [(270,90,360), (90,270,180)]
       n = 3 gives [(300,60,360), (60,180,120), (180,300,240)]
    """
    closure_guard, norm = 0, 360

    if needed_number_of_axis == 1:
        return [(closure_guard, norm, norm)]  # early exit for cornercase

    angle_per_sect = norm / needed_number_of_axis
    signed_correct_axis_shift = -angle_per_sect / 2
    triplets = []
    for i in range(0, needed_number_of_axis):
        angle_start = math.fmod(i * angle_per_sect + signed_correct_axis_shift + norm, norm)
        delta = angle_start + angle_per_sect

        angle_stop = derive_stop(angle_start, closure_guard, delta, norm)
        angle_mid = derive_mid(angle_start, angle_stop, norm)

        triplets.append((angle_start, angle_stop, angle_mid))

    return triplets


def transform_angle_map_ncw_icw(segment_angle_map_ncw):
    """
    return map of adjusted angles for imagefilledarcClockWise from nativeCW
    from imagefilledarc: 0 degrees is located at the three-oclock position,
    ... and the arc is drawn clockwise.
    but we want one $angleMid allways point to 12 oclock, the rest
    ... determined by $neededNumberOfAxis
    so transform maps 360 deg and 0 deg to 270 deg and 90 deg to 0 deg,
    ... i.e. d=-90 modulo 360
    """
    my_eps = 0.0  # 0.0000000000001 -  one zero more and 12+03 oclock for n=1

    if len(segment_angle_map_ncw) == 1:
        return [(270 + my_eps, 270 - my_eps, 270)]  # early exit for cornercase

    closure_guard, norm = 0, 360
    signed_shift_degrees = -90
    return rotate(closure_guard, norm, segment_angle_map_ncw, signed_shift_degrees)


def transform_angle_map_icw_ncw(segment_angle_map_icw):
    """
    return map of canonicalized angles for nativeClockWise from imagefilledarcCW
    from imagefilledarc: 0 degrees is located at the three-oclock position,
    ... and the arc is drawn clockwise.
    but we want one $angleMid allways point to 12 oclock, the rest
    ... determined by $neededNumberOfAxis
    so transform maps 360 deg and 0 deg to 270 deg and 90 deg to 0 deg,
    ... i.e. d=-90 modulo 360
    """
    closure_guard, norm = 0, 360
    # TODO(sthagen) remove after test: my_eps = 0.0000001

    if len(segment_angle_map_icw) == 1:
        return [(closure_guard, norm, norm)]  # early exit for cornercase

    signed_shift_degrees = +90
    return rotate(closure_guard, norm, segment_angle_map_icw, signed_shift_degrees)


def rotate(closure_guard, norm, segment_angle_map_icw, signed_shift_degrees):
    """Derive triplet mappings for segments."""
    triplets = []
    for data in segment_angle_map_icw:
        angle_start, angle_stop, angle_mid = data

        angle_start = math.fmod(angle_start + signed_shift_degrees + norm, norm)
        delta = angle_stop + signed_shift_degrees

        angle_stop = derive_stop(angle_start, closure_guard, delta, norm)
        angle_mid = derive_mid(angle_start, angle_stop, norm)

        triplets.append((angle_start, angle_stop, angle_mid))

    return triplets


def derive_stop(angle_start, closure_guard, delta, norm):
    """Derive stop angle respecting closure via norm."""
    angle = math.fmod(delta + norm, norm)
    if angle < angle_start and angle == closure_guard:
        angle = norm
    return angle


def derive_mid(angle_start, angle_stop, norm):
    """Derive mid angle respectng closure via norm."""
    angle = (angle_stop + angle_start) / 2.0
    if angle_stop < angle_start:
        angle = (angle_stop + norm + angle_start) / 2.0
    return angle
