##N:\\GIS Programming\\Data\\toxicWA2009\\toxicWA2009.shp
##N:\\GIS Programming\\Data\\wa_counties\\wa_counties.shp

import arcpy

fc1 = "N:\\GIS Programming\\Data\\wa_counties\\wa_counties.shp"


fc2 = "N:\\GIS Programming\\Data\\toxicWA2009\\toxicWA2009.shp"
print fc1

print fc2

##create feature layer named "countylyr" using the specified path
arcpy.MakeFeatureLayer_management(fc1, "countylyr")
arcpy.MakeFeatureLayer_management(fc2, "toxiclyr")
##select by attribute in the previously created layer, searching within the NAME10 field for "Ki" followed by wildcard
arcpy.SelectLayerByAttribute_management("countylyr", "NEW_SELECTION",'"NAME10" Like \'Ki%\'')
##output selection to a new shapefile
arcpy.CopyFeatures_management("countylyr", "N:\\GIS Programming\\Data\\toxicWA2009\\bento123n.shp")
