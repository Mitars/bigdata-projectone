from producers.producer import Producer
from producers.columnsdescription_producer import ColumnDescriptionProducer
from producers.applicationtest_producer import ApplicationTestProducer

# Global
required_dependencies = "org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.2"
bootstrap_servers = "localhost:9092"

# Producers
producer_columnsdescription = ColumnDescriptionProducer()
producer_applicationtest = ApplicationTestProducer()

activeProducers = [
    producer_columnsdescription,
    producer_applicationtest,
]

# App Name
producer_columnsdescription.app_name = "Read Home Credit - Column Descriptions"
producer_applicationtest.app_name = "Read Home Credit - Column Descriptions"

# Topic
producer_columnsdescription.topic = "homecredit.columnsdescription"
producer_applicationtest.topic = "homecredit.applicationtest"

# Drop Path
producer_columnsdescription.drop_path = "droplocation/columnsdescription"
producer_applicationtest.drop_path = "droplocation/applicationtest"

# Checkpoint Path
producer_columnsdescription.checkpoint_path = "checkpoint/homecredit.columnsdescription"
producer_applicationtest.checkpoint_path = "checkpoint/homecredit.applicationtest"
