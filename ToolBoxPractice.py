import arcpy from arcpy import env #Don't have to use arcpy.* ?

import os
env.workspace = arcpy.GetParameterAsText(0)
inFeatureClass = arcpy.GetParameterAsText(1)
outLocation = arcpy.GetParameterAsText(2)

# Use the arcpy.AddMessage command to print a message directly in the tool Results window

arcpy.AddMessage"Finished without crashing!")
