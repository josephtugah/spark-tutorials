# Kafka Cluster with Spark

Kafka Cluster with Zookeeper and PySpark Jupyter Notebook.

### To start the cluster and create containers
    docker compose build --no-cache

#### Once Build is complete
    docker compose up -d

    - The `-d` flag ensures the container is running in detached mode. The container runs in 
    the background and it's not interrupted in your terminal.

    - Ensure the previous container set up for lesson one is stopped before starting this container to
    prevent port conflicts

