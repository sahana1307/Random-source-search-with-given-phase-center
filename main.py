# This is a sample Python script.
#copy of working code in trial5

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import math
import ast
import csv

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
regra = re.compile(r'phase_centre_ra_deg.*?([0-9.-]+)')
regdec = re.compile(r'phase_centre_dec_deg.*?([0-9.-]+)')
regfile = re.compile(r'output_text_file=../../../../OSKAR-2.7-Example-Data/[\w-]+\.[\w-]+')
phase_ra = []
phase_dec = []
output_file = []
with open('oskar_sim_interferometer.ini') as f:
   for line in f:
     match1 = regra.match(line)
     match2 = regdec.match(line)
     match3 = regfile.match(line)
     if match1:
         phase_ra.append(match1.group(1))
         print(phase_ra)
     if match2:
         phase_dec.append(match2.group(1))
         print(phase_dec)

     if match3:
         output_file.append(match3.group(0))
         new_string = line.split('/')[-1]
         new_string1 = new_string.strip()
         print(new_string1)
f.close()
phase_ra = ", ".join(phase_ra)
phase_dec = ", ".join(phase_dec)
phase_ra = math.radians(float(phase_ra))
phase_dec = math.radians(float(phase_dec))
print(phase_ra)
f2 = open('newfilename10.txt','w')
writer = csv.writer(f2)
the_file = open(new_string1, 'r')
reader = csv.reader(the_file, skipinitialspace=True)
header = next(reader)
writer.writerow(header)
header = next(reader)
writer.writerow(header)
print(header)
for line in the_file:
  x = line.strip().split(',')
  print(x)
  ra_file = math.radians(float(x[0]))
  dec_file = math.radians(float(x[1]))
  inner_radius = math.radians(-10)
  outer_radius = math.radians(10)
  sin_delta_lat = math.sin(0.5 * (phase_dec - dec_file));
  sin_delta_lon = math.sin(0.5 * (phase_ra - ra_file));
  dist = 2.0 * math.asin(math.sqrt(sin_delta_lat * sin_delta_lat + math.cos(dec_file) * math.cos(phase_dec) * sin_delta_lon * sin_delta_lon));
#  if (not(dist >= inner_radius and dist < outer_radius)):
  if (dist >= inner_radius and dist < outer_radius):
#      print([line])
       writer.writerow(x)
