#  Python Crash Course example 16.3
#  
#  Project 2 - Data Visualisation - downloaded data - CSV file format
#
#  Weather data processing raw data


import csv
import matplotlib as plt
import numpy as np
from datetime import datetime

input_file = 'york_egxu_2017.csv'
#input_file = 'kisumu_hkki_2017.csv'
error_file = 'errors.txt'
output_file = str('Processed_-_' + input_file)


raw_data = {}
processed_data = {}
err_values = {}


with open(input_file, 'r') as f:
    """Read the data from the defined file and add it into a list of dictionaries"""
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        try:
            current_date = str(datetime.strptime(row[0], "%Y-%m-%d").date())
            current_temp = int(row[2])
        except ValueError:
            print(current_date, 'missing temperature data')
#            with open(error_file, 'a') as f:
#                f.write(str(new_value['current_date']) + ' ' + 'missing temperature info\n')
        try:
            current_dewp = int(row[3])
        except ValueError:
            print(current_date, 'missing dew point data')
#            with open(error_file, 'a') as f:
#                f.write(str(new_value['current_date']) + ' ' + 'missing dew point info\n')
        try:
            current_winds = float(row[5]) # not sure why it won't read the input directly as a float...
            current_winds = int(current_winds)
        except ValueError:
            print(current_date, 'missing wind speed data')
        try:
            current_windd = int(row[7])
        except ValueError:
            print(current_date, 'missing wind direction data')
        else:
            if current_date in raw_data:
                raw_data[current_date]['temps'].append(current_temp)
                raw_data[current_date]['dewps'].append(current_dewp)
                raw_data[current_date]['winds'].append(current_winds)
                raw_data[current_date]['windd'].append(current_windd%360)
            else:
                raw_data[current_date] = {}
                raw_data[current_date]['temps'] = [current_temp]
                raw_data[current_date]['dewps'] = [current_dewp]
                raw_data[current_date]['winds'] = [current_winds]
                raw_data[current_date]['windd'] = [current_windd%360]

                

#Create an empty file for writing processed data in
with open(output_file, 'w') as f:
    f.write('date,Max TempC,Min TempC,Mean TempC,Max DewpC,Min DewpC,\
Mean DewpC,Max Wind SpeedKph,Min Wind SpeedKph,Mean Wind SpeedKph,\
Mean Wind Direction\n')
    f.close()

#print(raw_data)


for current_date in raw_data:
    # Process the temperature data
    daily_temps = raw_data[current_date]['temps']
    # identify highest temperature for each day
    max_temp = max(daily_temps)
    # identify lowest temperature for each day
    min_temp = min(daily_temps)
    # identify mean temperature for each day
    mean_temp = int(np.mean(daily_temps))

    # Process the dew point data
    daily_dewps = raw_data[current_date]['dewps']
    # identify highest dew point temperature for each day
    max_dewp = max(daily_dewps)
    # identify lowest dew point temperature for each day
    min_dewp = min(daily_dewps)
    # identify mean dew point temperature for each day
    mean_dewp = int(np.mean(daily_dewps))

    # Process the temperature data
    daily_winds = raw_data[current_date]['winds']
    # identify highest temperature for each day
    max_winds = max(daily_winds)
    # identify lowest temperature for each day
    min_winds = min(daily_winds)
    # identify mean temperature for each day
    mean_winds = int(np.mean(daily_winds))

    # Process the temperature data
    daily_windd = raw_data[current_date]['windd']
    # identify mean temperature for each day
    mean_windd = int(np.mean(daily_windd))

    processed_data[current_date] = {}
    processed_data[current_date]['temps'] = [max_temp, min_temp, mean_temp]
    processed_data[current_date]['dewps'] = [max_dewp, min_dewp, mean_dewp]
    processed_data[current_date]['winds'] = [max_winds, min_winds, mean_winds]
    processed_data[current_date]['windd'] = mean_windd
    

    with open(output_file, 'a') as f:
        f.write(str(current_date) + ',' + str(max_temp) + ',' +
        str(min_temp) + ',' + str(mean_temp) + ',' + str(max_dewp) + ',' +
        str(min_dewp) + ',' + str(mean_dewp) + ',' + str(max_winds) + ',' +
        str(min_winds) + ',' + str(mean_winds) + ',' + str(mean_windd) + '\n')



