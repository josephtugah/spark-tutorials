
# Course Setup Guide

This repository will guide you through the steps to set up your development environment for learning Spark, PySpark, and related technologies. Please follow the instructions below.

## Step 1: Install Docker Desktop

1. Navigate to the `install-setup-docker` folder.
2. Follow the instructions inside to install **Docker Desktop** on your system. 
   - Docker is required for running containers for your PySpark environment.
   - Make sure Docker is properly installed and running before proceeding to the next step.

## Step 2: Set up PySpark Jupyter Lab Environment

1. After installing Docker, navigate to the `pyspark-jupyter-lab` folder.
2. Use the Dockerfile provided in the folder to create a Docker container for running PySpark in Jupyter Lab.
3. The technical lectures on Spark Core, Spark DataFrames, SparkSQL, and DataFrames will be conducted in the containerized environment.
   - Instructions to build the docker container are in the README file in the `pyspark-jupyter-lab` folder.


4. Once the container is running, open your browser and go to your logs in the Docker container use the provided host link with the token to access the Jupyter Lab environment where you'll be working with PySpark.

## Step 3: Set up Pyspark Jupyter Environment for Structured Streaming

- Refer to the README file in the `spark-structured-streaming` folder

## Step 4: Set up Jupyter Lab Environment Using Dataproc on GCP
- Refer to the README file in the `gcp-spark-jupyter-setup` folder

## Step 5: Set up Apache Spark on Hadoop Cluster in AWS

1. Navigate to the `aws-spark-setup` folder.
2. Follow the instructions inside to set up **Apache Spark** on a Hadoop cluster running in an **EC2 instance** on **AWS**.
3. This setup will allow you to execute distributed Spark jobs on a live cluster.

---

### Further Assistance
If you encounter any issues or have questions, feel free to reach out in the course discussion forum. Happy learning!
