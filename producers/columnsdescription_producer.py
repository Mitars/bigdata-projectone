from pyspark.sql.types import StringType
from producers.producer import Producer


class ColumnDescriptionProducer(Producer):
    def __init__(self):
        self.name = 'columnsdescription'
        self.key_value = ("special", "count")

    def get_schema(self):
        return [
            (StringType, "id"),
            (StringType, "table"),
            (StringType, "row"),
            (StringType, "description"),
            (StringType, "special"),
        ]

    def stream_modification(self, file_stream_df):
        return file_stream_df.groupBy(file_stream_df.special)\
            .count()\
            .orderBy("count", ascending=False)
