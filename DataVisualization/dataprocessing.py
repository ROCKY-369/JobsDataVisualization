import pandas as pd

# Load data using Pandas
data = pd.read_csv('data.csv')
rows_before = data.shape[0]

# Check for missing values before cleaning
print("Missing values before cleaning:")
print(data.isnull().sum())

# Data cleaning and manipulation
# Drop rows with any missing values
cleaned_data = data.dropna()

# Convert 'salary' and 'salary_in_usd' columns to numeric
cleaned_data['salary'] = pd.to_numeric(cleaned_data['salary'], errors='coerce')
cleaned_data['salary_in_usd'] = pd.to_numeric(cleaned_data['salary_in_usd'], errors='coerce')

# Convert 'work_year' column to integer and remove decimal part
cleaned_data['work_year'] = pd.to_numeric(cleaned_data['work_year'], errors='coerce', downcast='integer').astype('Int64')

# Filter out rows with NaN values in 'work_year'
cleaned_data = cleaned_data.dropna(subset=['work_year'])

# Filter out outliers in the 'salary' column
cleaned_data = cleaned_data[(cleaned_data['salary'] >= 10000) & (cleaned_data['salary'] <= 500000)]

# Text cleaning (removing the leading/trailing spaces from each text columns)
cleaned_data['job_title'] = cleaned_data['job_title'].str.strip()

# Making text data into the same case - lowercase
cleaned_data['employment_type'] = cleaned_data['employment_type'].str.lower()

# Identify and save duplicate rows
duplicate_rows = cleaned_data[cleaned_data.duplicated(keep=False)]
duplicate_rows.to_csv('duplicate_rows.csv', index=False)

# Remove duplicate rows
cleaned_data = cleaned_data.drop_duplicates()

# Check for missing values after cleaning
print("\nMissing values after cleaning:")
print(cleaned_data.isnull().sum())

# Save the cleaned dataset as a file
cleaned_data.to_csv('final_cleaned_data.csv', index=False)

rows_after = cleaned_data.shape[0]

print("Total rows before cleaning:", rows_before)
print("Total rows after cleaning:", rows_after)
