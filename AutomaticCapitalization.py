ForestType = 'Decidous'
print(ForestType)
print(ForestType[2])

ZIP = '99004-2013'
print(ZIP)
if(len(ZIP) > 5):
    ZIP5 = ZIP[:5]
print(ZIP5)

Cities = ['Spokane', 'Cheney', 'Medical Lake']
print(Cities)

#Cities = [Cities[0].upper(), Cities[1].upper(), Cities[2].upper()]

#dynamically convert city to uppercase or lowercase based on current capitalization
def toUpperOrLower(cities):
    i = 0
    if(cities[0][0].isupper() and cities[1][0].isupper() and cities[2][0].isupper()):
        for x in cities:
            cities[i] = x.lower()
            i = i + 1
    elif(cities[0][0].islower() and cities[1][0].islower() and cities[2][0].islower()):
        for x in cities:
            cities[i] = x[0].upper() + x[1:]
            i = i + 1
    return cities

toUpperOrLower(Cities)

print Cities + ["Converted to lowercase"]

toUpperOrLower(Cities)

print Cities + ["Converted to uppercase"]
