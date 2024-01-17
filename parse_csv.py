import csv

def get_population_array(data, args):
    population_array = [0 for _ in range(len(next(data)) - 2)]

    for row in data:
        if row[1] in args[1:]:
            for i in range(2, len(row)):
                population_array[i - 2] += int(row[i])
    print(population_array)
    return population_array

def parse_csv(args):
    try:
        with open("105demography_data.csv", 'r') as file:
            data = csv.reader(file, delimiter=';')
            population_array = get_population_array(data, args)
    except:
        print("105demograpy: Demography data file \"105_demography_data.csv\" file cannot be opened or read.")
        exit(84)