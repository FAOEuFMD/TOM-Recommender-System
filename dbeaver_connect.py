import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_df_pymysql(connection_details, query):
    try:
        # Establish the database connection
        conn = pymysql.connect(**connection_details)
    
        # Create the dataframe
        df = pd.read_sql(query, conn)
        
    except pymysql.Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close the connection (VERY IMPORTANT!)
        if conn:
            conn.close()
    return df