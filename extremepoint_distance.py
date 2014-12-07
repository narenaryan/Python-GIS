#Analyze geometry
import math
from proj1 import layer_feature_name,shapefile
#For finding North most and South most points of a region in US and calculate Great Circle distance between them

def Great_circle(fis,sec):
	lat1,lan1 = fis
	lat2,lan2 = sec
	#Converting lats,lans to radians
	rlat1,rlan1,rlat2,rlan2 = map(lambda x:math.radians(x),(lat1,lan1,lat2,lan2))
	dlat = rlat2-rlat1
	dlan = rlan2-rlan1
	a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlan/2))**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = 6371 * c
	return d


def findPoints(geometry, results):
	for i in range(geometry.GetPointCount()):
		x,y,z = geometry.GetPoint(i)
		if results['north'] == None or results['north'][1] < y:
			results['north'] = (x,y)
		if results['south'] == None or results['south'][1] > y:
			results['south'] = (x,y)
	for i in range(geometry.GetGeometryCount()):
		findPoints(geometry.GetGeometryRef(i), results)


layer = shapefile.GetLayer(0)
maps = layer_feature_name(layer)

for i in maps.items():
	print 'Feature ',i[0],': ',i[1]

choice = int(raw_input("Enter Feature No: "))

feature = layer.GetFeature(choice)
geometry = feature.GetGeometryRef()
results = {'north' : None,'south' : None}
findPoints(geometry, results)

print "\nNorthernmost point is (%0.4f, %0.4f)" % results['north']
print "Southernmost point is (%0.4f, %0.4f)" % results['south']

print '\nDistance between Northmost and Southmost points of %s is %d KM'%(maps[choice],Great_circle(results['north'],results['south']))




