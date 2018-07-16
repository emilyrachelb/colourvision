#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       download.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    Downloads a set of basic colour swatches

import os
import threading
from DictQuery import Query

# JSON Dictionary containing the colour information:
# List of colours taken from https://en.wikipedia.org/wiki/Web_colours#X11_colour_names
pinkColours = {
    "pink": {"colour": "ffc0cb"},
    "lightPink": {"colour": "ffb6c1"},
    "hotPink": {"colour": "ff69b4"},
    "deepPink": {"colour": "ff1493"},
    "paleVioletRed": {"colour": "db7093"},
    "mediumVioletRed": {"colour": "c71585"}
}
redColours = {
    "lightSalmon": {"colour": "ffa07a"},
    "salmon": {"colour": "fa8072"},
    "darkSalmon": {"colour": "e9967a"},
    "lightCoral": {"colour": "f08080"},
    "indianRed": {"colour": "cd5c5c"},
    "crimson": {"colour": "dc143c"},
    "fireBrick": {"colour": "b22222"},
    "darkRed": {"colour": "8b0000"},
    "red": {"colour": "ff0000"}
}

orangeColours = {
    "orangeRed": {"colour": "ff4500"},
    "tomato": {"colour": "ff6347"},
    "coral": {"colour": "ff7f50"},
    "darkOrange": {"colour": "ff8c00"},
    "orange": {"colour": "ffa500"}
}

yellowColours = {
    "yellow": {"colour": "ffff00"},
    "lightYellow": {"colour": "ffffe0"},
    "lemonChiffron": {"colour": "fffacd"},
    "lightGoldenrodYellow": {"colour": "fafad2"},
    "papayaWhip": {"colour": "ff3fd5"},
    "moccasin": {"colour": "ffe4b5"},
    "peachPuff": {"colour": "ffdab9"},
    "paleGoldenrod": {"colour": "eee8aa"},
    "khaki": {"colour": "f0e68c"},
    "darkKhaki": {"colour": "bdb76b"},
    "gold": {"colour": "ffd700"}
}
brownColours = {
    "cornsilk": {"colour": "fff8dc"},
    "blanchedAlmond": {"colour": "ffe8cd"},
    "bisque": {"colour": "ffe4c4"},
    "navajoWhite": {"colour": "ffdead"},
    "wheat": {"colour": "f5deb3"},
    "burlyWood": {"colour": "deb887"},
    "tan": {"colour": "d2b48c"},
    "rosyBrown": {"colour": "bc8f8f"},
    "sandyBrown": {"colour": "f4af60"},
    "goldenrod": {"colour": "daa520"},
    "darkGoldenrod": {"colour": "b8860b"},
    "peru": {"colour": "cd853f"},
    "chocolate": {"colour": "d2691e"},
    "saddleBrown": {"colour": "8b4513"},
    "sienna": {"colour": "a0522d"},
    "brown": {"colour": "a52a2a"},
    "maroon": {"colour": "800000"}
}

greenColours = {
    "darkOliveGreen": {"colour": "556b2f"},
    "olive": {"colour": "808000"},
    "oliveDrab": {"colour": "6b8e23"},
    "yellowGreen": {"colour": "9acd32"},
    "limeGreen": {"colour": "32cd32"},
    "lime": {"colour": "00ff00"},
    "lawnGreen": {"colour": "7cfc00"},
    "chartreuse": {"colour": "7fff00"},
    "greenYellow": {"colour": "adff2f"},
    "springGreen": {"colour": "00ff7f"},
    "mediumSpringGreen": {"colour": "00fa9a"},
    "lightGreen": {"colour": "90ee90"},
    "paleGreen": {"colour": "98fb98"},
    "darkSeaGreen": {"colour": "8fbc8f"},
    "mediumAquamarine": {"colour": "66cdaa"},
    "mediumSeaGreen": {"colour": "3cb371"},
    "seaGreen": {"colour": "2e8b57"},
    "forestGreen": {"colour": "228b22"},
    "green": {"colour": "008000"},
    "darkGreen": {"colour": "006400"}
}
cyanColours = {
    "aqua": {"colour": "00ffff"},
    "cyan": {"colour": "00ffff"},
    "lightCyan": {"colour": "e0ffff"},
    "paleTurquoise": {"colour": "afeeee"},
    "aquamarine": {"colour": "7fffd4"},
    "turquoise": {"colour": "40e0d0"},
    "mediumTurquoise": {"colour": "48d1cc"},
    "darkTurquoise": {"colour": "00ced1"},
    "lightSeaGreen": {"colour": "20b2aa"},
    "cadetBlue": {"colour": "5f9ea0"},
    "darkCyan": {"colour": "008b8b"},
    "teal": {"colour": "008080"}
}

