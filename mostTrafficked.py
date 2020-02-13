import os
import csv
import numpy as np

####################
# Global Variables #
####################

curr_path = os.getcwd()

#lut stands for LookUp Table
code_lut = {}
loc_lut = {}
freq_lut = {}
loc_freq_lut = {}

####################
# Helper functions #
####################

'''

parse counts the number of charges that a pump has done in a month.

    -called on every unique key in every months

    -returns code_freq, or the frequency that the pump code that the function was
        called on was used

    -returned data is captured in the respective dictionary

'''

def parse(key, filepath):
    code_freq = 0
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            code = row[1]
            if  code == key:
                code_freq +=1
    code_freq = code_freq // 5
    return code_freq

###################
# Start of script #
###################

'''

    Here the file that stores all the pumps is parsed through to populate the
        global dictionaries with keys that will be populated later.

'''

csv_file = open('Data\\socal_supercharger_posts_mapping.csv','r')
locations = csv.reader(csv_file)
next(locations)
for row in locations:
    temp_code = row[0]
    temp_location_act = row[1]
    temp_location_rep = row[2]
    code_lut.setdefault(temp_code, temp_location_act)
    loc_lut.setdefault(temp_location_act, temp_location_rep)
    loc_freq_lut.setdefault(temp_location_act, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    freq_lut[temp_code] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#Population of dictionaries occurs in this large nest of loops

directory = os.fsencode((curr_path+"\\Data\\field_data"))
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    for key in code_lut:
        code_frequency = parse(key, (curr_path+"\\Data\\field_data\\"+filename))

        if filename.startswith("Jan"):
            freq_lut[key][1] = code_frequency
            loc_freq_lut[code_lut[key]][1] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Feb"):
            freq_lut[key][2] = code_frequency
            loc_freq_lut[code_lut[key]][2] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Mar"):
            freq_lut[key][3] = code_frequency
            loc_freq_lut[code_lut[key]][3] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Apr"):
            freq_lut[key][4] = code_frequency
            loc_freq_lut[code_lut[key]][4] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("May"):
            freq_lut[key][5] = code_frequency
            loc_freq_lut[code_lut[key]][5] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Jun"):
            freq_lut[key][6] = code_frequency
            loc_freq_lut[code_lut[key]][6] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Jul"):
            freq_lut[key][7] = code_frequency
            loc_freq_lut[code_lut[key]][7] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Aug"):
            freq_lut[key][8] = code_frequency
            loc_freq_lut[code_lut[key]][8] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Sep"):
            freq_lut[key][9] = code_frequency
            loc_freq_lut[code_lut[key]][9] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Oct"):
            freq_lut[key][10] = code_frequency
            loc_freq_lut[code_lut[key]][10] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Nov"):
            freq_lut[key][11] = code_frequency
            loc_freq_lut[code_lut[key]][11] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        elif filename.startswith("Dec"):
            freq_lut[key][12] = code_frequency
            loc_freq_lut[code_lut[key]][12] += code_frequency
            freq_lut[key][0] += code_frequency
            loc_freq_lut[code_lut[key]][0] += code_frequency
            continue
        else:
            continue

#output of relevant data to the console

months = ["2019","January","February","March","April","May","June","July","August","September","October","November","December"]

for i, month in enumerate(months):
    max = 0
    max_code = "If you're seeing this, your code is broken"
    max_loc = "If you're seeing this, your code is broken"
    for key in code_lut:
        if freq_lut[key][i] >= max:
            max = freq_lut[key][i]
            max_code = key

    print("In Southern California, the most frequently visited pump " + max_code + " in " + month + " was at " + code_lut[max_code] + " with a total of " + str(max) + " visitors.")
    print("")
    max = 0
    for key in loc_lut:
        if loc_freq_lut[key][i] >= max:
            max = loc_freq_lut[key][i]
            max_loc = key

    print("In Southern California, the most frequently visited pump station in " + month + " was in " + code_lut[max_code] + " with a total of " + str(max) + " visitors.")
    print("")
    print("")
