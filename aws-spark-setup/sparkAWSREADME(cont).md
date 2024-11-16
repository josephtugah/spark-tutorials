
# Apache Spark and PySpark Setup on EC2

This guide provides step-by-step instructions to set up Apache Spark, Scala, sbt, and PySpark on an EC2 instance.

## Prerequisites
- An EC2 instance running Ubuntu with Hadoop installed
- A `.ppk` key file for authentication.

---

## 1. Install Scala
1. Navigate to the software directory:
   ```bash
   cd /home/ubuntu/spark-tutorial/softwares/
   ```
2. Download and extract Scala:
   ```bash
   wget https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz
   tar -xvzf scala-2.12.8.tgz
   ```
3. Update environment variables for Scala:
   ```bash
   echo "export SCALA_HOME=/home/ubuntu/spark-tutorial/softwares/scala-2.12.8" >> ~/.bashrc
   echo "export PATH=\$PATH:\$SCALA_HOME/bin" >> ~/.bashrc
   source ~/.bashrc
   ```

---

## 2. Install sbt
1. Download and extract sbt:
   ```bash
   wget https://github.com/sbt/sbt/releases/download/v1.4.1/sbt-1.4.1.tgz
   tar -xvzf sbt-1.4.1.tgz
   ```
2. Update environment variables for sbt:
   ```bash
   echo "export SBT_HOME=/home/ubuntu/spark-tutorial/softwares/sbt" >> ~/.bashrc
   echo "export PATH=\$PATH:\$SBT_HOME/bin" >> ~/.bashrc
   source ~/.bashrc
   ```

---

## 3. Install Apache Spark
1. Download and extract Spark:
   ```bash
   wget https://downloads.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
   tar -xvzf spark-3.5.3-bin-hadoop3.tgz
   ```
2. Update environment variables for Spark:
   ```bash
   echo "export SPARK_HOME=/home/ubuntu/spark-tutorial/softwares/spark-3.5.3-bin-hadoop3" >> ~/.bashrc
   echo "export PATH=\$PATH:\$SPARK_HOME/bin:\$SPARK_HOME/sbin" >> ~/.bashrc
   source ~/.bashrc
   ```
3. Launch the Spark shell:
   ```bash
   spark-shell
   ```
  
  - CTRL + X to exit the spark shell
  - Scala and Python have different syntax and runtime environments, so you can't directly execute Python code in the Scala REPL.To run PySpark (Python-based Spark code), you need to execute the Python script in a Python environment.

---

## 4. Install PySpark
1. Install the Python virtual environment:
   ```bash
   sudo apt install python3.12-venv
   python3 -m venv pyspark-env
   source pyspark-env/bin/activate
   ```
2. Install PySpark:
   ```bash
   pip install pyspark
   ```

---

## 5. Testing PySpark Code

### Option 1: Transfer File from Local Machine Using pscp

    - Open a terminal or command prompt on your local machine.

    - Run the following command from your local machine:

1. Use `pscp` to copy the pyspark_test.py file to your EC2 instance:
   ```bash
   pscp -i path-to-your-key.ppk path/to/pyspark_test.py ubuntu@your-ec2-public-ip:/home/ubuntu/spark-tutorial/softwares
   ```
   - This will copy `pyspark_test.py` from your local machine to the `/home/ubuntu/spark-tutorial/softwares` directory on the EC2 instance.

2. Run the Python script on the EC2 instance:
   ```bash
   python pyspark_test.py
   ```

### Option 2: Create the File on EC2 Using `nano` or `vim`
1. Use a text editor to create the Python script directly on the EC2 instance:
   ```bash
   nano pyspark_test.py
   ```
2. Paste your Python code, save, and exit.

   Save and exit (CTRL + S, then CTRL + X, then Y to confirm)
   
3. Run the Python script:
   ```bash
   python pyspark_test.py
   ```

---

## 6. Access Spark Web UI
- Navigate to `http://<your-ec2-instance-public-ip>:4040` in your browser.

---

## Notes
- Ensure all paths are accurate based on your EC2 instance setup.
