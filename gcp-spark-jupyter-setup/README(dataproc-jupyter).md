
# Setting Up Apache Spark and Jupyter Notebooks on Google Cloud Dataproc  

---

## Overview  
This guide provides step-by-step instructions for setting up Apache Spark and Jupyter Notebooks on Google Cloud Platform (GCP) using Dataproc. Dataproc simplifies the setup of clusters with pre-installed components like Apache Spark and Jupyter, making it easier to perform data analysis and build machine learning models interactively.  

With Dataproc, you can create a fully functional cluster with Jupyter in under two minutes.

---

## Prerequisites  
1. **GCP Account**:  
   - If you don’t have a GCP account, create one [here](https://console.cloud.google.com/freetrial/signup/tos?hl=en) to receive $300 in free credits.  
   - A credit card is required for account verification.  

2. **Basic Tools**:  
   - Access to Google Cloud Console.  
   - Familiarity with Jupyter Notebooks and basic Apache Spark concepts.  

---

## Setup Steps  

### Step 1: Create a GCP Project  
1. Sign in to [Google Cloud Console](https://console.cloud.google.com).  
2. Create a new project from the dashboard.
   <img width="580" alt="create-spark-project" src="https://github.com/user-attachments/assets/203eea5e-fac2-4840-9560-4ec48882a619">
 
4. Enable billing to use GCP resources.  

### Step 2: Set Up Your Environment  
1. Open **Cloud Shell** (top-right corner in the GCP console).

   <img width="597" alt="3setup-cloud-env" src="https://github.com/user-attachments/assets/3abe9be0-5692-47b7-91f3-31d7c4236f74">

2. Set your project ID:
    ![Screenshot 2024-11-15 192624](https://github.com/user-attachments/assets/c8640599-dafc-4f6d-a258-a20430bf9e7f)

   ```bash
   gcloud config set project <project_id>
   ```  
   Replace `<project_id>` with the ID of your project.  

4. Enable required APIs:
   - Using the cloud shell;
   ```bash
   gcloud services enable dataproc.googleapis.com \
     compute.googleapis.com \
     storage-component.googleapis.com \
     bigquery.googleapis.com \
     bigquerystorage.googleapis.com
   ```
   - Using the GCP Console
     ![Screenshot 2024-11-15 192952](https://github.com/user-attachments/assets/bd0c89db-a930-4aaa-b67f-b6fcd398033f)


### Step 3: Create a Google Cloud Storage (GCS) Bucket  
1. Define your region and bucket name:
   Using the cloud shell
   ```bash
   REGION=us-central1
   BUCKET_NAME=<your-bucket-name>
   ```  
   Replace `<your-bucket-name>` with a unique name. 


3. Create the bucket:  
   ```bash
   gsutil mb -c standard -l ${REGION} gs://${BUCKET_NAME}
   ```  

   You should see the following output
   ```bash
   Creating gs://<your-bucket-name>/...
   ```
   - Navigate to your Cloud Storage UI page on your console
   - Click on the bucket you created
   - Select configurations and change the access control from fine-grain to uniform
![bucket-access-conf](https://github.com/user-attachments/assets/2abdbd65-b842-459e-a802-ac575327c8e2)

---

### Step 4: Create a Dataproc Cluster  
1. Enable the following APIs:  
   - **Cloud Dataproc API**  
   - **Cloud Resource Manager API**  
   - **Compute Engine API**  

   - The Compute Engine default service account is created automatically when you enable the Compute Engine API in your Google Cloud project for the first time.The account is named in the format: PROJECT_NUMBER-compute@developer.gserviceaccount.com
   It is created to allow Compute Engine instances (VMs) to perform operations on your behalf, such as accessing other Google Cloud services like Cloud Storage or Dataproc.

   - Visit the IAM & Admin interface and assign the following roles to the default compute engine service
   account by clicking on the pen symbol next to the service account.
   

2. Define cluster variables: 
   Set the environment variables for your cluster 
   ```bash
   REGION=us-central1
   ZONE=us-central1-a
   CLUSTER_NAME=<your-cluster-name>
   BUCKET_NAME=<your-bucket-name>
   ```  

3. Create your Dataproc Cluster with Jupyter & Component Gateway:
   - Then run this gcloud command to create your cluster with all the necessary components to work with Jupyter on your cluster.

   ```bash
   gcloud beta dataproc clusters create ${CLUSTER_NAME} \
     --region=${REGION} \
     --image-version=1.5 \
     --master-machine-type=n2-standard-2 \
     --worker-machine-type=n2-standard-2 \
     --master-boot-disk-size 50GB \
     --worker-boot-disk-size 50GB \
     --bucket=${BUCKET_NAME} \
     --num-workers 2 \
     --optional-components=ANACONDA,JUPYTER \
     --enable-component-gateway
   ```  

4. Wait for the cluster creation to complete.  
   - Once your cluster is ready you will be able to access your cluster from the Dataproc Cloud console UI.

You should the following output once the cluster is created:

```bash
Created [https://dataproc.googleapis.com/v1beta2/projects/project-id/regions/us-central1/clusters/<your-cluster-name>] Cluster placed in zone [us-central1-a].
```
<img width="746" alt="dataproc-UI" src="https://github.com/user-attachments/assets/053a576e-e4cc-47c7-9011-1aa51273f9ef">

---

### Step 5: Access the JupyterLab Interface  
1. Go to **Dataproc Clusters** in the Cloud Console.  
2. Select your cluster and click on the **Web Interfaces** tab.  
3. Access JupyterLab via the Component Gateway link.  
<img width="746" alt="jupyter-env" src="https://github.com/user-attachments/assets/8d40263f-6d5c-440b-918f-082c19137837">

---

### Step 6: Create and Configure a Notebook  
1. In JupyterLab, create a new Python 3 notebook.  
2. Rename the notebook (e.g., "BigQuery Storage & Spark DataFrames.ipynb").  
3. Configure Spark to use the BigQuery Storage API:  

   - Determine your cluster's Scala version:  
     ```bash
     !scala -version
     ```  

   - Add the appropriate BigQuery connector package to your Spark session:  
     ```python
     from pyspark.sql import SparkSession

     spark = SparkSession.builder \
         .appName('BigQuery Storage & Spark DataFrames') \
         .config('spark.jars.packages', 'com.google.cloud.spark:spark-bigquery-with-dependencies_2.11:0.15.1-beta') \
         .getOrCreate()
     ```  
     Replace `2.11` with `2.12` if your Scala version is 2.12.  

---

## Key Notes on BigQuery Storage API  
- The BigQuery Storage API enables efficient parallel data reads and writes with Spark.  
- Supported serialization formats: Apache Avro, Apache Arrow.  
- Benefits: Improved performance for large datasets.  

---

## Conclusion  
You now have an operational environment with Apache Spark and Jupyter Notebooks on GCP using Dataproc. Use this setup for exploratory data analysis, processing large datasets, or building machine learning models efficiently.  

Happy coding! 🚀  
