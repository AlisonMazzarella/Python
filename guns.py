#Writing program to make calculations based on data from statistics published by the National Gun Violence Institute from 2014 - 2020. 
import csv
import math 

YEAR_COLUMN = 0
DEATHS_COLUMN = 1
SUICIDES_COLUMN = 2
INJURIES_COLUMN = 3
CHILDREN_COLUMN = 4
TEENS_COLUMN = 5
MASS_COLUMN = 6
MURDER_COLUMN = 7
DEFENSIVE_COLUMN = 8
UNINTENTIONAL_COLUMN = 9

def main(): 

    total_death = print_total_deaths() 

    percent = count_children_teens(total_death)
    print(percent)


def print_total_deaths(): 
    """For each year in the gun violence dictionary, print the total deaths for all causes combined for each year.

    Parameter
        guns_dict: a csv file/dictionary that contains data about gun violence per year.
            Each item in the dictionary is in this format:
            [year, deaths, suicides, injuries, children, teens, mass shooting, murder, defensive use, unintentional shooting]
    Return: totals
    """

    try:
    
        with open('guns.csv', 'r') as infile:  
            reader = csv.reader(infile)
            next(reader)
            total = 0
            tot_su = 0
            tot_in = 0
            tot_ch = 0
            tot_te = 0
            tot_ma = 0
            tot_mu = 0
            tot_de = 0
            tot_un = 0

            for row in reader:
                total += int(row[DEATHS_COLUMN])
                tot_su += int(row[SUICIDES_COLUMN])
                tot_in += int(row[INJURIES_COLUMN])
                tot_ch += int(row[CHILDREN_COLUMN])
                tot_te += int(row[TEENS_COLUMN])
                tot_ma += int(row[MASS_COLUMN])
                tot_mu += int(row[MURDER_COLUMN])
                tot_de += int(row[DEFENSIVE_COLUMN])
                tot_un += int(row[UNINTENTIONAL_COLUMN])

                totals = total + tot_su + tot_in + tot_ch + tot_te + tot_ma + tot_mu + tot_de + tot_un 

        print(f"The total number of deaths from gun related violence between 2014 and 2020 was {totals}. ")
        return totals

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def count_children_teens(total_deaths):
    """Count and print the number of deaths for children and teens in the gun violence dictionary. Then compare how much percent wise gun violence
    affects children and teens compared to the other columns. 

    Parameter
        guns_dict: a csv file/dictionary that contains data about gun violence per year.
            Each item in the dictionary is in this format:
            [year, deaths, suicides, injuries, children, teens, mass shooting, murder, defensive use, unintentional shooting]
    Return: percent
    """
    try:

        with open('guns.csv', 'r') as infile:  
            reader = csv.reader(infile)
            next(reader)
            
            tot_ch = 0
            tot_te = 0

            for row in reader:
                tot_ch += int(row[CHILDREN_COLUMN])
                tot_te += int(row[TEENS_COLUMN])

            adolescents = tot_ch + tot_te
    
            percent = adolescents / total_deaths * 100 
            print(f"Gun violence towards children and teens made up {percent:.2f}% of all gun related incidents.") 
            return round(percent, 2)


    except (csv.Error, KeyError) as error:
        print(f"Error: line {reader.line_num} of {infile.name}"
                " is formatted incorrectly.")


if __name__ == "__main__":
    main()