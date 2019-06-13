import arcpy

mxd = arcpy.mapping.MapDocument("N:\\GIS Programming\\Activity3.mxd")
print mxd.filePath
layerlist = arcpy.mapping.ListLayers(mxd)

numlyr = len(layerlist)
print "There are ", numlyr, "layers here"
for eachlayer in layerlist:
    print eachlayer.name

first = layerlist[0]
print first.name

last = layerlist[-1]
print last.name

try:
    print first.contrast
except:
    print "oops"
print first.visible
print first.isFeatureLayer
print last.isFeatureLayer
print last.isRasterLayer

desc_first = arcpy.Describe(first)
first_fields = desc_first.fields
for f in first_fields:
    print f.name

if first.isFeatureLayer:
    print "it is vector"
else:
    print "it is raster"

vnum = 0
rnum = 0

#start the FOR loop
for lyr in layerlist:
    if lyr.isFeatureLayer:
        vnum = vnum + 1
    else:
        rnum = rnum + 1
#end the FOR loop
print "There are", vnum, "vectors"
print "there are", rnum, "rasters"
