import arcpy

mxd = arcpy.mapping.MapDocument("N:\\GIS Programming\\Activity3.mxd")
print mxd.filePath
layerlist = arcpy.mapping.ListLayers(mxd)

numlyr = len(layerlist)
print "There are ", numlyr, "layers here"
for eachlayer in layerlist:
    eachlayer.visible = True
    if eachlayer.isRaster:
        eachlayer.visible = False

arcpy.RefreshActiveView()
for eachlayer2 in layerlist:
    print eachlayer2.visible
