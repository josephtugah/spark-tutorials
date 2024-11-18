
# Kafka and Spark Structured Streaming Practice

## Objective
This practice guide provides steps to set up a Kafka producer, post data to a Kafka topic, and use Spark Structured Streaming to process data from the Kafka topic. It is designed to help users understand how Kafka and Spark can work together for real-time data processing.

---

## Prerequisites
1. **Docker** installed and running.
2. A running Docker container named `ed-spark-jupyter-lab` (or equivalent).
3. Kafka and Spark installed or available within the container.
4. Basic understanding of Kafka and Spark Structured Streaming.

---

## Step-by-Step Instructions

### 1. **Access the Docker Container**
Run the following command to access the container:
```bash
docker exec -it <container-id> /bin/bash
```

Replace `<container-id>` with the actual ID of your `ed-spark-kafka` container.

---

### 2. **Understanding Kafka Ports**
- **Port 9092**: Used for external access, where clients connect to Kafka using the host's IP/hostname.
- **Port 29092**: Used for internal access between Docker containers to avoid unnecessary network hops.

---

### 3. **Create a Kafka Topic**
Run the following command to list all topics:
```bash
kafka-topics --list --bootstrap-server localhost:29092
```

To create a topic named `device-data`:
```bash
kafka-topics --create --topic device-data --bootstrap-server localhost:29092
```

---

### 4. **Start your sparksession in 03_reading_from_kafka.ipynb file**
- Write kafka dataframe to read messages from kafka.
- Before running the code to create the data frame, post sample data by following the steps below

### 5. **Post Sample Data to Kafka**
Use the Kafka producer to post data to the `device-data` topic:
```bash
kafka-console-producer --topic device-data --bootstrap-server localhost:29092
```

Post the following sample JSON data in the opened terminal:
```json
{"eventId": "7146c4a8-54ed-4075-b013-c2d99e65d295", "eventOffset": 10012, "eventPublisher": "device", "customerId": "CI00117", "data": {"devices": [{"deviceId": "D002", "temperature": 5, "measure": "C", "status": "SUCCESS"}]}, "eventTime": "2023-01-05 11:13:53.643895"}
```

### 6. **Write stream to Console Sink**
- Execute the code to create the kafka_df dataframe
- Run the rest of the code in the 03_reading_from_kafka.ipynb script and write the output to console sink to check the output (the last block of code)
- Clear the logs in the ed-spark-jupyter-lab container id

### 7. **Post more data into the Producer Terminal**
- Post the following sample device data per record into the command prompt terminal where your Kafka producer terminal is opened


Additional data:
```json
{"eventId": "1f547fd-e335-457e-9a1f-686cfbe903e3", "eventOffset": 10013, "eventPublisher": "device", "customerId": "CI00103", "data": {"devices": [{"deviceId": "D004", "temperature": 23, "measure": "C", "status": "SUCCESS"}]}, "eventTime": "2023-01-05 11:13:53.643895"}
{"eventId": "692e9999-1110-4441-a20e-fd76692e2c17", "eventOffset": 10014, "eventPublisher": "device", "customerId": "CI00109", "data": {"devices": [{"deviceId": "D003", "temperature": 18, "measure": "C", "status": "ERROR"}]}, "eventTime": "2023-01-05 11:13:53.643895"}
{"eventId": "a25e37a0-1488-411c-bb6d-f3f14e9bdd39", "eventOffset": 10061, "eventPublisher": "device", "customerId": "CI00115", "data": {"devices": [{"deviceId": "D004", "temperature": 27, "measure": "C", "status": "STANDBY"}, {"deviceId": "D003", "temperature": 4, "measure": "C", "status": "STANDBY"}, {"deviceId": "D003", "temperature": 12, "measure": "C", "status": "STANDBY"}]}, "eventTime": "2023-01-05 11:13:53.650859"}
{"eventId": "0468eae2-156e-4aa0-b730-b8d661b6f075", "eventOffset": 10073, "eventPublisher": "device", "customerId": "CI00119", "data": {"devices": []}, "eventTime": "2023-01-05 11:13:53.650859"}
```

---

### 8. **Clear Container Logs**
 - Afer posting each device data record, view the logs in the docker container to see how the stream is processing the data.

---

## Summary
- **Kafka Setup**: Created a topic and posted JSON data.
- **Spark Setup**: Configured Spark to read data from Kafka and process it in real time.
- **Data Flow**: Produced sample device data to Kafka, read it using Spark, and displayed it in the console.

This guide provides a foundational understanding of Kafka-Spark integration for real-time streaming analytics.
