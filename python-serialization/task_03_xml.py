import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename where the XML data should be saved.
    """
    # Create the root element
    root = ET.Element("data")
    
    # Iterate through the dictionary and create sub-elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to strings for XML
    
    # Create an ElementTree object and write to file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a dictionary.

    Args:
        filename (str): The filename to read the XML data from.

    Returns:
        dict: A dictionary containing the deserialized data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Reconstruct the dictionary
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary