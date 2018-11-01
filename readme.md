# Project One

Initial version of the project which uses Apache Spark to read data from a csv file, ingests it into Kafka, reads that Kafka topic with Apache Spark and submits it to a Database.

## Producers

Producers are located within the producers subdirectory. In order to create a new producer, add a new Python file in the directory and have it contain a class which inherits from the Producer class. It should override two methods get_schema and stream_modification, and it should have its name and key_value attributes initialized.

Next import the class in the general_config.py file, create an instance, add it to the activeProducer list and initialize its App Name, Topic, Drop Path and Checkpoint Path values.

## Running

In order to execute the application you have to have Kafka up and running (including both Zookeeper and Kafka).
You have to have Python and Spark installed on your system.
To run the file enter the following:

    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.2 main.py applicationtest

Where applicationtest is the name of the producer.
