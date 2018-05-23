#import bpy
import xml.etree.ElementTree as ET



#open file & filepath | link with exported file
xmlfile = 'G:\\Projects\\MAZUT\\Spring2018\\assets\\Camera.xml'
XMLimportedCamera = ET.parse(xmlfile)
XMLroot = XMLimportedCamera.getroot()
#read header in order to define origin software

#reject if it is unknown
for child in XMLroot:
    if 'MATRIX' in child.tag:
        attribs = []
        for attr in child.attrib:
            at = child.attrib.get(attr)
            attribs.append((at.split(';')))

    #print (child.attrib)
        print (attribs)
#read file

#disassemble xml file

#update selected cameras or cameras by name
