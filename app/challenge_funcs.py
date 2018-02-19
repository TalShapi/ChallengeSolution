from num2words import num2words
import xml.etree.ElementTree as ET
import urllib2, xmltodict, json

def get_station_info(number):
    try:
        url = 'https://feeds.capitalbikeshare.com/stations/stations.xml'
        tree = ET.parse(urllib2.urlopen(url))
        root = tree.getroot()
        obj_to_find = "./station/[id='"+str(number)+"']"
        xml_obj_str = ET.tostring(root.find(obj_to_find))
        dict = xmltodict.parse(xml_obj_str)
        return json.dumps(dict)
    except:
        return "An error occurred"        

def convert_num_to_words(number):
    try:
        str = num2words(int(number))
        formatted_str = str.replace(",","").replace(" and","").replace("-"," ")
        return formatted_str
    except:
        return "An error occurred"