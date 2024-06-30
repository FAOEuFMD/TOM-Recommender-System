import pandas as pd
from brick_mapping_preprocessing_functions import add_skills_covered_to_dict

# First import the two data mapping files that have information about which skills (aka bricks) are covered in each course main_topic:

brick_mapping_df = pd.read_excel("data/GET Prepared Training menu mapping_May2024.xlsx", skiprows=1)
additional_mappings_df = pd.read_excel("data/Master_courses.xlsx", "main_topic vs bricks")

# Do some initial cleaning to get that data in a format that we want:

# Make "Main topic" values lowercase for both dataframes:
brick_mapping_df["Main topic"] = brick_mapping_df["Main topic"].str.lower()
additional_mappings_df["main_topic"] = additional_mappings_df["main_topic"].str.lower()

# Insead of having an 'X' indicate whether a course covers a particular skill we will change it to 1
brick_mapping_df.replace(to_replace='X', value=1, inplace=True)
brick_mapping_df.replace(to_replace='x', value=1, inplace=True)

# Insead of keeping the Nan value within the "disease covered" column we will change this to a blank string.
brick_mapping_df["Disease covered"].fillna(value='', inplace=True)
additional_mappings_df["Disease covered"].fillna(value='', inplace=True)

# For all other cells, we want Nan values to be changed to ones. This is because the Nan values represent the brick/ skill NOT being present in the course content
brick_mapping_df.fillna(value=0, inplace=True)
additional_mappings_df.fillna(value=0, inplace=True)

# Select only the columns of interest from the brick_mapping_df. Choose the columns that have a match in additional_mappings_df:

brick_mapping_df = brick_mapping_df[['Main topic', 'Disease covered',
       'Simulation exercises','Training', 'Laboratories', 
       'Contingency planning', 'Assessment',
       'Identification, Registration and traceability', 'Risk assessment',
       'Information data management', 'Models', 'Surveillance', 'Awareness',
       'Clinical Examination', 'Epidemiological Investigation', 'Sampling',
       'Farm biosecurity', 'Personal biosecurity', 'Communication', 'Disposal',
       'Humane killing of animals', 'Vaccination', 'Cleaning and disinfection',
       'Movement control', 'Restricted zones', 'Psychological support',
       'Resource and impact tools and calculators', 'Logistic',
       'National emergency anagement', 'Coordination and PPP', 'Wildlife',
       'Recovery of disease status', 'Vaccination exit strategy',
       'Re-stocking']]

# Rename the columns in the brick_mapping_df so that the column names match the column names in additional_mappings_df

original_columns = brick_mapping_df.columns.tolist()
add_columns = additional_mappings_df.columns.tolist()

rename_cols = {}
original_columns = brick_mapping_df.columns.tolist()
add_columns = additional_mappings_df.columns.tolist()

for i in range(brick_mapping_df.shape[1]):
    rename_cols[original_columns[i]] = add_columns[i]

brick_mapping_df.rename(columns=rename_cols, inplace=True)

# now we are ready to merge the two dataframes
frames = [brick_mapping_df, additional_mappings_df]
merged_df = pd.concat(frames)




