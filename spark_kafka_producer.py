from utils import print_title
import general_config as cfg
import spark_initializer


def initialize_kafka_producer_stream(producer):
    """Initializes the kafka producer stream.
      Reads the files from a drop location and outputs them to Kafka topic.

    Args:
      producer (Producer): The producer.
    """
    # Spark Configuration
    spark_session = spark_initializer.initialize_session(producer.app_name)
    fileStreamDF = spark_initializer.read_stream(
        spark_session, producer.drop_path, producer.get_schema())

    # Execute dataframe operation
    resultDF = producer.stream_modification(fileStreamDF)

    # Stream Data to Kafka
    print("Streaming to Kafka topic \"" + producer.topic + "\" ...")
    print_title("Kafka - Streaming to topic \"" + producer.topic + "\"")

    try:
        resultDF.select_key_value(producer.key_value[0], producer.key_value[1])\
            .writeStream\
            .outputMode("complete")\
            .format("kafka")\
            .option("kafka.bootstrap.servers", cfg.bootstrap_servers)\
            .option("topic", producer.topic)\
            .option("checkpointLocation", producer.checkpoint_path + producer.topic)\
            .start()\
            .awaitTermination()
    except Exception as e:
        print("")
        print(e)
        print("An error occured.")
        print("Are you missing the required dependencies?")
        print("Example: spark-submit " + cfg.console_bold("--packages " + cfg.required_dependencies) + " main.py " + cfg.activeProducers[0].name + "\n")
