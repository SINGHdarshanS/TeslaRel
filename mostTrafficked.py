import os
import csv
import numpy as np
import pyplot from matplotlib as plt

curr_path = os.getcwd()
#LUT stands for LookUp Table
code_lut = {}
loc_lut = {}
freq_lut = {}


def parse(key, filepath):
    code_freq = 0
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            code = reader[0]
            if  code == key:
                code_frequency +=1
    code_frequency = code_frequency/5
    return code_frequency

with open((curr_path+"\\Data\\socal_supercharger_posts_mapping.csv"),'r') as csv_file:
    locations = csv.reader(csv_file)
    next(locations)
    for row in locations:
        temp_code = locations[0]
        temp_location_act = locations[1]
        temp_location_rep = locations[2]

'''
        -assigns keypairing only if key doesn't previously exist
        -unnecessary for code_lut but doesn't hurt to have a bit of protection

'''
        code_lut.setdefault(temp_code, temp_location_act)
        loc_lut.setdefault(temp_location_act, temp_location_rep)
        freq_lut[temp_code] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

directory = os.fsencode((curr_path+"\\Data\\field_data"))
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.startswith("Jan"):

        #parse file
        #for each element in the dictionary, parse through the whole csv and return the frequency into the frequency array in freq_lut
        for key in code_lut:
            freq_arr = parse(key, (curr_path+"\\Data\\field_data\\"+filename))
        continue

    elif filename.startswith("Feb"):
        #parse file
        continue
    elif filename.startswith("Mar"):
        #parse file
        continue
    elif filename.startswith("Apr"):
        #parse file
        continue
    elif filename.startswith("May"):
        #parse file
        continue
    elif filename.startswith("Jun"):
        #parse file
        continue
    elif filename.startswith("Jul"):
        #parse file
        continue
    elif filename.startswith("Aug"):
        #parse file
        continue
    elif filename.startswith("Sep"):
        #parse file
        continue
    elif filename.startswith("Oct"):
        #parse file
        continue
    elif filename.startswith("Nov"):
        #parse file
        continue
    elif filename.startswith("Dec"):
        #parse file
        continue
    else
        continue
