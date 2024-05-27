import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): A Python dictionary with data to serialize.
        filename (str): The filename of the output JSON file.
    
    If the output file already exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file to a Python dictionary.
    
    Args:
        filename (str): The filename of the input JSON file.
    
    Returns:
        dict: A Python dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

# Example usage:
if __name__ == "__main__":
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    filename = 'data.json'
    
    serialize_and_save_to_file(data, filename)
    loaded_data = load_and_deserialize(filename)
    print(loaded_data)  # Output should match the input dictionary data