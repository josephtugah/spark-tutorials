# Base Python 3.10 image
FROM python:3.10

# Expose Ports
EXPOSE 8888 4040

# Change shell to /bin/bash
SHELL ["/bin/bash", "-c"]

# Install OpenJDK (using openjdk-17-jdk-headless)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install nano & vim if available
RUN apt-get update && \
    apt-get install -y nano vim || true

# Setup JAVA_HOME -- useful for docker command line
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/

# Download and Setup Spark binaries
WORKDIR /tmp
RUN wget https://archive.apache.org/dist/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
RUN tar -xvf spark-3.3.0-bin-hadoop3.tgz
RUN mv spark-3.3.0-bin-hadoop3 spark
RUN mv spark / 
RUN rm spark-3.3.0-bin-hadoop3.tgz

# Set up environment variables
ENV SPARK_HOME=/spark
ENV PYSPARK_PYTHON=/usr/local/bin/python
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.5-src.zip
ENV PATH=$PATH:$SPARK_HOME/bin

# Fix configuration files
RUN mv $SPARK_HOME/conf/log4j2.properties.template $SPARK_HOME/conf/log4j2.properties
RUN mv $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf
RUN mv $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh

# Install Jupyter Lab, PySpark, Kafka, boto & Delta Lake
RUN pip install jupyterlab
RUN pip install pyspark==3.3.0
RUN pip install kafka-python==2.0.2
RUN pip install delta-spark==2.2.0
RUN pip install boto3

# Change to working directory and clone git repo
WORKDIR /home/jupyter

# Clone Ease with Apache Spark Repo to Start
RUN git clone https://github.com/subhamkharwal/pyspark-zero-to-hero.git

# Fix Jupyter logging issue
RUN ipython profile create
RUN echo "c.IPKernelApp.capture_fd_output = False" >> "/root/.ipython/profile_default/ipython_kernel_config.py"

# Start the container with root privileges
CMD ["python3", "-m", "jupyterlab", "--ip", "0.0.0.0", "--allow-root"]
