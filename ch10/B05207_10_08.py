#spark evaluating history data
import pyspark
import csv
import operator
import itertools
import collections

if not 'sc' in globals():
    sc = pyspark.SparkContext()
               
years = {}
occupations = {}
guests = {}

#The file header contains these column descriptors
#YEAR,GoogleKnowlege_Occupation,Show,Group,Raw_Guest_List

with open('daily_show_guests.csv', 'rb') as csvfile:    
    reader = csv.DictReader(csvfile)
    for row in reader:
        year = row['YEAR']
        if years.has_key(year):
            years[year] = years[year] + 1
        else:
            years[year] = 1
        
        occupation = row['GoogleKnowlege_Occupation']
        if occupations.has_key(occupation):
            occupations[occupation] = occupations[occupation] + 1
        else:
            occupations[occupation] = 1
            
        guest = row['Raw_Guest_List']
        if guests.has_key(guest):
            guests[guest] = guests[guest] + 1
        else:
            guests[guest] = 1

syears = sorted(years.items(), key=operator.itemgetter(1), reverse=True)
soccupations = sorted(occupations.items(), key=operator.itemgetter(1), reverse=True)
sguests = sorted(guests.items(), key=operator.itemgetter(1), reverse=True)

print syears[:5]
print soccupations[:5]
print sguests[:5]