# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.geometry as geom


def test_exact_top_of_center_true_ok():
    assert geom.exact_top_of_center(270) is True


def test_exact_top_of_center_false_ok():
    assert geom.exact_top_of_center(270 + 1) is False


def test_exact_bottom_of_center_true_ok():
    assert geom.exact_bottom_of_center(90) is True


def test_exact_bottom_of_center_false_ok():
    assert geom.exact_bottom_of_center(90 + 1) is False


def test_right_bottom_of_center_true_ok():
    assert geom.right_bottom_of_center(90 - 1) is True


def test_right_bottom_of_center_false_ok():
    assert geom.right_bottom_of_center(90) is False


def test_right_top_of_center_true_ok():
    assert geom.right_top_of_center(270 + 1) is True


def test_right_top_of_center_false_ok():
    assert geom.right_top_of_center(270) is False


def test_left_bottom_of_center_true_ok():
    assert geom.left_bottom_of_center(90 + 1) is True


def test_left_bottom_of_center_false_ok():
    assert geom.left_bottom_of_center(90) is False


def test_left_bottom_of_center_true_other_ok():
    assert geom.left_bottom_of_center(180 - 1) is True


def test_left_bottom_of_center_false_other_ok():
    assert geom.left_bottom_of_center(180) is False


def test_left_top_of_center_true_ok():
    assert geom.left_top_of_center(180) is True


def test_left_top_of_center_false_ok():
    assert geom.left_top_of_center(180 - 1) is False


def test_left_top_of_center_true_other_ok():
    assert geom.left_top_of_center(270 - 1) is True


def test_left_top_of_center_false_other_ok():
    assert geom.left_top_of_center(270) is False


def test_left_top_of_center_bad_argument_nok():
    message = r"'<=' not supported between instances of 'int' and 'object'"
    with pytest.raises(TypeError, match=message):
        geom.left_top_of_center(object())


def test_octant_of_angle_for_n_ok():
    assert geom.octant_of_angle(270) == 'N'


def test_octant_of_angle_for_s_ok():
    assert geom.octant_of_angle(90) == 'S'


def test_octant_of_angle_for_e_ok():
    assert geom.octant_of_angle(0) == 'E'


def test_octant_of_angle_for_se_ok():
    assert geom.octant_of_angle(90 - 1) == 'SE'


def test_octant_of_angle_for_w_ok():
    assert geom.octant_of_angle(180) == 'W'


def test_octant_of_angle_for_nw_ok():
    assert geom.octant_of_angle(270 - 1) == 'NW'


def test_octant_of_angle_for_sw_ok():
    assert geom.octant_of_angle(90 + 1) == 'SW'


def test_octant_of_angle_for_ne_ok():
    assert geom.octant_of_angle(270 + 1) == 'NE'


def test_xy_point_from_radius_angle_minimal_ok():
    r, a, dx, dy = 1, 0, 0, 0
    x, y = 1, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_x_ok():
    r, a, dx, dy = 1, 0, 1, 0
    x, y = 2, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_y_ok():
    r, a, dx, dy = 1, 0, 0, 1
    x, y = 1, 1
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_x_y_ok():
    r, a, dx, dy = 1, 0, 1, 1
    x, y = 2, 1
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_all_zero_ok():
    r, a, dx, dy = 0, 0, 0, 0
    x, y = 0, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_zero_ok():
    r, a, dx, dy = 0, 1, 2, 3
    x, y = 2, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_angle_zero_ok():
    r, a, dx, dy = 1, 0, 2, 3
    x, y = 3, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_angle_negative_and_zero_radius_ok():
    r, a, dx, dy = 0, -1, 2, 3
    x, y = 2, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)
