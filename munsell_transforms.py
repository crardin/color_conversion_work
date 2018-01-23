import numpy as np
import colour
from colour.utilities import message_box

# xyY = np.array([0.38736945, 0.35751656, 0.59362000])
#
# message_box(('Converting to "Munsell" colour from given "CIE xyY" '
#              'colourspace values:\n'
#              '\n\t{0}'.format(xyY)))
# print(colour.xyY_to_munsell_colour(xyY))
# print('\n')

f = open('testConversions.txt', 'w')

for munsell_colour in ('7.5R 4/8', '5YR 9/2', '10Y 8/12', '5GY 3/2'):
    f.write(('Converting to "xyY" colourspace and then to "XYZ" from given "Munsell" \t{0}'.format(munsell_colour)))
    f.write('\n')
    f.write('xyY value: \t' + str(colour.munsell_colour_to_xyY(munsell_colour)))
    f.write('\n')
    f.write('XYZ value: \t' + str(colour.models.cie_xyy.xyY_to_XYZ(colour.munsell_colour_to_xyY(munsell_colour))))
    f.write('\n')

f.close()