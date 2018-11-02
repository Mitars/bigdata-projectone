from producers.producer import Producer
from producers.columnsdescription_producer import ColumnDescriptionProducer
from producers.applicationtest_producer import ApplicationTestProducer

# Console Colors
CONSOLE_HEADER = '\033[95m'
CONSOLE_OKBLUE = '\033[94m'
CONSOLE_OKGREEN = '\033[92m'
CONSOLE_WARNING = '\033[93m'
CONSOLE_FAIL = '\033[91m'
CONSOLE_ENDC = '\033[0m'
CONSOLE_BOLD = '\033[1m'
CONSOLE_UNDERLINE = '\033[4m'

def console_bold(text):
    return CONSOLE_BOLD + text + CONSOLE_ENDC

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
producer_columnsdescription.checkpoint_path = "/home/ms/checkpoint/homecredit.columnsdescription/"
producer_applicationtest.checkpoint_path = "/home/ms/checkpoint/homecredit.applicationtest/"
