from pyspark.sql.functions import to_json, struct


class ProducerRaw:
    name = ""
    app_name = ""
    topic = ""
    drop_path = ""
    checkpoint_path = ""

    @classmethod
    def with_config(self, name, app_name, topic, drop_path, checkpoint_path):
        """Initializes a new instance of the ProducerRaw class.
        
        Args:
            name (string): The producer name.
            app_name (string): The name of the application.
            topic (string): The topic name.
            drop_path (string): The file drop path.
            checkpoint_path (string): The Kafka checkpoint path.
        """
        self = self()
        self.name = name
        self.app_name = app_name
        self.topic = topic
        self.drop_path = drop_path
        self.checkpoint_path = checkpoint_path
        return self

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
