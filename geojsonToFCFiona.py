#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Simon
#
# Created:     22-03-2017
# Copyright:   (c) Simon 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import fiona
from shapely.geometry import shape, mapping


def GeoJSONToShp(inputData, outputData):
    schema = {'geometry': {'type': 'LineString', 'coordinates': [x, y]}, 'properties': {'runid': 'str', 'distance': 'float: 4'}}
    with fiona.open(inputData) as input:
        #Change only the geometry of the schema: LineString -> PolyLine
        input.schema['geometry'] = "PolyLine"
        #Write the PolyLine shapefile
        with fiona.open(outputData, 'w', 'ESRI Shapefile', input.shema.copy(), input.crs) as output:
            for elem in input:
                #GeoJSON to shapely geometry
                geom = shape(elem['geometry'])
                #Shapely PolyLine to GeoJSON
                elem['geometry'] = mapping(geom.polyline)
                output.write(elem)




outputData = 'D:/runnerTracks/EHV0geojson.shp'
inputData = 'D:/runnerTracks/EHV0-clean.geojson'
GeoJSONToShp(inputData, outputData)