blueColours = {
    "lightSteelBlue": {"colour": "b0c4de"},
    "powderBlue": {"colour": "b0e0e6"},
    "lightBlue": {"colour": "add8e6"},
    "skyBlue": {"colour": "87ceeb"},
    "lightSkyBlue": {"colour": "87cefa"},
    "deepSkyBlue": {"colour": "00bfff"},
    "dodgerBlue": {"colour": "1e90ff"},
    "cornflowerBlue": {"colour": "6495ed"},
    "steelBlue": {"colour": "4682b4"},
    "royalBlue": {"colour": "4169e1"},
    "blue": {"colour": "0000ff"},
    "mediumBlue": {"colour": "0000cd"},
    "darkBlue": {"colour": "00008b"},
    "navy": {"colour": "000080"},
    "midnightBlue": {"colour": "191970"}
}
purpleColours = {
    "lavender": {"colour": "e6e6fa"},
    "thistle": {"colour": "d8bfd8"},
    "plum": {"colour": "dda0dd"},
    "violet": {"colour": "ee82ee"},
    "orchid": {"colour": "da70d6"},
    "fuchsia": {"colour": "ff00ff"},
    "magenta": {"colour": "ff00ff"},
    "mediumOrchid": {"colour": "ba55d3"},
    "mediumPurple": {"colour": "9370db"},
    "blueViolet": {"colour": "8a2be2"},
    "darkViolet": {"colour": "9400d3"},
    "darkOrchid": {"colour": "9932cc"},
    "darkMagenta": {"colour": "8b008b"},
    "purple": {"colour": "800080"},
    "indigo": {"colour": "4b0082"},
    "darkSlateBlue": {"colour": "483d8b"},
    "slateBlue": {"colour": "6a5acd"},
    "mediumSlateBlue": {"colour": "7b68ee"}
}

whiteColours = {
    "white": {"colour": "ffffff"},
    "snow": {"colour": "fffafa"},
    "honeydew": {"colour": "f0fff0"},
    "mintCream": {"colour": "f5fffa"},
    "azure": {"colour": "f0ffff"},
    "aliceBlue": {"colour": "f0f8ff"},
    "ghostWhite": {"colour": "f8f8ff"},
    "whiteSmoke": {"colour": "f5f5f5"},
    "seashell": {"colour": "fff6ee"},
    "beige": {"colour": "f5f5dc"},
    "oldLace": {"colour": "fdf5e6"},
    "floralWhite": {"colour": "fffaf0"},
    "ivory": {"colour": "fffff0"},
    "antiqueWhite": {"colour": "faebd7"},
    "linen": {"colour": "faf0e6"},
    "lavenderBlush": {"colour": "fff0f5"},
    "mistyRose": {"colour": "ffe4e1"}
}

greyColours = {
    "gainsboro": {"colour": "dcdcdc"},
    "lightGray": {"colour": "d3d3d3"},
    "silver": {"colour": "c0c0c0"},
    "darkGrey": {"colour": "a9a9a9"},
    "grey": {"colour": "808080"},
    "dimGrey": {"colour": "696969"},
    "lightSlateGray": {"colour": "778899"},
    "slateGray": {"colour": "708090"},
    "darkSlateGrey": {"colour": "2f4f4f"},
    "black": {"colour": "000000"}
}

# create the colour directories
os.system('mkdir -p colours/pink '
          'colours/red '
          'colours/orange '
          'colours/yellow '
          'colours/brown '
          'colours/green '
          'colours/cyan '
          'colours/blue '
          'colours/purple '
          'colours/white '
          'colours/grey')

for key in pinkColours:
    counter = 1
    colourName = key
    colourCode = Query(pinkColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/pink/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))
    
    for i in range (0, 999):
        counter = counter + 1
        os.system("cp colours/pink/{}-1.jpeg colours/pink/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in redColours:
    counter = 1
    colourName = key
    colourCode = Query(redColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/red/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/red/{}-1.jpeg colours/red/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in orangeColours:
    counter = 1
    colourName = key
    colourCode = Query(orangeColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/orange/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/orange/{}-1.jpeg colours/orange/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in yellowColours:
    counter = 1
    colourName = key
    colourCode = Query(yellowColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/yellow/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/yellow/{}-1.jpeg colours/yellow/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in brownColours:
    counter = 1
    colourName = key
    colourCode = Query(brownColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/brown/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/brown/{}-1.jpeg colours/brown/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in greenColours:
    counter = 1
    colourName = key
    colourCode = Query(greenColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/green/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/green/{}-1.jpeg colours/green/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in cyanColours:
    counter = 1
    colourName = key
    colourCode = Query(cyanColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/cyan/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/cyan/{}-1.jpeg colours/cyan/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in blueColours:
    counter = 1
    colourName = key
    colourCode = Query(blueColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/blue/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/blue/{}-1.jpeg colours/blue/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in purpleColours:
    counter = 1
    colourName = key
    colourCode = Query(purpleColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/purple/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/purple/{}-1.jpeg colours/purple/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in whiteColours:
    counter = 1
    colourName = key
    colourCode = Query(whiteColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/white/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/white/{}-1.jpeg colours/white/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))

for key in greyColours:
    counter = 1
    colourName = key
    colourCode = Query(greyColours).get("{}/colour".format(colourName))
    os.system("wget -qO colours/grey/{}-{}.jpeg https://placehold.it/1024/{}/000000?text=+".format(colourName, counter, colourCode))
    print("getting {}".format(colourName))

    for i in range(0, 999):
        counter = counter + 1
        os.system("cp colours/grey/{}-1.jpeg colours/grey/{}-{}.jpeg".format(colourName, colourName, counter))
    print("finished getting {}".format(colourName))