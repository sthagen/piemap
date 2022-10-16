from PIL import Image, ImageDraw, ImageFont
# get an image
W = 1080
H = W
im = Image.new(mode="RGBA", size=(W, H), color='white')

# create draw context and draw arc
draw = ImageDraw.Draw(im)
N = 16
# colors = ('limegreen', 'seagreen', 'yellow', 'yellowgreen', 'crimson', 'silver') * 4
colors = ('darkgreen', 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'yellow', 'darkgreen') * 4
OFF = 270
MAX = 360
R = 900
r = (R * 0.80, R * 0.60, R * 0.30, R * 0.15, R * 0.10, 0, 20, R) * 4
# r = (R, R, R, R, R) * 4
woff = 0
hoff = 50
t_size = 40
st_size = 24
center_x = W / 2 - R / 2
center_y = H / 2 - R / 2 + hoff

# colors
green = '#008800'
yellowgreen = '#77ff20'
red = '#dd0000'
darkred = '#900000'
gray = '#c0c0c0'
yellow = '#ffff20'
white = '#ffffff'

# All good if above disc at 80% all sectors below receive proportional red coloring adding to the yellow
fill = red
start = 270
end = 269.95
rd = R * 0.80
shift = R - rd
left_upper = (center_x + shift, center_y + shift)
right_lower = (center_x + rd, center_y + rd)
draw.pieslice((left_upper, right_lower), start, end, fill=fill)

# Very bad if visible disc at 60%
start = 270
end = 269.95
rd = R * 0.6
shift = R - rd
left_upper = (center_x + shift, center_y + shift)
right_lower = (center_x + rd, center_y + rd)
draw.pieslice((left_upper, right_lower), start, end, fill=None, outline=gray, width=1)


# Inner disc to hide singularity noise at center
fill = gray
start = 270
end = 269.95
rd = R * 0.10
shift = R - rd
left_upper = (center_x + shift, center_y + shift)
right_lower = (center_x + rd, center_y + rd)
draw.pieslice((left_upper, right_lower), start, end, fill=fill)

# The sectors
for n in range(N):
    width = 1
    start = n * MAX / N + OFF
    end = start + MAX / N
    if r[n] > 0:
        fill = colors[n]
        shift = R - r[n]
        left_upper = (center_x + shift, center_y + shift)
        right_lower = (center_x + r[n], center_y + r[n])
        draw.pieslice((left_upper, right_lower), start, end, fill=fill)  # , outline='black', width=width)
        # draw.rectangle((left_upper, right_lower), fill=None, outline=fill, width=width)
    else:
        fill = white
        shift = R - R
        left_upper = (center_x + shift, center_y + shift)
        right_lower = (center_x + R, center_y + R)
        draw.pieslice((left_upper, right_lower), start, end, fill=fill)  # , outline='black', width=width)
        # draw.rectangle((left_upper, right_lower), fill=None, outline=fill, width=width)
    # im.show()

# The axes
for n in range(N):
    width = 1
    start = n * MAX / N + OFF
    end = start + 0.05
    extrusion = 15
    left_upper = (center_x - extrusion, center_y - extrusion)
    right_lower = (center_x + R + extrusion, center_y + R + extrusion)
    draw.pieslice((left_upper, right_lower), start, end, fill=gray, outline=gray, width=width)

# outer circle (axis marker joining all dimensions)
fill = None
start = 270
end = 269.95
rd = R * 1.00
shift = R - rd
left_upper = (center_x + shift, center_y + shift)
right_lower = (center_x + rd, center_y + rd)
draw.pieslice((left_upper, right_lower), start, end, fill=fill, outline=gray, width=1)

# All good if above disc at 80% circle only as marker
fill = None
start = 270
end = 269.95
rd = R * 0.80
shift = R - rd
left_upper = (center_x + shift, center_y + shift)
right_lower = (center_x + rd, center_y + rd)
draw.pieslice((left_upper, right_lower), start, end, fill=fill, outline=gray, width=1)

# title and sub title
t_fnt = ImageFont.truetype('../FreeMono.ttf', t_size)
st_fnt = ImageFont.truetype('../FreeMono.ttf', st_size)
t_text = 'Hällo'
st_text = "Wörldß"
t_len = draw.textlength(t_text, font=t_fnt)
st_len = draw.textlength(st_text, font=st_fnt)
draw.multiline_text((W / 2 - int(t_len / 2), hoff), t_text, font=t_fnt, fill=(0, 0, 0), align='center')
draw.multiline_text((W / 2 - int(st_len / 2), hoff + t_size), st_text, font=st_fnt, fill=(0, 0, 0), align='center')
del draw

# im.resize((640, 640), resample=Image.Resampling.LANCZOS)
im.save('../bitmap.png', "PNG")

im.show()
