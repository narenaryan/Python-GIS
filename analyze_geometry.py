#Analyze geometry of Area

from proj1 import layer_feature_name,shapefile

def analyzeGeometry(geometry, indent=0):
	s = []
	s.append(" " * indent)
	s.append(geometry.GetGeometryName())

	if geometry.GetPointCount() > 0:
		s.append(" with %d data points" % geometry.GetPointCount())

	if geometry.GetGeometryCount() > 0:
		s.append(" containing:")

	print "".join(s)

	for i in range(geometry.GetGeometryCount()):
		analyzeGeometry(geometry.GetGeometryRef(i), indent+1)


layer = shapefile.GetLayer(0)
maps = layer_feature_name(layer)

for i in maps.items():
	print 'Feature ',i[0],': ',i[1]

choice = int(raw_input("Enter Feature No: "))

feature = layer.GetFeature(choice)
geometry = feature.GetGeometryRef()

analyzeGeometry(geometry)




