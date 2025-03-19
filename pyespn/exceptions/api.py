
class API400Error(Exception):
    """Exception raised when a 400 error is raised from the espn api"""
    def __init__(self, error_code, error_message, message="espn api returned error: "):
        self.error_code = error_code
        self.error_message = error_message
        self.message = f"{message}{self.error_code} | error message {self.error_message})"
        super().__init__(self.message)
