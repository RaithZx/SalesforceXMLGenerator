import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

from xml.dom import minidom

from tkinter import *
 
window = Tk()
 
def clicked():
    lbl.configure(text="Button was clicked !!")

window.title("Welcome to LikeGeeks app")
window.geometry('230x230')
lbl = Label(window, text="Hello").pack()
 
# lbl.grid(column=3, row=0)
 
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked).pack()
# btn.grid(column=0, row=1)
window.mainloop()

version = '43.0'
key = "ProfilesAndRelated"
# key = "Typical"

# writeToFile("items2.xml", key, version)

templates = {
    "ProfilesAndRelated" :[
        "ApexClass",
        "ApexPage",
        "CustomApplication",
        "CustomMetadata",
        "CustomObject",
        "CustomPermission",
        "CustomTab",
        "FlexiPage",
        "Layout",
        "Profile"
    ],
    "Typical" : [
        "ApexClass",
        "ApexPage",
        "ApexTrigger",
        "CspTrustedSite",
        "CustomApplication",
        "CustomMetadata",
        "CustomObject",
        "CustomPermission",
        "CustomTab",
        "Dashboard",
        "EmailTemplate",
        "FlexiPage",
        "Group",
        "HomePageLayout",
        "Layout",
        "PermissionSet",
        "Profile",
        "Queue",
        "Report",
        "ReportType",
        "Workflow"
    ]
}

def generateXML(template, v):
    # create the file structure
    data = ET.Element('Package')
    data.set("xmlns", "http://soap.sforce.com/2006/04/metadata")
    for metadata in templates[key]:
        types = ET.SubElement(data, 'types')
        members = ET.SubElement(types, 'members')
        members.text= '*'
        name = ET.SubElement(types, 'name')
        name.text = metadata
    version = ET.SubElement(data, 'version')
    version.text=v
    # create a new XML file with the results
    rough_string = ET.tostring(data, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def writeToFile(fileName, key, version):
    myfile = open(fileName, "w")
    myfile.write(generateXML(key, version))
    
# myfile.write( '<?xml version="1.0"?>' )
