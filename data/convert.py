import csv
import json

csvfile = open('meanAndStdev.csv', 'r')
jsonfile = open('sdal.json', 'w')

fieldnames = (
        "word",
        "pleasantness_mean",
        "activation_mean",
        "imagery_mean",
        "pleasantness_stdev",
        "activation_stdev",
        "imagery_stdev",
    )
    
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
