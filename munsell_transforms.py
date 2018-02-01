import numpy as np
import colour

with open('testConversions.txt', 'w') as f:
    for munsell_colour in ('7.5R 4/8', '5YR 9/2', '10Y 8/12', '5GY 3/2', '2.8P 4.5/9.3', 'N8.9', '2.4B 4.6/6.0'):
        f.write(('Converting to "xyY" colourspace and then to "XYZ" from given "Munsell" \t{0}'.format(munsell_colour)))
        f.write('\n')
        f.write('xyY value: \t' + str(colour.munsell_colour_to_xyY(munsell_colour)))
        f.write('\n')
        f.write('XYZ value: \t' + str(colour.models.cie_xyy.xyY_to_XYZ(colour.munsell_colour_to_xyY(munsell_colour))))
        f.write('\n')
        f.write('Lab50 value: \t' + str(colour.models.cie_lab.XYZ_to_Lab(colour.models.cie_xyy.xyY_to_XYZ(colour.munsell_colour_to_xyY(munsell_colour)))))
        f.write('\n')

