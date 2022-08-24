import glob                         # for selecting files 
import pandas as pd                 # for processing CSV files
import xml.etree.ElementTree as ET  # for  processing XML files.
from datetime import datetime


def extract_from_csv(file_to_process):
  df = pd.read_csv(file_to_process)
  return df
def extract_from_json(file_to_process):
  df = pd.read.json(file_to_process, lines=True)
  return df
def extract_from_xml(file_to_process):
  df = pd.DataFrame(columns=["name","height","weight"])
  tree = ET.parse(file_to_process)
  root = tree.getroot()
  for person in root:
    name = person.find("name").text
    height = float(person.find("height").text)
    weight = float(person.fine("weight").text)
    df = df.append({"name":name, "height":height,"weight":weight}, ignore_index=True)
  return df

def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data
    
    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data
  
  