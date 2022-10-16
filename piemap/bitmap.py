from typing import no_type_check

from PIL import Image, ImageDraw, ImageFont  # type: ignore

from piemap import (
    ANGLE_MAX,
    ANGLE_OFF,
    GRAY,
    GREEN,
    HEIGHT,
    HEIGHT_OFF,
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
    return (TOP_LEFT_X + shift, TOP_LEFT_Y + shift), (TOP_LEFT_X + r, TOP_LEFT_Y + r)


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
def render() -> None:
    """Make importable to support tests."""

    # create an image for prototyping
    im = Image.new(mode='RGBA', size=(WIDTH, HEIGHT), color=WHITE)

    # create prototyping draw context
    draw = ImageDraw.Draw(im)

    N = 9
    R = RADIUS
    r = (R, R * 0.90, R * 0.80, R * 0.70, R * 0.65, R * 0.60, R * 0.55, 0, None)

    # All good if above disc at 80% all sectors below receive proportional red coloring adding to the yellow
    draw.pieslice(bbox_from_radii(R, R * 0.80), *fake_full_circle(ANGLE_OFF), fill=RED)

    # Inner disc to hide singularity noise at center
    draw.pieslice(bbox_from_radii(R, R * 0.10), *fake_full_circle(ANGLE_OFF), fill=GRAY)

    # The sectors
    for n in range(N):
        val = r[n]
        if val is None:
            draw.pieslice(bbox_from_radii(R, R), start_of(n, N), end_of(n, N), fill=WHITE)
            continue

        color = YELLOW if val < R * 0.80 else GREEN
        draw.pieslice(bbox_from_radii(R, val), start_of(n, N), end_of(n, N), fill=color)

    # The axes
    for n in range(N):
        draw.pieslice(
            extrude_bbox_by(PIE_BOX, 15), *fake_line(middle_of(n, N)), fill=GRAY, outline=GRAY, width=LINE_WIDTH
        )

    # outer circle (axis marker joining all dimensions)
    draw.pieslice(bbox_from_radii(R, R * 1.00), *fake_full_circle(ANGLE_OFF), fill=None, outline=GRAY, width=LINE_WIDTH)

    # All good if above disc at 80% circle only as marker
    draw.pieslice(bbox_from_radii(R, R * 0.80), *fake_full_circle(ANGLE_OFF), fill=None, outline=GRAY, width=1)

    # title and sub title
    t_fnt = ImageFont.truetype(FONT_PATH, TITLE_SIZE)
    st_fnt = ImageFont.truetype(FONT_PATH, SUBTITLE_SIZE)
    t_text = 'Hällo'
    st_text = 'Wörldß'
    t_len = draw.textlength(t_text, font=t_fnt)
    st_len = draw.textlength(st_text, font=st_fnt)
    draw.multiline_text((WIDTH_HALF - int(t_len / 2), HEIGHT_OFF), t_text, font=t_fnt, fill=(0, 0, 0), align='center')
    draw.multiline_text(
        (WIDTH_HALF - int(st_len / 2), HEIGHT_OFF + TITLE_SIZE), st_text, font=st_fnt, fill=(0, 0, 0), align='center'
    )
    del draw

    # im.resize((640, 640), resample=Image.Resampling.LANCZOS)
    im.save(OUT_PNG_PATH, 'PNG')

    im.show()


if __name__ == '__main__':
    render()
