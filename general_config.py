from producers.columnsdescription_producer import ColumnDescriptionProducer
from producers.applicationtest_producer import ApplicationTestProducer

# Global
required_dependencies = "org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.2"
bootstrap_servers = "localhost:9092"

# Producers
producer_columnsdescription = ColumnDescriptionProducer.with_config(
    "columnsdescription",
    "Read Home Credit - Column Descriptions",
    "homecredit.columnsdescription",
    "droplocation/columnsdescription",
    "checkpoint/homecredit.columnsdescription"
)

producer_applicationtest = ApplicationTestProducer.with_config(
    "applicationtest",
    "Read Home Credit - Column Descriptions",
    "homecredit.applicationtest",
    "droplocation/applicationtest",
    "checkpoint/homecredit.applicationtest"
)

activeProducers = [
    producer_columnsdescription,
    producer_applicationtest
]
