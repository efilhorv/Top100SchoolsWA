import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# MySQL connection details (replace with your actual details)
host = 'localhost'
user = 'root'
password = ''
database = 'WA_OPEN_DATA'

# Establish a connection to MySQL server
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
) as connection:
    # Query to select the top 10 rows based on the 2020_Rank from rank_school_top100 table
    query_top_rank = "SELECT * FROM rank_school_top100 ORDER BY `2020_Rank` ASC LIMIT 10"
    df_top_rank = pd.read_sql(query_top_rank, connection)

    # Query to select the bottom 10 rows based on the 2020_Rank from rank_school_top100 table
    query_bottom_rank = "SELECT * FROM rank_school_top100 ORDER BY `2020_Rank` DESC LIMIT 10"
    df_bottom_rank = pd.read_sql(query_bottom_rank, connection)


#--------------------------------------------------------------------------------------------------------
    # query_top_rank = "SELECT * FROM rank_school_top100 ORDER BY `2020_Rank` ASC LIMIT 10"
    # df_top_rank = pd.read_sql(query_top_rank, connection)


    # query_bottom_rank = "SELECT * FROM rank_school_top100 ORDER BY `2020_Rank` DESC LIMIT 10"
    # df_bottom_rank = pd.read_sql(query_bottom_rank, connection)

#------------------------TOP AND BOTTON RANKING SCHOOL_NAME-----------------------------------------


# Now you have DataFrames for both top and bottom 10 ranks
# You can perform your analysis and visualization on these DataFrames
# Example: Plotting a bar chart for the '2020_Rank' column in df_top_rank
sns.barplot(x='School_Name', y='2020_Rank', data=df_top_rank)
plt.title('Top 10 Schools - 2020 Rank (rank_school_top100)')
plt.show()

# Example: Plotting a bar chart for the '2020_Rank' column in df_bottom_rank
sns.barplot(x='School_Name', y='2020_Rank', data=df_bottom_rank)
plt.title('Bottom 10 Schools - 2020 Rank (rank_school_top100)')
plt.show()



#---------------------------------TOP / BOTTON MATH AND ENGLISH---------------------------------------------


plt.figure(figsize=(12, 6))
sns.barplot(x='School_Name', y='English', data=df_top_rank, color='blue', label='English')
sns.barplot(x='School_Name', y='Maths', data=df_top_rank, color='orange', label='Maths', bottom=df_top_rank['English'])
plt.title('Top 10 Schools - English and Maths Scores (rank_school_top100)')
plt.legend()
plt.show()



plt.figure(figsize=(12, 6))
sns.barplot(x='School_Name', y='English', data=df_bottom_rank, color='blue', label='English')
sns.barplot(x='School_Name', y='Maths', data=df_bottom_rank, color='orange', label='Maths', bottom=df_bottom_rank['English'])
plt.title('Botton 10 Schools - English and Maths Scores (rank_school_top100)')
plt.legend()
plt.show()

#--------------------------------- NEW


df_top_rank['Combined_Scores'] = df_top_rank['State_Overall_Score'] + df_top_rank['Socio_Economi_Status'] + df_top_rank['Median_ATAR']
df_bottom_rank['Combined_Scores'] = df_bottom_rank['State_Overall_Score'] + df_bottom_rank['Socio_Economi_Status'] + df_bottom_rank['Median_ATAR']

# Plotting for top schools
plt.figure(figsize=(15, 6))

# Grouped bar chart for top schools
sns.barplot(x='School_Name', y='Combined_Scores', data=df_top_rank, color='purple', label='Combined Scores')

plt.title('Top 10 Schools - Combined Scores')
plt.legend()
plt.show()

# Plotting for bottom schools
plt.figure(figsize=(15, 6))

# Grouped bar chart for bottom schools
sns.barplot(x='School_Name', y='Combined_Scores', data=df_bottom_rank, color='purple', label='Combined Scores')

plt.title('Bottom 10 Schools - Combined Scores')
plt.legend()
plt.show()




#---------------------------------------------------



df = pd.DataFrame({
    'School_Name': pd.Series(df_top_rank['School_Name']),
    'State_Overall_Score': pd.Series(df_top_rank['State_Overall_Score']),
    'Socio_Economi_Status': pd.Series(df_top_rank['Socio_Economi_Status']),
    'Median_ATAR': pd.Series(df_top_rank['Median_ATAR'])
})

# Plot the bar chart
ax = df.plot.bar(figsize=(15, 8))

# Adjust x-axis labels
labs = [round(float(t.get_text()), 1) for t in ax.axes.get_xmajorticklabels()]
ax.set_xticklabels(labs)

# Set the School_Name as x-axis tick labels
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['School_Name'])

plt.title('Top 10 Schools - State_Overall_Score, Socio_Economi_Status, and Median_ATAR Scores')
plt.show()


#----------------------------------------3 towers analyses


df = pd.DataFrame({
    'School_Name': pd.Series(df_bottom_rank['School_Name']),
    'State_Overall_Score': pd.Series(df_bottom_rank['State_Overall_Score']),
    'Socio_Economi_Status': pd.Series(df_bottom_rank['Socio_Economi_Status']),
    'Median_ATAR': pd.Series(df_bottom_rank['Median_ATAR'])
})

# Plot the bar chart
ax = df.plot.bar(figsize=(15, 8))

# Adjust x-axis labels
labs = [round(float(t.get_text()), 1) for t in ax.axes.get_xmajorticklabels()]
ax.set_xticklabels(labs)

# Set the School_Name as x-axis tick labels
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['School_Name'])

plt.title('Top 10 Schools - State_Overall_Score, Socio_Economi_Status, and Median_ATAR Scores')
plt.show()