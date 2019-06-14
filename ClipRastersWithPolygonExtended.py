import arcpy
#Clip a set of rasters with a polygon

inputFolder = arcpy.GetParameterAsText(0)
arcpy.env.workspace = inputFolder
inputPolyName = arcpy.GetParameterAsText(1)

for myraster in arcpy.ListRasters():
    newname = myraster[0:-4] + "_Clip" + myraster[-4:]
    arcpy.Clip_management(
    myraster,"#",newname, inputPolyName, clipping_geometry="ClippingGeometry")
