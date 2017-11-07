def get_color_components(color):

    blue = color & 0xFF
    green = (color >> 8) & 0xFF
    red = (color >> 16)

    return 'red={0} green={1} blue={2}'.format(red, green, blue)

print get_color_components(0x00CED1)
print get_color_components(0x8B008B)