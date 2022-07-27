import os 

with open('lifeexpectancy.csv') as f:

    max_life_general = 0
    min_life_general = 100
    max_life_general_country = ""
    min_life_general_country = ""
    max_life_general_date = 0
    min_life_general_date = 0
    overall_average_life = 0
    overall_max_life_country = ""
    overall_min_life_country = ""
    overall_max_life_age = 0
    overall_min_life_age = 100

    year_input = int(input("Enter the year of interest: "))

    for line in f:
        data = line.strip()
        parts = data.split(",")
        if parts[0].lower() == "entity":
            continue 

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if life_expectancy > max_life_general:
            max_life_general = life_expectancy 
            max_life_general_country = entity
            max_life_general_date = year 

        if life_expectancy < min_life_general:
            min_life_general = life_expectancy
            min_life_general_country = entity 
            min_life_general_date = year 

        if life_expectancy > overall_average_life:
            overall_average_life = life_expectancy 

        if life_expectancy > overall_max_life_age:
            overall_max_life_age = life_expectancy 
            overall_max_life_country = entity 

        if life_expectancy < overall_min_life_age:
            overall_min_life_age = life_expectancy 
            overall_min_life_country = entity 


    print(f"The overall max life expectancy is: {max_life_general} from {max_life_general_country} in {max_life_general_date}")
    print(f"The overall min life expectancy is: {min_life_general} from {min_life_general_country} in {min_life_general_date}")
    print(f"""For the year {year_input} is: 
    The average life expectancy across all countries was {overall_average_life}. 
    The max life expectancy was in {overall_max_life_country} with {overall_max_life_age}.
    The min life expectancy was in {overall_min_life_country} with {overall_min_life_age}. """)

