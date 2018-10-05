import csv
import datetime

f = open("/Users/James/Downloads/guns.csv", 'r')
gun_data = list(csv.reader(f))
header = gun_data[0]
data = gun_data[1:]
# print(data[0:10])

gun_deaths_years = {}
for values in data:
    year = values[1]
    if year in gun_deaths_years:
        gun_deaths_years[year] = gun_deaths_years[year] + 1
    else:
        gun_deaths_years[year] = 1
# print(gun_deaths_years)
dates = []
for values in data:
    year_data = int(values[1])
    month_data = int(values[2])

    dates.append(datetime.datetime(year=year_data, month=month_data, day=1))
print(dates[:5])

date_counts = {}
for values in dates:
    if values in date_counts:
        date_counts[values] = date_counts[values] + 1
    else:
        date_counts[values] = 1
print(date_counts)

# The above code returns all of the gun deaths occurring for each month.

sex_counts = {}
for values in data:
    sex = values[5]
    if sex in sex_counts:
        sex_counts[sex] = sex_counts[sex] + 1
    else:
        sex_counts[sex] = 1
print(sex_counts)

race_counts = {}
for values in data:
    race = values[7]
    if race in race_counts:
        race_counts[race] = race_counts[race] + 1
    else:
        race_counts[race] = 1
print(race_counts)

mapping = {}
for vals in race_counts.keys():
    if vals in mapping:
        pass
    else:
        mapping[vals] = 0
mapping['Asian/Pacific Islander'] = 15834141
mapping['Black'] = 40250635
mapping['Hispanic'] = 44618105
mapping['Native American/Native Alaskan'] = 3739506
mapping['White'] = 197318956
print(mapping)


g = open("/Users/James/Downloads/census.csv", 'r')
census = list(csv.reader(g))

race_per_hundredk = {}
for values in race_counts.keys():
    new = int(race_counts[values]) / int(mapping[values])
    adjusted = new * 100000
    race_per_hundredk[values] = adjusted
print(race_per_hundredk)

intents = []
for values in data:
    intents.append(values[3])

races = []
for values in data:
    races.append(values[7])

homicide_race_counts = {}
for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] = homicide_race_counts[race] + 1

homicide_per_hundredk = {}
for values in homicide_race_counts.keys():
    new = int(homicide_race_counts[values]) / int(mapping[values])
    homicide_race_counts[values] = (new * 100000)
print(homicide_race_counts)
