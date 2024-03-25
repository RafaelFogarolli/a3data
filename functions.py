import pickle

def save_pickle(file_object, file_name):
    """
    Saves an object in binary format (pickle) to a file. 

    Args:
        file_object (any kind of object): The object that will be saved in te file.
        file_name (str): The path to the file where the object will be saved.

    Returns:
        None
    """
    with open(file_name, 'wb') as file_name:
        pickle.dump(file_object, file_name)


def load_pickle(file):
    """
    Loads and returns the contents of a binary file (pickle).

    Args:
        file (str): The path to the file to be uploaded.

    Returns:
        Any object type: The contents of the binary file, deserialized by pickle.
    """
    with open(file, 'rb') as file:
        return pickle.load(file)
    



    