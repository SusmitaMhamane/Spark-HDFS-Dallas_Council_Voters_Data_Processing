-- Author: Susmita Vikas Mhamane
-- Date: July 8, 2024
-- Description: Script to manage Dallas Council voters dataset, including checking, deleting, and uploading to HDFS. This script is part of a data processing pipeline that utilizes Apache Spark for data transformation.


Dallas Council Voters Data Processing

----------------------------------------------------------------------------------------

Overview:

This project processes a dataset containing information about Dallas Council members' voting records using Apache Spark. The dataset is stored in a CSV file (DallasCouncilVoters.csv.gz) and includes columns for date, title, and voter name.

----------------------------------------------------------------------------------------

Objective:

The objective of this project is to:

Cleanse and prepare the data using Spark DataFrame operations.
Extract meaningful columns such as first name, middle name (if available), and last name from the VOTER_NAME field.
Store the cleaned and transformed data back into HDFS.

----------------------------------------------------------------------------------------

Files Included:

dataframe.py: Python script that performs data processing using Apache Spark DataFrame API.
datframe.sh: Bash script to manage the dataset, including checking its presence, deletion if exists, and uploading to HDFS.
unset_jupyter.sh: Bash script to unset environment variables related to Jupyter notebooks to ensure clean execution in other environments.
DallasCouncilVoters.csv.gz: Dataset containing voting records of Dallas Council members.

----------------------------------------------------------------------------------------

Detailed Steps in dataframe.sh:

Source unset_jupyter.sh: Ensures that any environment variables related to Jupyter are unset before executing further commands.
Check and Delete Dataset: Checks if the dataset (DallasCouncilVoters.csv.gz) exists in HDFS. If it does, deletes the existing dataset to ensure a fresh upload.
Upload Dataset: Copies the dataset from the local file system (~/test-jupyter/...) to HDFS (/user/talentum/).
Execute Spark Job: Initiates the execution of dataframe.py using spark-submit, which processes the dataset using Apache Spark.
Clean Up: After completing the Spark job, sources unset_jupyter.sh again to clean up the environment, ensuring no lingering environment variables affect subsequent operations.
End of Script: Marks the end of the shell script file.

Usage:

Save this script as dataframe.sh.
Ensure the paths (~/test-jupyter/P3/M1/M2/SM1/Dataset/DallasCouncilVoters.csv.gz and /user/talentum/) are adjusted according to your actual file locations and HDFS setup.
Execute the script using bash datframe.sh or ./datframe.sh (after making it executable with chmod +x datframe.sh).

----------------------------------------------------------------------------------------

Steps to Execute:

Environment Setup: Ensure Python and Apache Spark are installed and configured correctly. This project assumes a Spark standalone setup.
Upload Dataset: Run datframe.sh to upload DallasCouncilVoters.csv.gz to HDFS for Spark job execution.
Execute Spark Job: Run spark-submit dataframe.py to execute the Spark job that processes the data.
Output: The processed data will be stored in HDFS or displayed based on the operations in dataframe.py.

----------------------------------------------------------------------------------------

Detailed Steps in dataframe.py:

Initialization: Creates a Spark session (SparkSession) and loads necessary libraries.
Data Loading: Loads the CSV file (DallasCouncilVoters.csv.gz) into a Spark DataFrame (voter_df1).
Data Transformation:
Splits VOTER_NAME into individual components (splits) based on whitespace.
Derives first_name, middle_name, and last_name from VOTER_NAME.
Cleans and organizes the data using various DataFrame operations (withColumn, split, size, concat_ws, etc.).
Output: Displays intermediate schemas and final processed data to validate transformations.

----------------------------------------------------------------------------------------

Dependencies:

Apache Spark: Version 2.4.5 (or compatible with the scripts)
Python: 2.7.17
Hadoop: For HDFS operations

----------------------------------------------------------------------------------------

Notes:

Ensure proper permissions and environment variables are set before running the scripts.
Adjust file paths and configurations (spark-submit options, HDFS paths) based on your environment setup.
For larger datasets or different environments, tweak Spark configurations (spark.executor.memory, spark.driver.memory, etc.) accordingly.