# Import necessary Spark SQL functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("SparkSession Test").master("local[*]").getOrCreate()

# Sample data
data = [("Alice", 30),
        ("Bob", 25),
        ("Charlie", 35)]

# Create a DataFrame from the sample data
df = spark.createDataFrame(data, ["name", "age"])

# Show the DataFrame
df.show()

# Perform some transformations and actions
filtered_df = df.filter(col("age") > 30)
count = filtered_df.count()

print(f"Number of people over 30: {count}")

# Perform a simple SQL query on the DataFrame
df.createOrReplaceTempView("people")
sql_df = spark.sql("SELECT name FROM people WHERE age > 30")
sql_df.show()

# Stop the Spark session when done
spark.stop()
