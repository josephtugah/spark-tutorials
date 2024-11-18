
# Kafka Lab Guide

This guide provides detailed instructions for working with Apache Kafka in a Docker environment. Follow these steps to create topics, produce messages, consume messages, and manage offsets.

---

## Prerequisites

1. Docker installed and running on your system.
2. Kafka running inside a Docker container. Identify your Kafka container ID using:
   ```bash
   docker ps
   ```

---

## Steps

### 1. Connect to the Kafka Container
1. Open a terminal and attach to the running Kafka container:
   ```bash
   docker exec -it <container-id> /bin/bash
   ```
   Replace `<container-id>` with the actual ID of your Kafka container.

---

### 2. List Existing Topics
To list all topics in the Kafka broker, run:
```bash
kafka-topics --list --bootstrap-server localhost:29092
```

---

### 3. Create a Topic
1. Create a topic named `test-topic`:
   ```bash
   kafka-topics --create --topic test-topic --bootstrap-server localhost:29092
   ```

2. Verify the topic details:
   ```bash
   kafka-topics --describe --topic test-topic --bootstrap-server localhost:29092
   ```
   - Screenshot topic's configurations for submission
---

### 4. Create a Topic with Partitions and Replication Factor
1. Create a topic named `test-topic-1` with 3 partitions and a replication factor of 2:
   ```bash
   kafka-topics --create --topic test-topic-1 --partitions 3 --replication-factor 2 --bootstrap-server localhost:29092
   ```

2. Verify the topic's configuration:
   ```bash
   kafka-topics --describe --topic test-topic-1 --bootstrap-server localhost:29092
   ```
   - Screenshot topic's configurations for submission
   - For each partition, specify the leader and the follower
---

### 5. Get Offsets for a Topic
Retrieve offsets for `test-topic-1`:
```bash
kafka-get-offsets --topic test-topic-1 --bootstrap-server localhost:29092
```
  
---

### 6. Produce Messages to a Topic
1. Start a producer for `test-topic-1`:
   ```bash
   kafka-console-producer --topic test-topic-1 --bootstrap-server localhost:29092
   ```

2. Type messages into the terminal, one per line:
   - Add more messages to get 10 lines
   ```
   spark streaming
   kafka is awesome
   welcome to DE class
   ```

3. Exit the producer terminal with **Ctrl+C**.

4. Check the offsets again:
   ```bash
   kafka-get-offsets --topic test-topic-1 --bootstrap-server localhost:29092
   ```
   - Screenshot your offset for submission
---

### 7. Consume Messages from a Topic
1. Open a terminal and connect to the Kafka container:
   ```bash
   docker exec -it <container-id> /bin/bash
   ```

2. Start a consumer for `test-topic-1`:
   ```bash
   kafka-console-consumer --topic test-topic-1 --bootstrap-server localhost:29092
   ```

   - You will not see any messages because the broker is waiting for new messages.

---

### 8. Consume Old Messages
To consume old messages, specify the offset and partition:

1. Read messages from **partition 1** starting from the earliest offset:
   ```bash
   kafka-console-consumer --topic test-topic-1 --bootstrap-server localhost:29092 --partition 1 --offset earliest
   ```

2. Similarly, consume from **partition 0** and **partition 2**:
   ```bash
   kafka-console-consumer --topic test-topic-1 --bootstrap-server localhost:29092 --partition 0 --offset earliest
   kafka-console-consumer --topic test-topic-1 --bootstrap-server localhost:29092 --partition 2 --offset earliest
   ```

---

### 9. Consume Messages Without Specifying Offset and Partition
Run the consumer without additional parameters to read newly produced messages:
```bash
kafka-console-consumer --topic test-topic-1 --bootstrap-server localhost:29092
```

---

### 10. Produce Additional Messages
1. Open another terminal and start a producer for `test-topic-1`:
   ```bash
   kafka-console-producer --topic test-topic-1 --bootstrap-server localhost:29092
   ```

2. Type new messages:
   ```
   hello class
   we are producing
   yeah!!!
   ```

3. Exit the producer with **Ctrl+C**.

4. Check offsets again:
   ```bash
   kafka-get-offsets --topic test-topic-1 --bootstrap-server localhost:29092 --partition 1 --offset earliest
   ```

---

## Summary

This guide covers key Kafka operations including creating topics, producing messages, consuming messages, and managing offsets. By following these steps, you will gain hands-on experience with Apache Kafka in a Dockerized environment.
