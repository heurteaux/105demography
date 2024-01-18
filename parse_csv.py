import csv
from maths import *

def get_population_array(data, args):
    population_array = [0 for _ in range(len(next(data)) - 2)]
    country_arr = []

    for row in data:
        if row[1] in args[1:]:
            country_arr.append(row[0])
            for i in range(2, len(row)):
                population_array[i - 2] += int(row[i])

    if (len(country_arr) != len(args) - 1):
        print("105demography: Was unable to find data for one of the country codes. Please enter a valid country code.")
        exit(84)
    return population_array, country_arr

def parse_csv(args):
    population_array = None
    try:
        file = open("105demography_data.csv", 'r')
    except:
        print("105demography: Demography data file \"105_demography_data.csv\" file cannot be opened or read.")
        exit(84)
    
    try:
        data = csv.reader(file, delimiter=';')
    except:
        print("105demography: Cannot read csv data. Please make the csv file valid")
        exit(84)
        
    population_array, country_arr = get_population_array(data, args)

    print("Country: ", end="")
    
    for i in range(len(country_arr)):
        if (i != len(country_arr) - 1):
            print("{},".format(country_arr[i]), end=" ")
        else:
            print("{}".format(country_arr[i]))
    do_math(population_array)