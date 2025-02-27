

def get_type_futures(data, futures_type):
    try:
        result = next(item for item in data["items"] if item["name"] == futures_type)
    except StopIteration:
        result = None
    return result


def get_type_ats(data, ats_type):
    try:
        result = next(item for item in data["items"] if item["type"]["name"] == ats_type)
    except StopIteration:
        result = None
    return result
