#!/usr/anaconda3/bin/python3.5

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
 
# Directory where you have the GOES-16 Files
dirname = '//dados//fazzt//GOES-R-CMI-Imagery//Band13//'
 
# Put all file names on the directory in a list
G16_images = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMIPF-M*.nc')):
 G16_images.append(filename)
 
# If the log file doesn't exist yet, create one
file = open('//produtos//ch13//G16_Log.txt', 'a')
file.close()
 
# Put all file names on the log in a list
log = []
with open('//produtos//ch13//G16_Log.txt') as f:
 log = f.readlines()
 
# Remove the line feed
log = [x.strip() for x in log]
 
# Compare the directory list with the file list
# Loop through all files in the directory
for x in G16_images:
 # If a file is not on the log, process it
 if x not in log:
  os.system("//usr//anaconda3/bin//python3.5 " + "\"//home//fazzt//scripts_python//process_goes-16.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
