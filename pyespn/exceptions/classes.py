
class JSONNotProvidedError(Exception):
    """Exception raised when a 400 error is raised from the espn api"""
    def __init__(self, error_message, message="json object not provided to create class: "):
        self.error_message = error_message
        self.message = f"{message} {self.error_message})"
        super().__init__(self.message)

