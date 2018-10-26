class Producer:
    # Attributes
    name = ""
    key_value = ("", "")
    app_name = ""
    topic = ""
    drop_path = ""
    checkpoint_path = ""

    # Functions
    def get_schema(self):
        """Gets the schema of the DataFrame. 

            Returns: A list of tuples where the first element is the type and the second is the column name.
        """

        pass

    def stream_modification(self, file_stream_df):
        """Modifies the DataFrame stream.

        Args:
            file_stream_df (DataFrame): The DataFrame.
        """

        pass
