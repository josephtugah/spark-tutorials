# Setting Up AWS Cloud Environment for Apache Spark

This guide provides step-by-step instructions for setting up a Hadoop cluster on an Ubuntu EC2 instance.

## Prerequisites
1. **Create an AWS Free Tier Account**
   - Before starting, you need an AWS Free Tier account. If you don’t already have one, you can sign up at the [AWS Free Tier page](https://aws.amazon.com/free).
   
2. **Additional Setup Instruction**
   - [Create a user with administrative access](https://docs.aws.amazon.com/batch/latest/userguide/create-an-iam-account.html)

3. **Create an EC2 Instance**
     - Follow the instructions in this [tutorial to create an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-launch-my-first-ec2-instance.html). Make sure you select the Free Tier option during the instance creation process.
     - **Important**: Do not terminate the EC2 instance after creating it. You will need it running for your Hadoop cluster setup.
        
   **Recommended Youtube Tutorial**
- To help you create your instance and connect to your EC2 instance using Putty, you can refer to this [YouTube tutorial](https://www.youtube.com/watch?v=I_TkA3zK1S4) which covers the steps for creating the EC2 instance and connecting to it using Putty on Windows.

   - [Create a key pair using Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html)  
     *Note: We will be using Putty (an SSH and telnet client) to connect to our EC2 instance, so ensure that the private key-pair selected is in `.ppk` format.*

- **Open Putty and connect to the EC2 VM with the following steps**
  - Hostname: `ubuntu@<Public IP Address of EC2>`
  - Navigate to the Connection section
  - Select SSH
  - Select Auth
  - Select Credentials
  - At the Private
    
<img width="334" alt="Putty Configuration" src="https://github.com/user-attachments/assets/34fa1348-73b4-4b44-bdd7-1ffdf824c440"> 

<img width="331" alt="ppk auth" src="https://github.com/user-attachments/assets/b6523022-be48-489e-893d-77664a6a2077">


---
# Hadoop Cluster Setup on EC2 (Ubuntu)
## Steps

### Step 1: Update and Install Python
1. **Update package list:**
   ```bash
   sudo apt-get update
   ```
2. **Install Python 3.7:**
   ```bash
   sudo apt-get install python3.7
   ```

---

### Step 2: Install Java
1. **Install OpenJDK 8:** Hadoop requires Java to run.
   ```bash
   sudo apt install openjdk-8-jdk
   sudo apt install --reinstall openjdk-8-jdk
   ```
2. **Verify Java Installation Path:**
   ```bash
   ls /usr/lib/jvm/java-8-openjdk-amd64
   ```
3. **Set Java Environment Variables:**
   - Open the shell profile file:
     ```bash
     nano ~/.bashrc
     ```
   - Add the following lines:
     Press the "i" key to interact with the shell profile
     ```bash
     export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
     export PATH=$JAVA_HOME/bin:$PATH
     ```
   - Save and exit the file.
   - Apply the changes:
     ```bash
     source ~/.bashrc
     ```

---

### Step 3: Set up Password-less SSH Login
1. **Install SSH Client and Server:**
   ```bash
   sudo apt-get install openssh-server openssh-client
   ```
2. **Generate SSH Keys:**
   ```bash
   ssh-keygen -t rsa -P ""
   ```
3. **Set up authorized keys:**
   ```bash
   cat /home/ubuntu/.ssh/id_rsa.pub >> /home/ubuntu/.ssh/authorized_keys
   ```
4. **Test SSH Connection:**
   ```bash
   ssh localhost
   ```

---

### Step 4: Hadoop Installation & Configuration
1. **Download Hadoop:**
   ```bash
   wget https://downloads.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
   ```
2. **Move and Extract Hadoop:**
   ```bash
   mv hadoop-3.3.5.tar.gz /home/ubuntu/spark-tutorial/softwares
   cd /home/ubuntu/spark-tutorial/softwares
   sudo tar -xzvf hadoop-3.3.5.tar.gz
   ```

3. **Set Hadoop Environment Variables:**
   - Open the shell profile file:
     ```bash
     nano ~/.bashrc
     ```
   - Add the following Hadoop environment variables:
     ```bash
     export HADOOP_HOME=/home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5
     export PATH=$PATH:$HADOOP_HOME/bin
     export PATH=$PATH:$HADOOP_HOME/sbin
     export HADOOP_MAPRED_HOME=$HADOOP_HOME
     export HADOOP_COMMON_HOME=$HADOOP_HOME
     export HADOOP_HDFS_HOME=$HADOOP_HOME
     export YARN_HOME=$HADOOP_HOME
     export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
     export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
     ```
   - Save and exit the file.
   - Apply the changes:
     ```bash
     source ~/.bashrc
     ```
4. **Verify Hadoop Installation:**
   ```bash
   hadoop version
   ```

5. **Set JAVA_HOME in Hadoop Configuration:**

   - Open `hadoop-env.sh`:
     ```bash
     sudo nano /home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5/etc/hadoop/hadoop-env.sh
     ```
   - Add JAVA_HOME variable:
     ```bash
     export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
     ```

---

### Step 5: Configure Hadoop Filesystem and Directories
1. **Create Hadoop Temporary Directory:**
   ```bash
   sudo mkdir -p /home/ubuntu/spark-tutorial/softwares/hadoop_data/tmp
   ```

2. **Edit Core-Site Configuration:**
   - Open `core-site.xml`:
     ```bash
     sudo nano /home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5/etc/hadoop/core-site.xml
     ```
   - Add the following configuration:
     ```xml
     <configuration>
         <property>
             <name>hadoop.tmp.dir</name>
             <value>/home/ubuntu/spark-tutorial/softwares/hadoop_data/tmp</value>
         </property>
         <property>
             <name>fs.defaultFS</name>
             <value>hdfs://<your-EC2-private-IP-Address>:9000</value>
         </property>
     </configuration>
     ```

3. **Create Directories for NameNode and DataNode:**
   ```bash
   sudo mkdir -p /home/ubuntu/spark-tutorial/softwares/hadoop_data/namenode
   sudo mkdir -p /home/ubuntu/spark-tutorial/softwares/hadoop_data/datanode
   sudo chown -R ubuntu:ubuntu /home/ubuntu/spark-tutorial/softwares
   ```

4. **Edit HDFS-Site Configuration:**
   - Open `hdfs-site.xml`:
     ```bash
     sudo nano /home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5/etc/hadoop/hdfs-site.xml
     ```
   - Add the following configuration:
     ```xml
     <configuration>
         <property>
             <name>dfs.namenode.name.dir</name>
             <value>/home/ubuntu/spark-tutorial/softwares/hadoop_data/namenode</value>
         </property>
         <property>
             <name>dfs.datanode.data.dir</name>
             <value>/home/ubuntu/spark-tutorial/softwares/hadoop_data/datanode</value>
         </property>
         <property>
             <name>dfs.replication</name>
             <value>1</value>
         </property>
     </configuration>
     ```

---

### Step 6: Configure YARN as the Cluster Manager
1. **Edit MapReduce Configuration:**
   - Open `mapred-site.xml`:
     ```bash
     sudo nano /home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5/etc/hadoop/mapred-site.xml
     ```
   - Add the following:
     ```xml
     <configuration>
         <property>
             <name>mapreduce.framework.name</name>
             <value>yarn</value>
         </property>
     </configuration>
     ```

2. **Edit YARN Configuration:**
   - Open `yarn-site.xml`:
     ```bash
     sudo nano /home/ubuntu/spark-tutorial/softwares/hadoop-3.3.5/etc/hadoop/yarn-site.xml
     ```
   - Add the following:
     ```xml
     <configuration>
         <property>
             <name>yarn.nodemanager.aux-services</name>
             <value>mapreduce_shuffle</value>
         </property>
         <property>
             <name>yarn.resourcemanager.webapp.address</name>
             <value><your-EC2-private-IP>:8088</value>
         </property>
     </configuration>
     ```

---

### Step 7: Format HDFS and Start Hadoop Services
1. **Format the NameNode:**
   ```bash
   hdfs namenode -format
   ```
2. **Start HDFS and YARN Services:**
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```
3. **Check Java Processes:**
   ```bash
   jps
   ```

---

### Step 8: Update Security Group Rules
1. **Allow Inbound Rules in Security Group:**
   - Add custom TCP ports for NameNode (9870) and YARN (8088).
   - Set CIDR blocks to `0.0.0.0/0` for access from any IP address.

---

Your Hadoop cluster setup is now complete! You can access the NameNode at `<EC2_Private_IPv4_adresses>:9870` and the YARN dashboard at `<EC2_Private_IPv4_adresses>:8088`.
