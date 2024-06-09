import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dbeaver_connect import create_df_pymysql

def add_skills_covered_to_dict(i):
    skills_covered_in_course = []
    
    for key_value in i:
        if i[key_value] == 1:
            skills_covered_in_course.append(key_value)

    i["skills_covered_in_course"] = skills_covered_in_course