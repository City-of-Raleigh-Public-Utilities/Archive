# ArchiveAndCompress.py
# Archive and Compress by Corey White and Carl Stearns. Raleigh Public Utilities GIS 2014/08/25
###########################################################################################################
# Import arcpy, os, datetime modules
import arcpy, os, datetime, sys
from arcpy import env
arcpy.env.overwriteOutput = True
###########################################################################################################

def Archive():

    #set workspace
    arcpy.env.workspace = "Database Connections\\RPUD.sde" # Need to change this to work where it runs

    #list of datasets to archive
    datasetList = ["RPUD.EVENTS","RPUD.ProjectTracking","RPUD.PU_Boundaries","RPUD.ReclaimedWaterDistributionNetwork","RPUD.Sewer_Features","RPUD.SewerCollectionNetwork","RPUD.WaterDistributionNetwork"]

    #date string for geodb name
    dateString = datetime.datetime.now().strftime("%Y%m%d")

    #create file geodb
    arcpy.CreateFileGDB_management("//corfile/Public_Utilities_NS/5215_Capital_Improvement_Projects/636_Geographic_Info_System/Archive/", "RPUD" + dateString+ ".gdb") #will security settings on this directory prevent copy? If so go \\corfile\Common

    #copy datasets to Archive
    for dataset in datasetList:
        print "archiving " + dataset
        arcpy.Copy_management(dataset, "//corfile/Public_Utilities_NS/5215_Capital_Improvement_Projects/636_Geographic_Info_System/Archive/" + "RPUD" + dateString+ ".gdb/" + dataset ) #will security settings on this directory prevent copy? If so go \\corfile\Common
    print "Archiving complete"

Archive()
