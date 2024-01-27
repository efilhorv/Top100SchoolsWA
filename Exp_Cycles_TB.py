import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace the file path with the path to your CSV file
csv_file_path = r'C:\Users\Jose\Documents\PROJECT_18\Data_CSV\Cycle_Routes.csv'
df = pd.read_csv(csv_file_path, delimiter=';')
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

# Explore Distribution of INFRASTRUCT_TYPE
plt.figure(figsize=(12, 8))
sns.countplot(x='INFRASTRUCT_TYPE', data=df)
plt.title('Distribution of INFRASTRUCT_TYPE')
plt.xlabel('INFRASTRUCT_TYPE')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Explore Results by STATUS
plt.figure(figsize=(12, 8))
sns.boxplot(x='STATUS', y='SHAPE_Length', data=df)
plt.title('Distribution of SHAPE_Length by STATUS')
plt.xlabel('STATUS')
plt.ylabel('SHAPE_Length')
plt.xticks(rotation=45, ha='right')
plt.show()

# Correlation Analysis
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()