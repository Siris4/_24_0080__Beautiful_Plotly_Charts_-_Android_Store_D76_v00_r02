import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Remove the columns "Last_Updated" and "Android_Ver"
df.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)

# Filter the DataFrame for rows where the 'App' column is 'Instagram'
instagram_df = df[df['App'] == 'Instagram']

# Identify all duplicates in the 'Instagram' rows (including the first occurrence)
duplicates_mask = instagram_df.duplicated(keep=False)

# Combine the duplicates and the original row
instagram_duplicates = instagram_df[duplicates_mask]

# Count all Instagram rows
total_instagram_rows = instagram_df.shape[0]

# Calculate the number of duplicates
duplicate_count = total_instagram_rows - 1

# Print the original "Instagram" row and its duplicates
print("Original 'Instagram' entry and its duplicates:")
print(instagram_duplicates)

# Print the final count of duplicates
print(f"Total count of duplicates beyond the first occurrence: {duplicate_count}")
