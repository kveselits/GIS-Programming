import arcpy

mxd = arcpy.mapping.MapDocument("N:\\GIS Programming\\Activity3.mxd")
print mxd.filePath
layerlist = arcpy.mapping.ListLayers(mxd)

##count the number of broken links within the layer list:
numBrokenLinks = 0
for lyr in layerlist:
    if lyr.isBroken:
        numBrokenLinks += 1
print numBrokenLinks
