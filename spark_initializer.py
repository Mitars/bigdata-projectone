from pyspark.sql.types import StructType, StructField
from pyspark.sql import SparkSession, DataFrame


def select_key_value(self, key, value):
    """Casts the given columns to a string and gives them a key and value alias.

    Args:
        key (string): The column which represents the key.
        value (string): The column which represents the value.

    Returns:
        DataFrame: The key and value selection.
    """
    return self.selectExpr("CAST(" + key + " AS STRING) key", "CAST(" + value + " AS STRING) value")


def initialize_session(app_name):
    """Initializes the SparkSession.

        Args:
            app_name (string): The name of the application.

        Return
            The initialized SparkSession.
    """
    sparkSession = SparkSession.builder\
        .master("local")\
        .appName(app_name)\
        .getOrCreate()

    sparkSession.sparkContext.setLogLevel("ERROR")
    DataFrame.select_key_value = select_key_value

    return sparkSession


def read_stream(spark_session, drop_path, schema):
    """Reads the files as a stream.

        Args:
            sparkSession (SparkSession): The SparkSession.
            dropLocation (string): The location from where the stream will be read.
            schema (list): A list of tuples where the first element is the type and the second is the column name.

        Return
            The file stream DataFrame.
    """
    fileStreamDF = spark_session.readStream\
        .option("header", "true")\
        .option("maxFilesPerTrigger", 1)\
        .schema(StructType([StructField(field[1], field[0](), True) for field in schema]))\
        .csv(drop_path)

    print("\nThe stream is " +
          ("ready!\n" if fileStreamDF.isStreaming else "NOT ready!\n"))
    print("Schema:")
    fileStreamDF.printSchema()

    return fileStreamDF
