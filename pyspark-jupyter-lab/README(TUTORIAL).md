# PySpark Jupyter Lab Notebook - Python v3.10

Jupyter Lab Notebook with root access.
EaseWithApacheSpark notebooks provided to start with.

### To build image from the Dockerfile:
    docker build --tag easewithdata/pyspark-jupyter-lab .

### To create container from image
    docker run -d -p 8888:8888 -p 4040:4040 --name jupyter-lab easewithdata/pyspark-jupyter-lab


### Click on the container name to open the logs
 - Click on the localhost link with the token endpoint to access the jupyter lab environment.

   
   <img width="950" alt="docker image" src="https://github.com/user-attachments/assets/cfbee07a-36df-4e02-8722-a253f077546f">


# Git LFS and Dataset Retrieval Guide

This guide explains how to resolve issues with Git LFS placeholder files and retrieve the actual datasets tracked by Git LFS.

## Problem
The files tracked by Git LFS appear as placeholders instead of the actual dataset files. This happens if:
- The repository is cloned without Git LFS installed or enabled.

## Solution
Follow the steps below to pull the actual data from the tracked files.

### Step 1: Open an Interactive Shell in Your Docker Container
Run the following command to access your Docker container's shell:
```bash
docker exec -it <container-id> /bin/bash
```

### Step 2: Install Git LFS in Your Docker Container
Update the package list and install Git LFS:
```bash
apt update
apt install -y git-lfs
git lfs install
git lfs --version
```

### Step 3: Change Directory
Navigate to the directory where you will pull the datasets from the GitHub repository:
```bash
cd ./pyspark-zero-to-hero
mkdir new-datasets
cd ./new-datasets
```

### Step 4: Pull Data from the Dataset-Specific Directory
Initialize a new Git repository and configure sparse checkout to fetch only the required datasets:
```bash
git init
git remote add origin https://github.com/subhamkharwal/pyspark-zero-to-hero.git
git config core.sparseCheckout true

echo "datasets" >> .git/info/sparse-checkout

git pull origin master
```

## Notes
- Ensure Git LFS is properly installed and configured before cloning repositories with large files tracked by Git LFS.
- Replace `<container-id>` with the ID of your Docker container.

