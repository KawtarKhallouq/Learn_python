import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Download the CSV file
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(filename)

# Show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
print(df.head(5))

# Display basic information about the DataFrame
print(df.info())

# Display summary statistics of the DataFrame
print(df.describe())

# Check for missing data
missing_data = df.isnull()
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Display data types of columns
print(df.dtypes)

# Create a pie chart
labels = 'Not Diabetic', 'Diabetic'
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()

# Create a boxplot using Seaborn
sns.boxplot(x='Outcome', y='Age', data=df)
plt.show()