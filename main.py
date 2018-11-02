import sys
import spark_kafka_producer
import general_config as cfg


def printAvailableProducers(producers):
    """Prints the available producers.

    Args:
        producers (list): The list of available producers.
    """
    print("available producers:")
    for p in producers:
        print("\t- " + p.name)
    print("")


def incorrectProducerArgument(producers, producer_name=None):
    """prints an error message when the arguments have not been specified correctly.

    Args:
        producers (list): The list of available producers.
        producer_name (string, optional): Defaults to None. the name of the producer which was not found in the list of available producers.
    """
    print("")
    if producer_name:
        print("No producer called \"" + producer_name + "\" available.")
    print("Please specify an existing producer as an argument.")
    printAvailableProducers(producers)
    print("Example: spark-submit --packages " + cfg.required_dependencies + " main.py " + cfg.console_bold(producers[0].name) +"\n")


def selectExistingProducer(producers, console_arguments):
    """Tries to select an existing producer.

    Returns:
        producers (list): The list of available producers.
        console_arguments (array): The list of console arguments. The second argument should contain the name of the producer.
    """
    selectedProducer = None
    if len(console_arguments) != 2:
        incorrectProducerArgument(producers)

    else:
        producer_name = sys.argv[1]        
        for p in producers:
            if p.name == producer_name:
                selectedProducer = p

        if not selectedProducer:
            incorrectProducerArgument(producers, producer_name)

    return selectedProducer


if __name__ == "__main__":
    # Select the producer
    selectedProducer = selectExistingProducer(cfg.activeProducers, sys.argv)

    if not selectedProducer:
        sys.exit()

    # Run Stream
    spark_kafka_producer.initialize_kafka_producer_stream(selectedProducer)
