from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import numpy as np
from statistics import mean, median, mode
import matplotlib.pyplot as plt


from collections import defaultdict


filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"


all_incomes = []
labels = []
all_taxes = []

ubi = 674
minimum_wage = 674

def calculate_weekly_tax(weekly_income):
    # Convert weekly income to annual income
    
    annual_income = weekly_income * 52
    # Calculate annual tax
    if annual_income <= 18200:
        annual_tax = 0
    elif annual_income <= 45000:
        annual_tax = (annual_income - 18200) * 0.16
    elif annual_income <= 135000:
        annual_tax = 4288 + (annual_income - 45000) * 0.30
    elif annual_income <= 190000:
        annual_tax = 31288 + (annual_income - 135000) * 0.37
    else:
        annual_tax = 51638 + (annual_income - 190000) * 0.45

    # Convert annual tax to weekly tax
    weekly_tax = annual_tax / 52
    return weekly_tax


def get_incomes(df):
    incomes = []
    labels = []
    taxes = defaultdict(float)
    
    for idx, row in df.iterrows():
        earn_less_than = int(row['earn_less_than'])
        population = int(row['population_000'])
        money = [earn_less_than] * population
        tax = calculate_weekly_tax(earn_less_than) * population
        
        labels.append(earn_less_than)
        incomes.extend(money)
        taxes[earn_less_than] += tax
    
    return incomes, labels, taxes



def main():
    # Read the CSV file into a DataFrame
    incomes_df = pd.read_csv(data / "incomes.csv")

    # Get incomes, labels, and taxes
    all_incomes, labels, total_taxes = get_incomes(incomes_df)

    # Sort labels and calculate the population count for each income threshold
    sorted_labels = sorted(set(labels))
    population_counts = [all_incomes.count(label) for label in sorted_labels]
    total_taxes_list = [total_taxes[label] for label in sorted_labels]

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot income population counts
    plt.plot(sorted_labels, population_counts, marker='o', linestyle='-', color='b', label='Population Count')

    # Plot total taxes
    plt.plot(sorted_labels, total_taxes_list, marker='x', linestyle='--', color='r', label='Total Taxes Paid')

    # Add title and labels
    plt.title('Income and Taxes Plot')
    plt.xlabel('Income Threshold')
    plt.ylabel('Values')
    plt.legend()

    # Display the plot
    plt.show()

    # Calculate and print statistical measures
    print("Mean Income:", mean(all_incomes))
    print("Median Income:", median(all_incomes))
    print("Mode Income:", mode(all_incomes))
    print("Mean Tax:", mean(total_taxes_list))
    print("Median Tax:", median(total_taxes_list))
    print("Mode Tax:", mode(total_taxes_list))


    


if __name__ == "__main__":
    main()