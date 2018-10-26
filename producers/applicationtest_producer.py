from pyspark.sql.types import StringType, FloatType
from producers.producer import Producer


class ApplicationTestProducer(Producer):
    def __init__(self):
        self.name = 'applicationtest'
        self.key_value = ("contract_type", "income_total")

    def get_schema(self):
        return [
            (StringType, "id"),
            (StringType, "contract_type"),
            (StringType, "code_gender"),
            (StringType, "flag_own_car"),
            (StringType, "flag_own_realty"),
            (FloatType, "cnt_children"),
            (StringType, "amt_income_total"),
        ]

    def stream_modification(self, file_stream_df):
        return file_stream_df.groupBy(file_stream_df.contract_type)\
            .agg({"amt_income_total": "sum"})\
            .withColumnRenamed("sum(amt_income_total)", "income_total")\
            .orderBy("income_total", ascending=False)
