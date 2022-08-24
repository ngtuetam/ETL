from extract_data import extract_from_csv, extract_from_json, extract_from_xml, extract
from transform_data import transform
from load_data import load
from logging import log

if __name__ == '__main__':
    tmpfile    = "temp.tmp"               # file used to store all extracted data
    logfile    = "logfile.txt"            # all event logs will be stored in this file
    targetfile = "transformed_data.csv"   # file where transformed data is stored

    log("\n ETL Started")
    log("Extract phase Started")
    extracted_data = extract()
    log("Extract phase Ended")
    log("Transform phase Started")
    transformed_data = transform(extracted_data)
    log("Transform phase Ended")
    log("Load phase Started")
    load(targetfile,transformed_data)
    log("Load phase Ended")
    log("ETL Ended\n")