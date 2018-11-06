from pyspark.sql.types import StringType
from producer_raw import ProducerRaw


class ColumnDescriptionProducer(ProducerRaw):
    def get_schema(self):
        return [
            (StringType, "id"),
            (StringType, "table"),
            (StringType, "row"),
            (StringType, "description"),
            (StringType, "special"),
        ]
