from pyspark.sql.types import StringType
from producers.producer import Producer


class ColumnDescriptionProducer(Producer):
    def __init__(self):
        self.name = 'columnsdescription'

    def get_schema(self):
        return [
            (StringType, "id"),
            (StringType, "table"),
            (StringType, "row"),
            (StringType, "description"),
            (StringType, "special"),
        ]
