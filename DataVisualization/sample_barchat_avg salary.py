#barchat to get Average Salary based on Employment Type and Experience Level

import pandas as pd
import matplotlib.pyplot as plt


cleaned_data = pd.read_csv('final_cleaned_data.csv')

# Group data by 'experience_level' and 'employment_type' and get the mean salary in USD
avg_salary_usd = cleaned_data.groupby(['experience_level', 'employment_type'])['salary_in_usd'].mean().unstack()

plt.figure(figsize=(10, 6))
# Plotting the bar chart with some styles
avg_salary_usd.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral'], width=0.8, ax=plt.gca())

plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')
plt.title('Average Salary in USD by Experience Level & Employment Type')
plt.legend(title='Employment Type', loc='upper left')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
