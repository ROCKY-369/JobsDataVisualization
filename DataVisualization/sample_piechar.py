#sample pie chart showing the percentage of different experience levels
import pandas as pd
import matplotlib.pyplot as plt

# reading the final cleaned data
cleaned_data = pd.read_csv('final_cleaned_data.csv')

# here we are Counting the number of each experience level
experience_counts = cleaned_data['experience_level'].value_counts()

# Plotting
plt.figure(figsize=(6, 6))
plt.pie(experience_counts, labels=experience_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Experience Levels')
plt.axis('equal')
plt.show()
