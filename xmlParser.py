import os 
from xml.etree import ElementTree
from tabulate import tabulate

file_name = 'xml/bods3.xml'
full_file = os.path.abspath(os.path.join('', file_name))
tree = ElementTree.parse(full_file)
# print(tree)
root = tree.getroot()
transDate = root.get('CreationDateTime')
# print("CreationDateTime = {val}".format(val=transDate))

# print(root.attrib)
# http = root.get('xmlns')
# print("{val}".format(val = http))

# for elm in root.findall("./{}Operators/{}Operator/".format(http, http)):
#     print(elm.tag)
#     # print(elm.attrib)

#Path Roots for easy modification
rootPath = "./"
http = "{http://www.transxchange.org.uk/}"
servicesPath = rootPath + http + "Services/"
servicePath = servicesPath + http + "Service/"
linePath = servicePath + http + "Lines/" + http + "Line/"
standardServicePath = servicePath + http + "StandardService/"
operatorPath = rootPath + http + "Operators/"
nationalOperatorCodePath = operatorPath + http + "Operator/"


#define class for each table row. Helpfully a tableRow can be initialised as first row headers :)
class tableRow:
    def __init__(self):
        self.operatorID = 'Operator ID'
        self.noc = 'NOC'
        self.lineName = 'Line Name'
        self.serviceCode = 'Service Code'
        self.origin = 'Origin'
        self.destination = 'Destination'

chips = tableRow()

for operatorID in root.findall(operatorPath):
    print(operatorID.attrib['id']) #get operator ID
    setattr(chips, 'operatorID', operatorID.attrib['id'])

for noc in root.findall(nationalOperatorCodePath):
    if noc.tag == (http + "NationalOperatorCode"):
        print(noc.text) #NationalOperatorCode
        setattr(chips, 'noc', noc.text)

for line in root.findall(linePath):
    if line.tag == http + "LineName":
        print(line.text) #LineName
        setattr(chips, 'lineName', line.text)

for service in root.findall(servicePath):
    if service.tag == http + "ServiceCode":
        print(service.tag, service.text) #Service Code/ID?
        setattr(chips, 'serviceCode', service.text)

for serviceRoute in root.findall(standardServicePath):
    if serviceRoute.tag == http + "Origin":
        print(serviceRoute.tag, serviceRoute.text) #Origin
        setattr(chips, 'origin', serviceRoute.text)
    if serviceRoute.tag == http + "Destination":
        print(serviceRoute.tag, serviceRoute.text) #Destination
        setattr(chips, 'destination', serviceRoute.text)

print(chips.serviceCode, chips.operatorID, chips.lineName, chips.origin, chips.destination)