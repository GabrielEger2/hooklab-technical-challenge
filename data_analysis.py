import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the JSON data using Pandas
data = pd.read_json('dados_compras.json')

# Explore the first few rows of the dataset
print(data.head())

# Check for missing values in the dataset
missing_values = data.isnull()

# Count the number of missing values in each column
missing_count = missing_values.sum()

# Display the count of missing values
print("Missing Value Counts:")
print(missing_count)
total_cells = data.size
total_missing = missing_values.sum().sum()
percentage_missing = (total_missing / total_cells) * 100

print("\nPercentage of Missing Values:", percentage_missing, "%")

# Get the total number of purchases
total_purchases = data.shape[0]

print("Total Number of Purchases:", total_purchases)

# Analyze the distribution of gender
gender_distribution = data['Sexo'].value_counts()
print("\nGender Distribution:")
print(gender_distribution)

# Calculate the total amount spent on purchases by gender
total_amount_by_gender = data.groupby('Sexo')['Valor'].sum()

def format_currency(amount):
    return f"R${amount:.2f}"

total_amount_by_gender_formatted = total_amount_by_gender.apply(format_currency)

print("\nTotal Amount Spent by Gender:")
print(total_amount_by_gender_formatted)

# Set up Seaborn for better style
sns.set(style="ticks")

# Plot a bar chart for missing value counts
plt.figure(figsize=(10, 6))
missing_count.plot(kind='line', color='orange')
plt.title('Missing Value Counts')
plt.xlabel('Columns')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Plot a bar chart for gender distribution
plt.figure(figsize=(8, 6))
gender_distribution.plot(kind='bar', color=['blue', 'pink', 'purple'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Plot a bar chart for total amount spent by gender
plt.figure(figsize=(8, 6))
total_amount_by_gender.plot(kind='bar', color=['pink', 'blue', 'purple'])
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.xticks(rotation=0)
plt.ticklabel_format(style='plain', axis='y')  # Disable scientific notation
plt.show()