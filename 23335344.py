"""
AUTHOR NAME: MATEI HEPCAL
STUDENT NUMBER: 23335344
"""

def read_csv(csvfile):
    
    """
    Reads CSV file and returns list of its contents.
    Returns "data": lists of lists, each inner list represents a row of the CSV file
    """
    
    with open(csvfile, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            row = line.strip().split(',')
            data.append(row)
        return data


def MaxMin(data, region):
    
    """
    Find city with maximum and minimum populations in the given region.
    Returns list of 2 strings, names of the cities with the maximum and minimum populations
    """
    
    name_col = 0
    population_col = 1
    yearly_change_col = 2
    net_change_col = 3
    land_area_col = 4
    region_col = 5
    
    
    max_pop = 0
    min_pop = 100000000
    population = 0
    max_name = ""
    min_name = ""
    
    
    for row in data[1:]:
        
        if row[region_col] == region and int(row[net_change_col]) > 0:
            population = int(row[population_col])
            
            if population > max_pop:
                max_pop = population
                max_name = row[name_col]
        
            if population < min_pop:
                min_pop = population
                min_name = row[name_col]
        
    return[max_name, min_name]



def stdvAverage(data, region):
    
    """
    Calculates average city population and standard deviation of populations in a given region.
    Returns list of two floats, the average population and the standard deviation.
    """
    name_col = 0
    population_col = 1
    yearly_change_col = 2
    net_change_col = 3
    land_area_col = 4
    region_col = 5
    
    total_population = 0
    count = 0
    
    for row in data:
        
        if row[region_col] == region:
            total_population += int(row[population_col])
            count += 1
            
    if count == 0:
        return[0,0]
        
    avg_population = total_population/count
        
        
    sum_sq_diff = 0
        
    for row in data:
            
        if row[region_col] == region:
            diff = int(row[population_col]) - avg_population
            sum_sq_diff += diff * diff
                
    variance = sum_sq_diff/(count-1)
        
    std_dev = variance ** (1/2)
        
    return[round(avg_population,4), round(std_dev,4)]
        


def sort_by_density(density_list):
    """
    Takes lists of lists where each inner list contains name of a country and its population density.
    Returns the list sorted by descending population density.
    """
    return sorted(density_list, key=lambda x: x[1], reverse = True)

def density(data, region):
    
    """
    Takes country data and region, calculates population density of each country in the given region
    Calls on sort_by_density function to return the sorted list of countries and their population densities
    """
    
    name_col = 0
    population_col = 1
    yearly_change_col = 2
    net_change_col = 3
    land_area_col = 4
    region_col = 5
    
    result = []
    
    for row in data:
        
        if row[region_col] == region:
            
            name = row[name_col]
            population = int(row[population_col])
            area = int(row[land_area_col])
            density = population/area
            result.append([name, round(density,4)])
            
    return sort_by_density(result)



def corr(data, region):
    """
    Calculates correlation coefficient between population and land area for all countries in the given region
    Returns correlation coefficient as a float value.
    """
    
    name_col = 0
    population_col = 1
    yearly_change_col = 2
    net_change_col = 3
    land_area_col = 4
    region_col = 5
    
    population_list = []
    area_list = []
    
    for row in data:
        
        if row[region_col] == region:
            population_list.append(int(row[population_col]))
            area_list.append(int(row[land_area_col]))
            
    n = len(population_list)
    if n == 0:
        return[]
    
    sum_population = sum(population_list)
    sum_area = sum(area_list)
    avg_population = sum_population / n
    avg_area = sum_area / n
    
    numerator = 0
    denom_1 = 0
    denom_2 = 0
    
    for i in range(n):
        
        diff_population = population_list[i] - avg_population
        diff_area = area_list[i] - avg_area
        
        numerator += diff_population * diff_area
        denom_1 += diff_population * diff_population
        denom_2 += diff_area * diff_area
        
    if denom_1 == 0 or denom_2 == 0:
        return 0
    
    correlation = numerator / ((denom_1 * denom_2) ** 0.5)
    
    return round(correlation,4)
    
    
                             
        
        
def main(csvfile, region): 
    
    """
    Main function takes file name and region name and calls functions to perform calculations on the data.
    Returns a tuple containing the results of all calculations.
    """
    data = read_csv(csvfile)
    MaxMin_result = MaxMin(data,region)
    stdvAverage_result = stdvAverage(data, region)
    density_result = density(data, region)
    corr_result = corr(data, region)
    
    return MaxMin_result, stdvAverage_result, density_result, corr_result
    
    

