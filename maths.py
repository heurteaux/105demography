def get_sum_pairs(population_array):
    info_date = 1960
    result = 0
    
    for info in population_array:
        result += info * info_date
        info_date += 1
    return result

def get_sum_x():
    result = 0
    for info_date in range(1960, 2018):
        result += info_date
    return result

def get_sum_y(population_array):
    result = 0
    for info in population_array:
        result += info
    return result

def sum_x_sqr():
    result = 0
    for info_date in range(1960, 2018):
        result += info_date**2
    return result

def get_sum_pairs_switched(years, population_array):
    return sum(year * population for year, population in zip(years, population_array))

def get_sum_y_sqr(population_array):
    return sum(info**2 for info in population_array)

def linear_regression(population_array):
    n = 58
    sum_x = get_sum_x()
    sum_y = get_sum_y(population_array)
    sum_x_sqr_v = sum_x_sqr()
    sum_y_sqr_v = get_sum_y_sqr(population_array)
    sum_xy = get_sum_pairs_switched(range(1960, 2018), population_array)

    aX = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sqr_v - sum_x**2)
    bX = (sum_y - aX * sum_x) / n

    aY = (n * sum_xy - sum_y * sum_x) / (n * sum_y_sqr_v - sum_y**2)
    bY = (sum_x - aY * sum_y) / n

    print("Fit1")
    print("\tY = {:.2f} X - {:.2f}".format(aX / 1000000, abs(bX / 1000000)))
    print("Fit2")
    print("\tX = {:.2f} Y + {:.2f}".format(aY * 1000000, bY))
        
def do_math(population_array):
    linear_regression(population_array)
