import arcpy

#Obtain filepath of table or database that contains address data:
db = "C:/Addresses.dbf"

fields = ["Direction", "Number", "Street", "Address"]

oldName = "Invalid Address"

#Attempt to format direction properly
def Direction(street, direction, oldName):
    abbreviations = ["N ", "S ", "E ", "W "]
    directions = ["NORTH", "SOUTH", "EAST", "WEST"]
    suffixes = ["TH", "ST", "DR", "CIR", "BLVD", "AVE"]

    #print direction
    firstTwoStreet = row[2][:2]
    
    #If direction is empty, attempt to parse full address for direction
    if street != " ":
        if any(x in firstTwoStreet for x in abbreviations):
            print street
            return street
        elif direction in directions:
            tempDir = direction[0]
            print tempDir + " " + street
            return tempDir + " " + street
        else:
            return "Invalid Address"

    #All other values are invalid, so return empty string
    else:
        return oldName
            
with arcpy.da.UpdateCursor(db, fields) as cursor:
    for row in cursor:
        #Concatenate string using parsed values
        newStreet = Direction(row[2], str(row[0]), oldName)
        row[3] = str(int(row[1])) + " " + newStreet
        cursor.updateRow(row)
        oldName = newStreet
        print row[3]
