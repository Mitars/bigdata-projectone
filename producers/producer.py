from pyspark.sql.functions import to_json, struct


class Producer:
    name = ""
    app_name = ""
    topic = ""
    drop_path = ""
    checkpoint_path = ""

    def get_schema(self):
        """Gets the schema of the DataFrame. 

            Returns: A list of tuples where the first element is the type and the second is the column name.
        """
        pass

    def to_json_df(self, file_stream_df):
        """Converts the DataFrame stream to a JSON format.

        Args:
            file_stream_df (DataFrame): The DataFrame.

            Returns: A dataframe which holds the data in a JSON format.
        """
        return file_stream_df.select(to_json(struct([file_stream_df[x] for x in file_stream_df.columns])).alias("value"))
