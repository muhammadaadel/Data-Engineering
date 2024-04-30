# (IPL)- Indian Premier League for Cricket analysis till 2017

## Introduction

The goal of this project is to perform data analytics on IPL for Cricket data.

## Cricket-Explained (video)
#### I highly recommend you to watch this video to understand about the game and most importantly to be able to create insights out of the dataset.

[![Data-Engineering](https://img.youtube.com/vi/NZGLHdcw2RM/0.jpg)](https://www.youtube.com/watch?v=NZGLHdcw2RM)

## Architecture 
<img src="Architecture.jpg">

## Technology Used
- Databricks (A jupyter-notebook-like environment made specifically for Data)
- AWS S3
- Pyspark
- Spark SQL
- Matplotlib
- Seaborn

## Dataset Used
#### Indian Premier League till 2017 Data:
This dataset has the ball by ball data of all the Indian Premier League (IPL) matches till 2017 season including balls, teams, players and teams.
#### Source
Link: https://data.world/raghu543/ipl-data-till-2017/workspace/project-summary?agentid=raghu543&datasetid=ipl-data-till-2017

## Steps
1- First, we need to upload dataset to AWS S3 cloud storage by creating an S3 Bucket
- you can create your own bucket or i have made my own publicly accessible, so you might use it if you wish.
  Link: https://eu-north-1.console.aws.amazon.com/s3/buckets/ipl-dataset-till-2017?region=eu-north-1&bucketType=general&tab=objects
  <img src="My S3 Bucket.jpg">
  
2- Then, On Databricks, we'll create a cluster for data processing
  <img src="Cluster.jpg">
  
3- Create a new notebook, Connect it to the cluster, and run the command below to check if everything is working as intended, your screen should look like this:
  ```
  Spark
  ``` 
  <img src="connect_project_with_cluster.jpg">

4- To start working with spark, you have to create a spark session object like below:
```
from pyspark.sql import SparkSession

# create spark seesion object
spark = SparkSession.builder.appName('IPL_Data_Analysis').getOrCreate()
```

5- Now, We're ready to import and read our data from the S3 Bucket we've created:
#### Important note:
- before reading the data using spark syntax, we have to import all the data types used in the dataset,then, define a clear schema for each table, and finally assigning the created schema as an argument when reading the data as follows:
  
  - I will take team.csv as an example since it has a simple schema that is easy to digest:
  ```
  # import types first
  from pyspark.sql.types import StructType, StructField, IntegerType, DecimalType, StringType, BooleanType, DateType

  # create team schema
  team_schema = StructType([
    StructField("team_sk", IntegerType(), True),
    StructField("team_id", IntegerType(), True),
    StructField("team_name", StringType(), True)
  ])
  ```
  
  - then, copy S3 URL for the data you want to read, for example:
    <img src="S3 URL.jpg">
    
  - Finally, use this syntax to read the data:
    ```
    # Read data from AWS S3 Bucket and match it to the defined schema
    team_df = spark.read.format('csv').option('header', 'true').load("S3_URL", schema=Schema_to_match)
    ```
    - So, for team.csv, it will be as follows:
      ```
      # Read team.csv from AWS S3 Bucket and match it to the above defined schema
      team = spark.read.format('csv').option('header', 'true').load("s3://ipl-dataset-till-2017/Team.csv", schema=team_schema)
      ```


6- Finally, i recommend you to run the following not to waste time getting errors from different libraries and functions definition:
```
from pyspark.sql.functions import col, when, sum, avg, row_number, count  # Import functions for transformation 
from pyspark.sql.window import Window   # to work with window function

# For visualization
import matplotlib.pyplot as plt
import seaborn as sns  
```

## Finale
#### Now, you're ready to go and use pyspark and spark SQL for processing and analytics and gain actionable insights using Matplotlib and Seaborn visualization capablities for this complex Cricket game.



