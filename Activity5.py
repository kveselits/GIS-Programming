##N:\\GIS Programming\\Data\\toxicWA2009\\toxicWA2009.shp
##N:\\GIS Programming\\Data\\wa_counties\\wa_counties.shp

import arcpy

fc1 = "N:\\GIS Programming\\Data\\wa_counties\\wa_counties.shp"


fc2 = "N:\\GIS Programming\\Data\\toxicWA2009\\toxicWA2009.shp"
print fc1

print fc2

arcpy.MakeFeatureLayer_management(fc1, "countylyr")
arcpy.MakeFeatureLayer_management(fc2, "toxiclyr")
arcpy.SelectLayerByAttribute_management("countylyr", "NEW_SELECTION",'"NAME10" Like \'Ki%\'')
arcpy.CopyFeatures_management("countylyr", "N:\\GIS Programming\\Data\\toxicWA2009\\bento123n.shp")
