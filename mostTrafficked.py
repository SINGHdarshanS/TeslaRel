import os
import csv
import numpy as np
from matplotlib import pyplot as plt

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
            code = row[1]
            if  code == key:
                code_freq +=1
    code_freq = code_freq / 5
    return code_freq

csv_file = open('Data\\socal_supercharger_posts_mapping.csv','r')
locations = csv.reader(csv_file)
next(locations)
for row in locations:
    temp_code = row[0]
    temp_location_act = row[1]
    temp_location_rep = row[2]
    code_lut.setdefault(temp_code, temp_location_act)
    loc_lut.setdefault(temp_location_act, temp_location_rep)
    #first index will carry yearly total
    freq_lut[temp_code] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

directory = os.fsencode((curr_path+"\\Data\\field_data"))
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    for key in code_lut:
        print("Parsing "+key + " in " + filename)
        code_frequency = parse(key, (curr_path+"\\Data\\field_data\\"+filename))

        if filename.startswith("Jan"):
            freq_lut[key][1] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of January." )
            continue
        elif filename.startswith("Feb"):
            freq_lut[key][2] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of February." )
            continue
        elif filename.startswith("Mar"):
            freq_lut[key][3] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of March." )
            continue
        elif filename.startswith("Apr"):
            freq_lut[key][4] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of April." )
            continue
        elif filename.startswith("May"):
            freq_lut[key][5] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of May." )
            continue
        elif filename.startswith("Jun"):
            freq_lut[key][6] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of June." )
            continue
        elif filename.startswith("Jul"):
            freq_lut[key][7] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of July." )
            continue
        elif filename.startswith("Aug"):
            freq_lut[key][8] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of August." )
            continue
        elif filename.startswith("Sep"):
            freq_lut[key][9] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of September." )
            continue
        elif filename.startswith("Oct"):
            freq_lut[key][10] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of October." )
            continue
        elif filename.startswith("Nov"):
            freq_lut[key][11] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of November." )
            continue
        elif filename.startswith("Dec"):
            freq_lut[key][12] = code_frequency
            freq_lut[key][0] += code_frequency
            print("There were " + str(code_frequency) + " uses of pump " + key + " in the month of December." )
            continue
        else:
            continue


months = ["2019","January","February","March","April","May","June","July","August","September","October","November","December"]

for i, month in enumerate(months):
    max = 0
    max_code = "If you're seeing this, your code is broken"
    for key in code_lut:
        if freq_lut[key][i] >= max:
            max = freq_lut[key][i]
            max_code = key

    print("In Southern California, the most frequently visited pump location in " + month + " was the " + code_lut[max_code] + " pump with a total of " + str(max) + " visitors.")
