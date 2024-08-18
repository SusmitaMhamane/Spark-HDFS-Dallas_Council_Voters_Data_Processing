#!/bin/bash
#
# Author: Susmita Vikas Mhamane
# Date: July 8, 2024
# Description: Script to manage Dallas Council voters dataset, including checking, deleting, and uploading to HDFS.
#              This script is part of a data processing pipeline that utilizes Apache Spark for data transformation.

# Source unset_jupyter.sh to ensure clean environment
source ./unset_jupyter.sh
# Check if the dataset exists in HDFS
hdfs dfs -test -e /user/talentum/DallasCouncilVoters.csv.gz
if [ $? -eq 0 ]; then
    echo "File is There"
    hdfs dfs -rm /user/talentum/DallasCouncilVoters.csv.gz
    echo "File Deleted Successfully"
fi
# Upload the dataset to HDFS
hdfs dfs -put ~/test-jupyter/P3/M1/M2/SM1/Dataset/DallasCouncilVoters.csv.gz /user/talentum/
echo "Dataset uploaded to HDFS."

# Execute Spark job to process the dataset
spark-submit dataframe.py

# Clean up environment after job completion
source ./unset_jupyter.sh
echo "Environment cleaned up."

# End of script
