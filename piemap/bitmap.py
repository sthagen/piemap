from typing import no_type_check

from PIL import Image, ImageDraw, ImageFont  # type: ignore

import piemap.geometry as geom
from piemap import (
    ANGLE_MAX,
    ANGLE_OFF,
    CIRCLE_CENTER,
    GRAY,
    GREEN,
    HEIGHT,
    HEIGHT_OFF,
    LABEL_SIZE,
    LINE_WIDTH,
    PIE_BOX,
    RADIUS,
    RED,
    SUBTITLE_SIZE,
    TITLE_SIZE,
    TOP_LEFT_X,
    TOP_LEFT_Y,
    WHITE,
    WIDTH,
    WIDTH_HALF,
    YELLOW,
)

FONT_PATH = '../FreeMono.ttf'
OUT_PNG_PATH = '../bitmap.png'
FAKE_EPS_DEGREES = 0.05

Coord = tuple[float, float]
BBox = tuple[Coord, Coord]


@no_type_check
def start_of(n: int, n_max: int) -> float:
    """Start angle in values [0, MAX] first ref is 12 o'clock (OFF) with the of sector n of [1, N]."""
    fractional_angle = ANGLE_MAX / n_max
    return (n * fractional_angle + ANGLE_OFF - fractional_angle / 2) % ANGLE_MAX


@no_type_check
def middle_of(n: int, n_max: int) -> float:
    """Middle angle (axis) in values [0, MAX] first ref is 12 o'clock (OFF) with the of sector n of [1, N]."""
    return (n * ANGLE_MAX / n_max + ANGLE_OFF) % ANGLE_MAX


@no_type_check
def end_of(n: int, n_max: int) -> float:
    """End angle in values [0, MAX] first ref is 12 o'clock (OFF) with the of sector n of [1, N]."""
    return (start_of(n, n_max) + ANGLE_MAX / n_max) % ANGLE_MAX


@no_type_check
def bbox_from_radii(ref_r: int, r: float) -> BBox:
    """Return bbox as left upper and right lower x,y tuples from radius within reference radius"""
    shift = ref_r - r
    return (TOP_LEFT_X + shift, TOP_LEFT_Y + shift), (TOP_LEFT_X + ref_r + r, TOP_LEFT_Y + ref_r + r)


@no_type_check
def extrude_bbox_by(bbox: BBox, extrusion: int) -> BBox:
    """Extrude bounding box symmetrically by extrusion amount."""
    return (bbox[0][0] - extrusion, bbox[0][1] - extrusion), (bbox[1][0] + extrusion, bbox[1][1] + extrusion)


@no_type_check
def fake_full_circle(angle: float) -> Coord:
    """Fake a full circle to reduce the number of functions used."""
    return angle, angle - FAKE_EPS_DEGREES


@no_type_check
def fake_line(angle: float) -> Coord:
    """Fake a line to reduce the number of functions used."""
    return angle, angle + FAKE_EPS_DEGREES


@no_type_check
def draw_titles(engine, title: str, subtitle: str) -> None:
    """Draw the title and subtitle centered on top of the pie and adjust placement for text length."""
    t_fnt = ImageFont.truetype(FONT_PATH, TITLE_SIZE)
    st_fnt = ImageFont.truetype(FONT_PATH, SUBTITLE_SIZE)
    t_len = engine.textlength(title, font=t_fnt)
    st_len = engine.textlength(subtitle, font=st_fnt)
    engine.multiline_text((WIDTH_HALF - int(t_len / 2), HEIGHT_OFF), title, font=t_fnt, fill=(0, 0, 0), align='center')
    engine.multiline_text(
        (WIDTH_HALF - int(st_len / 2), HEIGHT_OFF + TITLE_SIZE), subtitle, font=st_fnt, fill=(0, 0, 0), align='center'
    )


