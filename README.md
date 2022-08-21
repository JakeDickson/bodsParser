# bodsParser - Basic XML Parser for TransXChange formats
![alt text](https://github.com/JakeDickson/bodsParser/blob/master/sampleTable.png?raw=true)

TO USE: Extract XML files to 'xmlParser.py folder'/xml/ and run the python
file (python3). Output is printed to terminal using Tabulate. Included are
some sample xml files for reference.

DEPENDENCIES: xml.etree, tabulate

ASSUMPTIONS: TransXChange format used, and files are not corrupt/incorrectly
filled. 

FUTURE WORK: Convert to C++ for speed. Extract ZIPs automatically with gzip
etc. 

Note: If you change headers, you will need to change headersList and
table loop to reflect the order change.
