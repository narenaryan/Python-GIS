#Initialize variables for other programmes to use
import osgeo.ogr

def layer_feature_name(layer):
	return {i:layer.GetFeature(i).GetField("NAME") for i in  range(layer.GetFeatureCount())}


shapefile = osgeo.ogr.Open("tl_2012_us_state.shp")

layers = [shapefile.GetLayer(i) for i in range(shapefile.GetLayerCount())]

'''
#Code for printing all layers features
for layer in layers:
	print layer_feature_name(layers)'''
