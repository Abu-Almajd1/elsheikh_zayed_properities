from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("PostgreSQL_PySpark") \
    .config("spark.jars", r"C:\Users\LOQ\Desktop\data_engineering\postgresql-42.3.1.jar") \
    .getOrCreate()

# PostgreSQL connection properties
db_url = "jdbc:postgresql://host.docker.internal:5432/realestate"  
db_properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

# Read data into PySpark DataFrame
df = spark.read.jdbc(url=db_url, table="propertyfinder_data", properties=db_properties)

# Show the first few rows
df.show()


#"C:\Program Files (x86)\Java\jdk-1.8"