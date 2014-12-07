#Get attributes of a state according to Feature no

from proj1 import layer_feature_name,shapefile


layer = shapefile.GetLayer(0)
maps = layer_feature_name(layer)

for i in maps.items():
	print 'Feature ',i[0],': ',i[1]

choice = int(raw_input("Enter Feature No: "))

print '\nFeature %d has following attributes'%choice
for k,v in layer.GetFeature(choice).items().items():
	s = "||||%s||||%s||||"%(k,v)
	print '\n',s
	print len(s)*'-'

feature = layer.GetFeature(choice)
geometry = feature.GetGeometryRef()
name = geometry.GetGeometryName()

print "\nFeature's geometry data consists of a %s" % name
