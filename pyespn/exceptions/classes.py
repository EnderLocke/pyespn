
class JSONNotProvidedError(Exception):
    """Exception raised when the json is not provided"""
    def __init__(self, error_message, message="json object not provided to create class: "):
        self.error_message = error_message
        self.message = f"{message} {self.error_message})"
        super().__init__(self.message)

