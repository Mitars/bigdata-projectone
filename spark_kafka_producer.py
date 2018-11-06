from utils import print_title, console_bold
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
    file_stream_df = spark_initializer.read_stream(
        spark_session, producer.drop_path, producer.get_schema())

    # Converts the dataframe to a JSON format
    result_df = producer.to_json_df(file_stream_df)

    # Stream Data to Kafka
    print("Streaming to Kafka topic \"" + producer.topic + "\" ...")
    print_title("Kafka - Streaming to topic \"" + producer.topic + "\"")

    try:
        result_df.selectExpr("CAST(value AS STRING)")\
            .writeStream\
            .outputMode("append")\
            .format("kafka")\
            .option("kafka.bootstrap.servers", cfg.bootstrap_servers)\
            .option("topic", producer.topic)\
            .option("checkpointLocation", producer.checkpoint_path)\
            .start()\
            .awaitTermination()
    except Exception as e:
        print("")
        print(e)
        print("An error occured.")
        print("Are you missing the required dependencies?")
        print("Example: spark-submit " + console_bold("--packages " + cfg.required_dependencies) + " main.py " + cfg.activeProducers[0].name + "\n")
