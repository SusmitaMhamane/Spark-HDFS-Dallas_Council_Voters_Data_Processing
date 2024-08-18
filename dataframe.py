#!/usr/bin/python
#
# Author: Susmita Vikas Mhamane
# Date: July 8, 2024
# Description: This script processes the Dallas Council voters dataset using Apache Spark.
#              It performs data cleaning and transformation operations on the CSV file,
#              extracts first name, middle name (if available), and last name from the 'VOTER_NAME' field,
#              and demonstrates various Spark DataFrame operations.
#

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, split, size, concat_ws
import pyspark.sql.functions as F
from pyspark import SparkContext, SparkConf

# Initialize Spark session
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()
sc = spark.sparkContext

# Load the CSV file
voter_df1 = spark.read.format('csv').options(Header=True).load('DallasCouncilVoters.csv.gz')
# Print the schema of the initial DataFrame
print("Schema of the original DataFrame:")
voter_df1.printSchema()

# Perform data transformations
print("Adding a new column called splits separated on whitespace")
voter_df2 = voter_df1.withColumn('splits', F.split('VOTER_NAME', '\s+'))
# Print the schema of the transformed DataFrame
print("Schema after adding 'splits' column:")
voter_df2.printSchema()
# Display the transformed DataFrame
print("Showing the transformed DataFrame:")
voter_df2.show(truncate=False)

# Extract first name from 'splits'
print("Creating a new column called first_name based on the first item in splits")
voter_df3 = voter_df2.withColumn('first_name', voter_df2.splits.getItem(0))
# Print the schema after adding 'first_name'
print("Schema after adding 'first_name' column:")
voter_df3.printSchema()
# Display DataFrame with 'first_name'
print("Showing DataFrame with 'first_name':")
voter_df3.show()

# Extract last name from 'splits'
print("Getting the last entry of the splits list and creating a column called last_name")
voter_df4 = voter_df3.withColumn('last_name', voter_df3.splits.getItem(F.size('splits') - 1))
# Display DataFrame with 'last_name'
print("Showing DataFrame with 'last_name':")
voter_df4.show()

# Extract middle name from 'splits' if available
print("Creating a new column called 'middle_name' based on the second item in 'splits' (if available)")
voter_df5 = voter_df4.withColumn('splits', split(col('VOTER_NAME'), ' ')) \
                    .withColumn('middle_name', when(size(col('splits')) > 2, col('splits').getItem(1)).otherwise(''))

# Select and display relevant columns
print("Selecting and displaying 'first_name', 'middle_name', and 'last_name':")
voter_df5.select('first_name', 'middle_name', 'last_name').show()

# Merge 'middle_name' and 'last_name' into 'last_name'
print("Merging 'middle_name' and 'last_name' into a single 'last_name' column")
voter_df6 = voter_df5.withColumn('last_name', concat_ws(' ', col('splits').getItem(1), col('splits').getItem(size('splits') - 1)))

# Select and display final columns
print("Selecting and displaying 'first_name' and 'last_name':")
voter_df6.select('first_name', 'last_name').show(truncate=False)
