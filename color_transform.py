import colour

spd = colour.ILLUMINANTS_RELATIVE_SPDS.get('F2')
colour.colour_rendering_index(spd)

print(colour.colour_rendering_index(spd))

il = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D50']
colour.xy_to_CCT(il, method='Hernandez 1999')

print(colour.xy_to_CCT(il, method='Hernandez 1999'))