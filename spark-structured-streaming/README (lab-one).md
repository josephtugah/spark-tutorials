
# Running Spark Streaming with Socket Input Data

This README provides step-by-step instructions for setting up and running a Spark Streaming application that reads data from a TCP socket.

---

## Prerequisites
1. **Docker Installed**: Ensure Docker is installed and running on your system.
2. **Netcat (ncat) Utility**: Required to send test data to the TCP socket.
3. **Jupyter Notebook Environment**: Your Spark Streaming scripts should be in a Jupyter Notebook environment.

---

## Steps

### 1. Install `ncat` in the Docker Container

1. Start your spark structured streaming container and copy the container id of the ed-pyspark-jupyter-lab container

2. Open a command prompt terminal and attach to the running Docker container by running:

   ```bash
   docker exec -it <ed-pyspark-jupyter-lab-container-id> /bin/bash
   ```

3. Update the package manager:
   ```bash
   sudo apt-get update
   ```

3. Install the `ncat` utility:
   ```bash
   sudo apt-get install ncat
   ```

4. Verify the installation:
   ```bash
   ncat -v
   ```
   This should display the version and usage details of `ncat`.

---

### 2. Set Up the Socket Listener
1. Start a TCP socket on port `9999`:

   ```bash
   ncat -l 9999
   ```
   - `-l`: Indicates that `ncat` should act as a listener.
   - `9999`: Specifies the port to listen on.

2. Keep this terminal open as it will act as the data source.

---

### 3. Run the Spark Streaming Notebook
1. Open the `spark-streaming/02_stream_reading_from_sockets.ipynb` file in your Jupyter environment.
2. Run the t

3. The Spark application will wait for incoming data from the socket.

---

### 4. Send Data to the TCP Socket
1. In the `ncat` terminal, type the following messages one line at a time:
   ```
   hello amalitechies
   hello once again
   we meet again
   hello class
   amalitechies de class
   ```

2. The Spark Streaming application should process and display these messages.

---

### 5. View Docker Container Logs
1. Open another terminal and view the logs of your Docker container:
   ```bash
   docker logs <your-container-id>
   ```

2. Observe the logs for Spark Streaming output as the messages are processed.

---

## Troubleshooting
- Ensure the port `9999` is not used by another application.
- If running Spark in a container, ensure the `localhost` and port mapping are correctly configured between the host and the container.
- Restart the `ncat` listener if it disconnects.

---

## Summary
With this setup, your Spark Streaming application can read and process data from a TCP socket using the `ncat` utility. Follow the steps carefully to simulate a streaming data source and monitor the application’s output.
