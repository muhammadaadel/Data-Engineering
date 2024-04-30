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
3- Create a new notebook, Connect it to the cluster, and run this command to start with spark
  ```
  Spark
  ``` 
  <img src="connect_project_with_cluster.jpg">




