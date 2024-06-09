import pandas as pd
from brick_mapping_preprocessing_functions import add_skills_covered_to_dict

# First import the data map that has information about which skills (aka bricks) are covered in each course

brick_mapping_df = pd.read_excel("data/get_prepared_competencies_mapping.xlsx", skiprows=1)

# Do some initial cleaning to get that data in a format that we want:

# Insead of having an 'X' indicate whether a course covers a particular skill we will change it to 1
brick_mapping_df.replace(to_replace='X', value=1, inplace=True)

# Insead of keeping the Nan value within the "disease covered" column we will change this to a blank string. There is only one course that does not explicitly have any diseases that are covered in the course content. 
brick_mapping_df["Disease covered"].fillna(value='', inplace=True)

# For all other cells, we want Nan values to be changed to ones. This is because the Nan values represent the brick/ skill NOT being present in the course content
brick_mapping_df.fillna(value=0, inplace=True)

# Convert the brick mapping dataframe into a dict for easier handling:
temp_dict = brick_mapping.to_dict(orient='records')

# Add the course name as a key for each of the course dictionaries to make data retrieval easier:

brick_mapping_dict = {}
for dict_item in temp_dict:
    brick_mapping_dict[dict_item["Course"]] = dict_item

# Add a new key/value pair for each course that contains a list of skills that are covered in the course:

for i in brick_mapping_dict:
    add_skills_covered_to_dict(brick_mapping_dict[i])