@no_type_check
def draw_label_at(engine, label: str, at: Coord) -> None:
    """Draw the label starting at position."""
    fnt = ImageFont.truetype(FONT_PATH, LABEL_SIZE)
    l_len = engine.textlength(label, font=fnt)
    engine.multiline_text((at[0] - int(l_len / 2), at[1]), label, font=fnt, fill=(0, 0, 0), align='center')


@no_type_check
def to_plot(xy: Coord) -> Coord:
    """Map [0, 1] x [0, 1] onto the plot area that goes east, south."""
    return NotImplemented


@no_type_check
def render(values: tuple[float | None, ...]) -> None:
    """Make importable to support tests."""
    n_dim = len(values)

    # create an image for prototyping
    im = Image.new(mode='RGBA', size=(WIDTH, HEIGHT), color=WHITE)

    # create prototyping draw context
    draw = ImageDraw.Draw(im)

    # All good if above disc at 80% all sectors below receive proportional red coloring adding to the yellow
    draw.pieslice(bbox_from_radii(RADIUS, RADIUS * 0.80), *fake_full_circle(ANGLE_OFF), fill=RED)

    # Inner disc to hide singularity noise at center
    draw.pieslice(bbox_from_radii(RADIUS, RADIUS * 0.03), *fake_full_circle(ANGLE_OFF), fill=GRAY)

    # The sectors
    for n, val in enumerate(values):
        if val is None:
            draw.pieslice(bbox_from_radii(RADIUS, RADIUS), start_of(n, n_dim), end_of(n, n_dim), fill=WHITE)
            continue

        color = YELLOW if val < RADIUS * 0.80 else GREEN
        draw.pieslice(bbox_from_radii(RADIUS, val), start_of(n, n_dim), end_of(n, n_dim), fill=color)

    draw_label_at(draw, '^', CIRCLE_CENTER)  # protonly
    draw_label_at(draw, 'L', (CIRCLE_CENTER[0] - RADIUS, CIRCLE_CENTER[1] + RADIUS))  # protonly
    # The axes and dim=value labels
    for n, val in enumerate(values):
        draw.pieslice(
            extrude_bbox_by(PIE_BOX, 15), *fake_line(middle_of(n, n_dim)), fill=GRAY, outline=GRAY, width=LINE_WIDTH
        )
        coords = geom.xy_point_from_radius_angle(RADIUS, middle_of(n, n_dim), *CIRCLE_CENTER)
        if val is None:
            val_disp = 'n/a'
        else:
            val_disp = f'{round(val, 1)}|{round(val/RADIUS, 1)}'  # |{[round(c, 1) for c in coords]}'
            # ang_quest = (middle_of(n, n_dim) - ANGLE_OFF) % 360
            # val_disp = f'{round(ang_quest, 1)}|{[round(c, 1) for c in coords]}'
        # draw_label_at(draw, f'd[{n}]={val_disp}', (PIE_BOX[0][0], PIE_BOX[0][1] + n * LABEL_SIZE))
        draw_label_at(draw, f'd[{n}]={val_disp}', coords)

    # outer circle (axis marker joining all dimensions)
    draw.pieslice(
        bbox_from_radii(RADIUS, RADIUS * 1.00), *fake_full_circle(ANGLE_OFF), fill=None, outline=GRAY, width=LINE_WIDTH
    )

    # All good if above disc at 80% circle only as marker
    draw.pieslice(
        bbox_from_radii(RADIUS, RADIUS * 0.80), *fake_full_circle(ANGLE_OFF), fill=None, outline=GRAY, width=1
    )

    # title and sub title
    draw_titles(draw, title='Hällo', subtitle='Wörldß')
    del draw

    # im.resize((640, 640), resample=Image.Resampling.LANCZOS)
    im.save(OUT_PNG_PATH, 'PNG')

    im.show()


if __name__ == '__main__':  # pragma: no cover
    R = RADIUS
    r = (R, R * 0.90, R * 0.80, R * 0.70, R * 0.65, R * 0.60, R * 0.55, 0, None)
    render(r)
