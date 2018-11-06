from pyspark.sql.types import StringType, FloatType
from producer_raw import ProducerRaw


class ApplicationTestProducer(ProducerRaw):
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
