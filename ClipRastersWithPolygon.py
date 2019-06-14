import arcpy
#Clip a set of rasters with a polygon
import os

workspace = "N:\\GIS Programming\\Data\\Activity6"
feature_classes = []

walk = arcpy.da.Walk(workspace, datatype="FeatureClass", type="Polygon")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        feature_classes.append(os.path.join(dirpath, filename))
