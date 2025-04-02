

def get_type_futures(data, futures_type):
    """
    Retrieves the futures data of a specified type from the provided data.

    Args:
        data (dict): The data containing a list of items under the 'items' key.
        futures_type (str): The name of the futures type to look for.

    Returns:
        dict or None: The first item matching the specified futures type if found, otherwise None.

    Raises:
        KeyError: If the 'items' key is missing from the data.
        StopIteration: If no item with the specified futures type is found in the data.
    """
    try:
        result = next(item for item in data["items"] if item["name"] == futures_type)
    except StopIteration:
        result = None
    return result


def get_type_ats(data, ats_type):
    """
    Retrieves the ATS (Against The Spread) data of a specified type from the provided data.

    Args:
        data (dict): The data containing a list of items under the 'items' key.
        ats_type (str): The name of the ATS type to look for.

    Returns:
        dict or None: The first item matching the specified ATS type if found, otherwise None.

    Raises:
        KeyError: If the 'items' key is missing from the data.
        StopIteration: If no item with the specified ATS type is found in the data.
    """
    try:
        result = next(item for item in data["items"] if item["type"]["name"] == ats_type)
    except StopIteration:
        result = None
    return result
