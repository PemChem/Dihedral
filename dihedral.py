### This script provides definitions for distance, angle, and dihedral
### x1coord, y1coord, and z1coord correspond to the xyz cartesian
###   coordinates of atom 1
### These definitions can be copied and pasted into your existing 
###   python-coded files
### An example for running the dihedral definition is provided on
###   the last line of this file, and will produce an answer of -90.00
### Please uncomment the last line to do the test
### For multiple points, i.e., analyzing a dynamics trajectory
###   make a list of x1coord, etc., and loop through the list

def distance(x1coord, y1coord, z1coord, x2coord, y2coord, z2coord):
	import math
	xvar_list = [x1coord, x2coord]
	yvar_list = [y1coord, y2coord]
	zvar_list = [z1coord, z2coord]
	dx = float(xvar_list[1]) - float(xvar_list[0])
	dy = float(yvar_list[1]) - float(yvar_list[0])
	dz = float(zvar_list[1]) - float(zvar_list[0])
	dx2 = dx * dx
	dy2 = dy * dy
	dz2 = dz * dz
	distance = math.sqrt(dx2 + dy2 + dz2)
	return '{0:.2f}'.format(distance)
def angle(x1coord, y1coord, z1coord, x2coord, y2coord, z2coord, x3coord, y3coord, z3coord):
	import math
	xvar_list = [x1coord, x2coord, x3coord]
	yvar_list = [y1coord, y2coord, y3coord]
	zvar_list = [z1coord, z2coord, z3coord]
	vec1x = float(xvar_list[0]) - float(xvar_list[1])
	vec1y = float(yvar_list[0]) - float(yvar_list[1])
	vec1z = float(zvar_list[0]) - float(zvar_list[1])
	vec1 = [vec1x, vec1y, vec1z]
	vec2x = float(xvar_list[2]) - float(xvar_list[1])
	vec2y = float(yvar_list[2]) - float(yvar_list[1])
	vec2z = float(zvar_list[2]) - float(zvar_list[1])
	vec2 = [vec2x, vec2y, vec2z]
	onedx = float(xvar_list[1]) - float(xvar_list[0])
	onedy = float(yvar_list[1]) - float(yvar_list[0])
	onedz = float(zvar_list[1]) - float(zvar_list[0])
	onedx2 = onedx * onedx
	onedy2 = onedy * onedy
	onedz2 = onedz * onedz
	onedistance = math.sqrt(onedx2 + onedy2 + onedz2)
	twodx = float(xvar_list[2]) - float(xvar_list[1])
	twody = float(yvar_list[2]) - float(yvar_list[1])
	twodz = float(zvar_list[2]) - float(zvar_list[1])
	twodx2 = twodx * twodx
	twody2 = twody * twody
	twodz2 = twodz * twodz
	twodistance = math.sqrt(twodx2 + twody2 + twodz2)
	distances = onedistance * twodistance
	vectorsx = vec1x * vec2x
	vectorsy = vec1y * vec2y
	vectorsz = vec1z * vec2z
	vectors = vectorsx + vectorsy + vectorsz
	x = vectors / distances
	theta_radians = math.acos(x)
	theta = theta_radians * 57.29577951308
	return '{0:.2f}'.format(theta)
def dihedral(x1coord, y1coord, z1coord, x2coord, y2coord, z2coord, x3coord, y3coord, z3coord, x4coord, y4coord, z4coord):
	import math
	xvar_list = [x1coord, x2coord, x3coord, x4coord]
	yvar_list = [y1coord, y2coord, y3coord, y4coord]
	zvar_list = [z1coord, z2coord, z3coord, z4coord]
### For plane ABC
	vecABi = float(xvar_list[1]) - float(xvar_list[0])
	vecABj = float(yvar_list[1]) - float(yvar_list[0])
	vecABk = float(zvar_list[1]) - float(zvar_list[0])
	vecACi = float(xvar_list[2]) - float(xvar_list[0])
	vecACj = float(yvar_list[2]) - float(yvar_list[0])
	vecACk = float(zvar_list[2]) - float(zvar_list[0])
	ABcrossACi = (vecABj * vecACk) - (vecABk * vecACj)
	ABcrossACj = (vecABk * vecACi) - (vecABi * vecACk)
	ABcrossACk = (vecABi * vecACj) - (vecABj * vecACi)
	dABC = 0 - ABcrossACi - ABcrossACj - ABcrossACk
### For plane BCD
	vecBCi = float(xvar_list[2]) - float(xvar_list[1])
	vecBCj = float(yvar_list[2]) - float(yvar_list[1])
	vecBCk = float(zvar_list[2]) - float(zvar_list[1])
	vecBDi = float(xvar_list[3]) - float(xvar_list[1])
	vecBDj = float(yvar_list[3]) - float(yvar_list[1])
	vecBDk = float(zvar_list[3]) - float(zvar_list[1])
	BCcrossBDi = (vecBCj * vecBDk) - (vecBCk * vecBDj)
	BCcrossBDj = (vecBCk * vecBDi) - (vecBCi * vecBDk)
	BCcrossBDk = (vecBCi * vecBDj) - (vecBCj * vecBDi)
	dBCD = 0 - BCcrossBDi - BCcrossBDj - BCcrossBDk
### Calculating Dihedral
	numerator = (ABcrossACi * BCcrossBDi) + (ABcrossACj * BCcrossBDj) + (ABcrossACk * BCcrossBDk)
	denom1 = math.sqrt((ABcrossACi * ABcrossACi) + (ABcrossACj * ABcrossACj) + (ABcrossACk * ABcrossACk))
	denom2 = math.sqrt((BCcrossBDi * BCcrossBDi) + (BCcrossBDj * BCcrossBDj) + (BCcrossBDk * BCcrossBDk))
	denom = denom1 * denom2
	whole = numerator / denom
	dihedral_radian = math.acos(whole)
	ABxACcrossBCxBDi = (ABcrossACj * BCcrossBDk) - (ABcrossACk * BCcrossBDj)
	ABxACcrossBCxBDj = (ABcrossACk * BCcrossBDi) - (ABcrossACi * BCcrossBDk)
	ABxACcrossBCxBDk = (ABcrossACi * BCcrossBDj) - (ABcrossACj * BCcrossBDi)
	if ((ABxACcrossBCxBDi * vecBCi) + (ABxACcrossBCxBDj * vecBCj) + (ABxACcrossBCxBDk * vecBCk)) < 0:
		dihedral = dihedral_radian * -57.29577951308
	else:
		dihedral = dihedral_radian * 57.29577951308
	return '{0:.2f}'.format(dihedral)
print(dihedral(0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1))
