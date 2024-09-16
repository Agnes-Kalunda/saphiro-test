import pandas as pd
from scipy.stats import shapiro


file_path = '/home/agnes/saphiro/Data Set.xlsx'


data = pd.read_excel(file_path, sheet_name='Sheet1')

# Columns to check for normality
columns_to_check = ['Single leg squat', 'Bilateral landing', 'Unilateral landing', 'Running']

# Function to check normality using Shapiro-Wilk test
def check_normality(df, columns):
    for column in columns:
        stat, p = shapiro(df[column].dropna())  # Drops NA values
        print(f'{column}: w={stat}, p-value={p}') 
        if p > 0.05:
            print(f'{column} looks normal (fail to reject H0)')
        else:
            print(f'{column} does not look normal (reject H0)')
        print('')

check_normality(data, columns_to_check)
