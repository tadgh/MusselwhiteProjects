import re
import urllib.request
import csv
import sys
import os
import time

if len(sys.argv) != 2:
	print("Incorrect usage! Correct usage is\n\n scrape.exe http://whateverurlyouwanttoscrape.com/whatever\n\n")
	sys.exit(0)
try:
	input_url = str(sys.argv[1])
except:
	print("Something went wrong parsing your argument. Try again?\n")

print("Grabbing source....\n")
f = urllib.request.urlopen(input_url)
print("Matching regex Pattern....\n")
result_set = re.findall(r"""(?:data-position=")([A-Z]{1,2})"\B.+?'\)">([-a-zA-Z .]+)(?:.*?<td>(?:<b>)?)([A-Z@]+(?:<\/?b>)?[@A-Z]+).*?\$([,\d]+)""", str(f.read()))
print("writing excel file....\n")
current_date = time.strftime("%d-%m-%y %H-%M-%S")
with open(current_date +' scrape.csv', 'w', newline='') as csv_file:
	stats_writer = csv.writer(csv_file, dialect='excel')
	for match in result_set:
		new_location = re.sub(r"""[<b>\/]""", "", match[2])
		fixed_list = [match[0], match[1], new_location, match[3]]
		stats_writer.writerow(fixed_list)
print("Finished writing excel file to: " + os.path.abspath(current_date +' scrape.csv'))