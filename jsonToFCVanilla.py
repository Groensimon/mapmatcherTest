#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Simon
#
# Created:     20-03-2017
# Copyright:   (c) Simon 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
import json

arcpy.env.workspace = 'E:/module7/data/runnerTracks'



#A definition that converts a (geo)json file to a feature class that can be used for mapmatching
def GeoJSONToFC(workspace,inputData,fcname):

    if arcpy.Exists(fcname):
            arcpy.Delete_management(fcname)

    #Loading the EHV0.json file into the script
    with open(inputData) as json_data:
        data = json.load(json_data)

    #creating an empty list called 'tracks' and making data a global attribute
    tracks = []
    global data

    #Adding the _id and coordinates to the list 'tracks'
    for i in data[0]["summary"]:
        ID = i["runid"] #Problem 'string indices must be integers. The _id and runid values have both letters and numbers, meaning they are not numeric, be it integer or float!!
    for j in data[0]["trail"]:
        x,y = float(j[0]),float(j[1])
    tracks.append([ID,[x,y]])

    """
        x,y = [],[]
        for l in data:
            row = l.split()
            x.append(row[0])
            y.append(row[0])
        tracks.append([ID,[x,y]])
        """

    #Creating an empty feature class, adding the necessary attributes for id and the coordinates and reading the data in
    runnerTracks0 = arcpy.CreateFeatureclass_management(workspace,fcname,"POINT",'','','',4326)
    arcpy.AddField_management(runnerTracks0,"ID","TEXT")
    with arcpy.da.InsertCursor(runnerTracks0,["ID","SHAPE@XY"]) as cur:
        for v in coordinates:
            ID = v[0]
            pointGeometry = arcpy.PointGeometry(arcpy.Point(*v[1]))
            row = (ID,pointGeometry)
            cur.insertRow(row)
            print row

#Setting the parameters for the GeoJSONToFC definition
workspace = "D:/runnerTracks"
inputData = "D:/runnerTracks/EHV0.json"
fcname = "tracks00"
GeoJSONToFC(workspace,inputData,fcname)