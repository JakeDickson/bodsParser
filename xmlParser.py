import os 
from xml.etree import ElementTree
from tabulate import tabulate

# TO USE: Extract XML files to 'xmlParser.py folder'/xml/ and run the python
# file. Output printed to terminal 
# ASSUMPTIONS: TransXChange format used, and files are not corrupt/incorrectly
# filled. 
# FUTURE WORK: Convert to C++ for speed. Extract ZIPs automatically with gzip
# etc. 
# Note: If you change headers, you will need to change headersList and
# table loop to reflect the order change.

#OPTIONS:
fileNameToggle = False #toggles in Tabulate.
indexToggle = True

#Path Roots for easy modification
rootPath = './'
http = '{http://www.transxchange.org.uk/}'
servicesPath = rootPath + http + 'Services/'
servicePath = servicesPath + http + 'Service/'
linePath = servicePath + http + 'Lines/' + http + 'Line/'
standardServicePath = servicePath + http + 'StandardService/'
operatorPath = rootPath + http + 'Operators/'
nationalOperatorCodePath = operatorPath + http + 'Operator/'

#Define table row class. tableRow can be initialised as first row headers
class tableRow:
    def __init__(self):
        self.filePath = ''
        self.fileName = 'File Name'
        self.operatorID = 'Operator ID'
        self.noc = 'NOC'
        self.lineName = 'Line Name'
        self.serviceCode = 'Service Code'
        self.origin = 'Origin'
        self.destination = 'Destination'

#Create list of XML files from directory.
cwd = os.getcwd() + '/xml/'
fileList = os.listdir(cwd)
fileList[:] = [x for x in fileList if x.endswith('.xml')]

#Create list of Services and add static header for Tabulate.
serviceList = []
headerList = tableRow()
if fileNameToggle:
    serviceList.append([headerList.fileName, headerList.serviceCode, headerList.operatorID, headerList.lineName, headerList.origin, headerList.destination]) #for table headers
else:
    serviceList.append([headerList.serviceCode, headerList.operatorID, headerList.lineName, headerList.origin, headerList.destination]) #for table headers
#Assuming there are files in directory, iterate through, insert to tableRow and
#add to list.
for fileName in fileList:
    insertRow = tableRow()
    tree = ElementTree.parse(cwd + fileName)
    root = tree.getroot()

    if tree:
        insertRow.filePath = cwd + fileName
        insertRow.fileName = fileName

    for operatorID in root.findall(operatorPath):
        setattr(insertRow, 'operatorID', operatorID.attrib['id'])

    for noc in root.findall(nationalOperatorCodePath):
        if noc.tag == (http + 'NationalOperatorCode'):
            setattr(insertRow, 'noc', noc.text)

    for line in root.findall(linePath):
        if line.tag == http + 'LineName':
            setattr(insertRow, 'lineName', line.text)

    for service in root.findall(servicePath):
        if service.tag == http + 'ServiceCode':
            setattr(insertRow, 'serviceCode', service.text)

    for serviceRoute in root.findall(standardServicePath):
        if serviceRoute.tag == http + 'Origin':
            setattr(insertRow, 'origin', serviceRoute.text)
        if serviceRoute.tag == http + 'Destination':
            setattr(insertRow, 'destination', serviceRoute.text)

    if fileNameToggle:
        serviceList.append([insertRow.fileName, insertRow.serviceCode, insertRow.operatorID, insertRow.lineName, insertRow.origin, insertRow.destination])
    else:
        serviceList.append([insertRow.serviceCode, insertRow.operatorID, insertRow.lineName, insertRow.origin, insertRow.destination])
print(tabulate(serviceList, headers='firstrow',tablefmt='fancy_grid', showindex=indexToggle)) #print serviceList table